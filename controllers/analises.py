from flask import render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import func
from datetime import datetime
from sqlalchemy import case
from sqlalchemy.orm import aliased
from api import app, db
from sqlalchemy import or_
from api import Sede, Setor, TipoMaterial, TipoObjeto, Movimentos

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Obter filtros
    filtro_setor = request.args.get('setor')
    filtro_movimento = request.args.get('movimento')
    filtro_data_inicio = request.args.get('data_inicio')
    filtro_data_fim = request.args.get('data_fim')

    # Dados gerais
    entradas = db.session.query(func.sum(Movimentos.quantidade)).filter(Movimentos.movimento == 'Entrada').scalar() or 0
    saidas = db.session.query(func.sum(Movimentos.quantidade)).filter(Movimentos.movimento == 'Saída').scalar() or 0
    total = entradas - abs(saidas)

    # Lista de setores
    setores = Setor.query.all()

    # Materiais por setor
    materiais_por_setor = db.session.query(
        Setor.nome,
        TipoMaterial.nome,
        func.sum(Movimentos.quantidade)
    ).join(
        Movimentos, Movimentos.setor_destinatario_id == Setor.id
    ).join(
        TipoMaterial, TipoMaterial.id == Movimentos.tipo_material_id
    ).group_by(
        Setor.nome, TipoMaterial.nome
    ).all()

    # Alerta de reposição
    LIMITE_MINIMO = 10  # Defina o limite mínimo
    materiais_necessarios_reposicao = db.session.query(
        Setor.nome.label('setor'),
        TipoMaterial.nome.label('tipo_material'),
        func.sum(Movimentos.quantidade).label('quantidade')
    ).join(
        Movimentos, Movimentos.setor_destinatario_id == Setor.id
    ).join(
        TipoMaterial, TipoMaterial.id == Movimentos.tipo_material_id
    ).group_by(
        Setor.nome, TipoMaterial.nome
    ).having(
        func.sum(Movimentos.quantidade) < LIMITE_MINIMO
    ).all()

    # Preparar dados para gráficos
    distribuicoes_labels = [f'{setor} - {material}' for setor, material, _ in materiais_por_setor]
    distribuicoes_values = [quantidade for _, _, quantidade in materiais_por_setor]

    movimentacoes_labels = ['Entrada', 'Saída']
    movimentacoes_values = [entradas, saidas]

    # Criando alias para as junções com Setor (remetente e destinatário)
    setor_remetente = aliased(Setor)
    setor_destinatario = aliased(Setor)

    # Aplicar filtros nas movimentações
    query = db.session.query(
        Movimentos.id,
        Movimentos.movimento,
        Movimentos.quantidade,
        Movimentos.data_movimento,
        setor_remetente.nome.label('setor_remetente'),
        TipoObjeto.nome.label('tipo_objeto'),
        setor_destinatario.nome.label('setor_destinatario')
    ).join(
        setor_remetente, setor_remetente.id == Movimentos.setor_remetente_id
    ).join(
        TipoObjeto, TipoObjeto.id == Movimentos.tipo_objeto_id
    ).join(
        setor_destinatario, setor_destinatario.id == Movimentos.setor_destinatario_id
    )

    # Filtros
    if filtro_setor:
        query = query.filter(Setor.nome == filtro_setor)
    if filtro_movimento:
        query = query.filter(Movimentos.movimento == filtro_movimento)
    if filtro_data_inicio:
        try:
            data_inicio = datetime.strptime(filtro_data_inicio, '%Y-%m-%d')
            query = query.filter(Movimentos.data_movimento >= data_inicio)
        except ValueError:
            pass
    if filtro_data_fim:
        try:
            data_fim = datetime.strptime(filtro_data_fim, '%Y-%m-%d')
            query = query.filter(Movimentos.data_movimento <= data_fim)
        except ValueError:
            pass

    movimentacoes = query.order_by(Movimentos.data_movimento.desc()).all()

    # Debug: Verificar se a consulta retorna dados
    print(f'Movimentações: {len(movimentacoes)}')

    # Passar os dados para o template
    return render_template(
        'dashboard.html',
        entradas=entradas,
        saidas=saidas,
        total=total,
        movimentacoes=movimentacoes,
        distribuicoes_labels=distribuicoes_labels,
        distribuicoes_values=distribuicoes_values,
        movimentacoes_labels=movimentacoes_labels,
        movimentacoes_values=movimentacoes_values,
        filtro_setor=filtro_setor,
        filtro_movimento=filtro_movimento,
        filtro_data_inicio=filtro_data_inicio,
        filtro_data_fim=filtro_data_fim,
        setores=setores,
        materiais_necessarios_reposicao=materiais_necessarios_reposicao
    )

