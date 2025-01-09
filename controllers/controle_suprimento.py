from flask import render_template, request, redirect, url_for, flash
from api import app, db
from api import Sede, Setor, TipoMaterial, TipoObjeto, Movimentos

# Rota para Cadastro de Sede
@app.route('/', methods=['GET', 'POST'])
def cadastro_sede():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        if nome and tipo:
            sede = Sede(nome=nome, tipo=tipo)
            db.session.add(sede)
            db.session.commit()
            flash('Sede adicionada com sucesso!', 'success')
        return redirect(url_for('cadastro_sede'))
    return render_template('cadastro_sede.html')


@app.route('/cadastro_setor', methods=['GET', 'POST'])
def cadastro_setor():
    """
    Verifica se há sedes cadastradas e, caso não haja, adiciona sedes padrão e os setores associados.
    """
    # Obtém a lista de sedes para exibir no formulário
    sedes = Sede.query.all()

    if request.method == 'POST':
        nome = request.form['nome']
        sede_id = request.form['sede']
        
        if nome and sede_id:
            # Verifica se a sede já tem setores cadastrados
            sede = Sede.query.get(sede_id)
            setores_existentes = Setor.query.filter_by(sede_id=sede_id).count()  # Conta os setores
            
            # Se não houver setores cadastrados para essa sede
            if setores_existentes == 0:
                # Se não houver setores cadastrados, cria os setores padrão
                setores_padrao = [
                    "Administração", "Compras", "Dept. Pessoal", "Embalagem", "Estoque S4",
                    "Estoque Automação", "Estoque Anexo", "Estoque CD", "Fiscal", "Financeiro",
                    "Logística", "Marketing", "Mezanino", "RH", "Recebimento", "Salão", "Vendas",
                    "SGI", "Segurança do Trabalho", "Televendas", "TI"
                ]
                
                for setor_nome in setores_padrao:
                    setor = Setor(nome=setor_nome, sede_id=sede_id)
                    db.session.add(setor)
                db.session.commit()
                print(f"Setores padrão adicionados para a sede {sede.nome}")  # Log para depuração

            # Agora, adiciona o setor que foi enviado pelo formulário
            setor = Setor(nome=nome, sede_id=sede_id)
            db.session.add(setor)
            db.session.commit()
            flash('Setor adicionado com sucesso!', 'success')

        return redirect(url_for('cadastro_setor'))
    
    return render_template('cadastro_setor.html', sedes=sedes)


@app.route('/cadastro_material', methods=['GET', 'POST'])
def cadastro_material():
    if request.method == 'POST':
        nome = request.form['nome']
        icone = request.form['icone']  # Obter o ícone do formulário
        if nome and icone:
            material = TipoMaterial(nome=nome, icone=icone)  # Salvar o nome e o ícone
            db.session.add(material)
            db.session.commit()
            flash('Tipo de material adicionado com sucesso!', 'success')
        return redirect(url_for('cadastro_material'))
    return render_template('cadastro_material.html')


@app.route('/cadastro_objeto', methods=['GET', 'POST'])
def cadastro_objeto():
    materiais = TipoMaterial.query.all()
    if request.method == 'POST':
        nome = request.form['nome']
        tipo_material_id = request.form['tipo_material']
        icone = request.form['icone']  # Obtém o ícone do formulário
        if nome and tipo_material_id and icone:
            objeto = TipoObjeto(nome=nome, tipo_material_id=tipo_material_id, icone=icone)
            db.session.add(objeto)
            db.session.commit()
            flash('Objeto adicionado com sucesso!', 'success')
        return redirect(url_for('cadastro_objeto'))
    return render_template('cadastro_objeto.html', materiais=materiais)


@app.route('/entrada_saida', methods=['GET', 'POST'])
def entrada_saida():
    # Buscar dados do banco
    sedes = Sede.query.all()
    setores = Setor.query.all()
    materiais = TipoMaterial.query.all()
    objetos = TipoObjeto.query.all()

    if request.method == 'POST':
        # Usar .get() para evitar KeyError
        sede_id = request.form.get('sede')
        setor_remetente_id = request.form.get('setor_remetente')
        setor_destinatario_id = request.form.get('setor_destinatario')

        # Verificar se setor_destinatario foi marcado como 'Nulo' e ajustar
        if setor_destinatario_id == 'Nulo':
            setor_destinatario_id = None  # Substituir 'Nulo' por None

        # Obter outros dados do formulário
        nota_fiscal = request.form.get('nota')
        tipo_material_id = request.form.get('tipo_material')
        tipo_objeto_id = request.form.get('tipo_objeto')
        quantidade = request.form.get('quantidade')
        movimento = request.form.get('movimento')  # 'Entrada' ou 'Saída'

        # Criar o objeto de movimento
        if sede_id and tipo_material_id and tipo_objeto_id and quantidade and movimento:
            novo_movimento = Movimentos(
                sede_id=sede_id,
                setor_remetente_id=setor_remetente_id,
                setor_destinatario_id=setor_destinatario_id,
                notafiscal=nota_fiscal,
                tipo_material_id=tipo_material_id,
                tipo_objeto_id=tipo_objeto_id,
                quantidade=int(quantidade),
                movimento=movimento
            )
            db.session.add(novo_movimento)
            db.session.commit()
            flash('Movimento registrado com sucesso!', 'success')
        else:
            flash('Erro: Todos os campos obrigatórios devem ser preenchidos.', 'danger')

        return redirect(url_for('entrada_saida'))

    return render_template(
        'entrada_saida.html',
        sedes=sedes,
        setores=setores,
        materiais=materiais,
        objetos=objetos
    )
