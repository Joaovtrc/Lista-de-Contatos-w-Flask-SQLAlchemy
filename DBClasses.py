import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

db = declarative_base()

class Contato(db):
    __tablename__ = 'contatos'
    id = Column(Integer, primary_key = True,autoincrement=True)
    nome = Column(String(250), nullable = False)
    email = Column(String(30), nullable = False)
    enderecos = relationship('Endereco',backref ='contatos', lazy='subquery')
    telefones = relationship('Telefone',backref='contatos', lazy='subquery')

class Endereco(db):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True,autoincrement=True)
    endereco = Column(String(250), nullable=False)
    numero = Column(String(250), nullable=False)
    cep = Column(String(250), nullable=False)
    contato_id = Column(Integer, ForeignKey('contatos.id'))

class Telefone(db):
    __tablename__ = 'telefones'
    id = Column(Integer, primary_key=True,autoincrement=True)
    telefone = Column(String(250), nullable=False)
    tipo = Column(String(250), nullable=True)
    contato_id = Column(Integer, ForeignKey('contatos.id'))

engine = create_engine('sqlite:///sqlalchemy_example.db')


db.metadata.create_all(engine)