@app.route('/tipos_de_materiais')
def tipos_de_materiais():
    tipos_de_materiais = TipoMaterial.query.all()
    return render_template('tipos_de_materiais.html', tipos_de_materiais=tipos_de_materiais)

@app.route('/objetos_por_tipo', methods=['GET', 'POST'])
def objetos_por_tipo():
    # Objetos por tipo de material, incluindo o ícone
    objetos_por_tipo = db.session.query(
        TipoMaterial.nome, 
        TipoObjeto.nome, 
        TipoObjeto.icone,  # Adicionando o ícone
        func.count(TipoObjeto.nome)
    ).join(
        TipoObjeto, TipoObjeto.tipo_material_id == TipoMaterial.id
    ).group_by(
        TipoMaterial.nome, TipoObjeto.nome, TipoObjeto.icone  # Agrupando também por ícone
    ).all()

    # Criando um dicionário para organizar os objetos por tipo de material
    objetos_por_tipo_dict = {}
    for tipo_material_nome, tipo_objeto_nome, icone, quantidade in objetos_por_tipo:
        objetos_por_tipo_dict.setdefault(tipo_material_nome, []).append({
            'tipo_objeto': tipo_objeto_nome,
            'icone': icone,  # Incluindo o ícone
            'quantidade': quantidade
        })

    # Passando o dicionário com ícones para o template
    return render_template('objetos_por_tipo.html', objetos_por_tipo_dict=objetos_por_tipo_dict)

