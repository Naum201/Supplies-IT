from flask import Flask, render_template, Request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/gestão_de_estoque_ti'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos
class Sede(db.Model):
    __tablename__ = 'sede'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)

    # Outros campos e relacionamentos
    tipo = db.Column(db.Enum('Matriz', 'Filial'))

class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sede_id = db.Column(db.Integer, db.ForeignKey('sede.id'))
    sede = db.relationship('Sede', backref='setores')

class TipoMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    icone = db.Column(db.String(100), nullable=False)  # Adiciona a coluna 'icone'

class TipoObjeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    tipo_material_id = db.Column(db.Integer, db.ForeignKey('tipo_material.id'))
    tipo_material = db.relationship('TipoMaterial', backref='objetos')
    icone = db.Column(db.String(100), nullable=False)  # Novo campo para o ícone

class Movimentos(db.Model):
    __tablename__ = 'movimentos'
    id = db.Column(db.Integer, primary_key=True)
    notafiscal = db.Column(db.String(255), nullable=True)  # Campo adicionado
    quantidade = db.Column(db.Integer, nullable=False)
    movimento = db.Column(db.String(10), nullable=False)  # 'Entrada' ou 'Saída'
    tipo_material_id = db.Column(db.Integer, db.ForeignKey('tipo_material.id'), nullable=False)
    tipo_objeto_id = db.Column(db.Integer, db.ForeignKey('tipo_objeto.id'), nullable=False)
    setor_remetente_id = db.Column(db.Integer, db.ForeignKey('setor.id'), nullable=True)
    setor_destinatario_id = db.Column(db.Integer, db.ForeignKey('setor.id'), nullable=True)
    sede_id = db.Column(db.Integer, db.ForeignKey('sede.id'), nullable=False)  # Adiciona a chave estrangeira
    data_movimento = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relacionamentos
    sede = db.relationship('Sede', backref='movimentos')  # Relacionamento com a tabela Sede
    tipo_material = db.relationship('TipoMaterial', backref='movimentos')
    setor_remetente = db.relationship('Setor', foreign_keys=[setor_remetente_id])
    setor_destinatario = db.relationship('Setor', foreign_keys=[setor_destinatario_id])
    tipo_objeto = db.relationship('TipoObjeto', foreign_keys=[tipo_objeto_id])

    def __repr__(self):
        return f'<Movimento {self.id}>'

with app.app_context():
    db.create_all()

from controllers.controle_suprimento import *
#from controllers.glpi import *
from controllers.analises import *

if __name__ == '__main__':
    app.run(debug=True)