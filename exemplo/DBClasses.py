import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

##para não termos que lidar com Tabelas e mapeamentos
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key = True,autoincrement=True)
    nome = Column(String(250), nullable = False)
    email = Column(String(30), nullable = False)
    enderecos = relationship('Endereco',backref ='pessoa')
    telefones = relationship('Telefone',backref='pessoa')

class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True,autoincrement=True)
    rua = Column(String(250), nullable=False)
    numero = Column(String(250), nullable=False)
    cep = Column(String(250), nullable=False)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    ##pessoa = relationship(Pessoa)

class Telefone(Base):
    __tablename__ = 'telefone'
    id = Column(Integer, primary_key=True,autoincrement=True)
    numero = Column(String(250), nullable=False)
    tipo = Column(String(250), nullable=True)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    ##pessoa = relationship(Pessoa)

engine = create_engine('sqlite:///sqlalchemy_example.db')
##Cria a base de dados no banco. Caso a base de dados já exista, adiciona o que não existe. Se há modificações, ocorre uma exceção
#for tbl in reversed(Base.metadata.sorted_tables):
 #   engine.execute(tbl.delete())
Base.metadata.create_all(engine)

##para apagar todas as tabelas do banco