@app.route('/materiais_por_setor', methods=['GET', 'POST'])
def materiais_por_setor():
    # Obter filtros da URL
    filtro_setor = request.args.get('setor')
    filtro_data_inicio = request.args.get('data_inicio')
    filtro_data_fim = request.args.get('data_fim')

    # Consultar as quantidades de entrada, saída e quantidade atual por setor, material e objeto
    materiais_por_setor = db.session.query(
        Setor.nome.label('setor_nome'),
        TipoMaterial.nome.label('tipo_material_nome'),
        TipoObjeto.nome.label('tipo_objeto_nome'),
        func.sum(case(
            (Movimentos.movimento == 'Entrada', Movimentos.quantidade),
            else_=0
        )).label('entrada'),
        func.sum(case(
            (Movimentos.movimento == 'Saída', Movimentos.quantidade),
            else_=0
        )).label('saida'),
        (func.sum(case(
            (Movimentos.movimento == 'Entrada', Movimentos.quantidade),
            else_=0
        )) - func.sum(case(
            (Movimentos.movimento == 'Saída', Movimentos.quantidade),
            else_=0
        ))).label('quantidade_atual'),
        func.date(Movimentos.data_movimento).label('data_movimento')
    ).join(
        Setor, or_(
            Setor.id == Movimentos.setor_remetente_id,
            Setor.id == Movimentos.setor_destinatario_id
        )
    ).join(
        TipoMaterial, TipoMaterial.id == Movimentos.tipo_material_id
    ).join(
        TipoObjeto, TipoObjeto.id == Movimentos.tipo_objeto_id
    )

    # Aplicar filtros nos dados
    if filtro_setor:
        materiais_por_setor = materiais_por_setor.filter(Setor.nome == filtro_setor)
    if filtro_data_inicio:
        try:
            data_inicio = datetime.strptime(filtro_data_inicio, '%Y-%m-%d')
            materiais_por_setor = materiais_por_setor.filter(Movimentos.data_movimento >= data_inicio)
        except ValueError:
            pass
    if filtro_data_fim:
        try:
            data_fim = datetime.strptime(filtro_data_fim, '%Y-%m-%d')
            materiais_por_setor = materiais_por_setor.filter(Movimentos.data_movimento <= data_fim)
        except ValueError:
            pass

    # Agrupar os resultados por setor, material, objeto e data
    materiais_por_setor = materiais_por_setor.group_by(
        Setor.nome, TipoMaterial.nome, TipoObjeto.nome, func.date(Movimentos.data_movimento)
    ).all()

    # Processar os dados para o dicionário dos setores
    materiais_por_setor_dict = {}
    for setor_nome, tipo_material_nome, tipo_objeto_nome, entrada, saida, quantidade_atual, data_movimento in materiais_por_setor:
        if setor_nome not in materiais_por_setor_dict:
            materiais_por_setor_dict[setor_nome] = []
        materiais_por_setor_dict[setor_nome].append({
            'tipo_material': tipo_material_nome,
            'tipo_objeto': tipo_objeto_nome,
            'entrada': entrada,
            'saida': saida,
            'quantidade_atual': quantidade_atual,
            'data_movimento': data_movimento
        })

    # Consultar análise por dia, semana e mês
    analise_por_dia = db.session.query(
        func.date(Movimentos.data_movimento).label('data'),
        func.count(Movimentos.id).label('total')
    ).group_by(
        func.date(Movimentos.data_movimento)
    ).order_by(
        func.date(Movimentos.data_movimento)
    ).all()

    analise_por_semana = db.session.query(
        func.week(Movimentos.data_movimento).label('semana'),
        func.count(Movimentos.id).label('total')
    ).group_by(
        func.week(Movimentos.data_movimento)
    ).order_by(
        func.week(Movimentos.data_movimento)
    ).all()

    analise_por_mes = db.session.query(
        func.date_format(Movimentos.data_movimento, '%Y-%m').label('mes'),
        func.count(Movimentos.id).label('total')
    ).group_by(
        func.date_format(Movimentos.data_movimento, '%Y-%m')
    ).order_by(
        func.date_format(Movimentos.data_movimento, '%Y-%m')
    ).all()

    # Converter os resultados para dicionários (se forem None, retornará uma lista vazia)
    analise_por_dia_dict = [{'data': row.data, 'total': row.total} for row in analise_por_dia] if analise_por_dia else []
    analise_por_semana_dict = [{'semana': row.semana, 'total': row.total} for row in analise_por_semana] if analise_por_semana else []
    analise_por_mes_dict = [{'mes': row.mes, 'total': row.total} for row in analise_por_mes] if analise_por_mes else []

    # Passar os dados para o template
    return render_template(
        'materiais_por_setor.html',
        setores=Setor.query.all(),
        materiais_por_setor_dict=materiais_por_setor_dict,
        filtro_setor=filtro_setor,
        filtro_data_inicio=filtro_data_inicio,
        filtro_data_fim=filtro_data_fim,
        analise_por_dia=analise_por_dia_dict,
        analise_por_semana=analise_por_semana_dict,
        analise_por_mes=analise_por_mes_dict
    )

@app.route('/setores_por_sede', methods=['GET', 'POST'])
def setores_por_sede():
    # Consulta para obter setores por sede
    setores_por_sede = db.session.query(Sede.nome, Setor.nome).\
        join(Setor, Setor.sede_id == Sede.id).all()
    
    # Construindo o dicionário
    setores_por_sede_dict = {}
    for sede_nome, setor_nome in setores_por_sede:
        setores_por_sede_dict.setdefault(sede_nome, []).append(setor_nome)
    
    # Passando o contexto correto
    return render_template('setores_por_sede.html', setores_por_sede_dict=setores_por_sede_dict)
