from sqlalchemy.orm import sessionmaker
from DBClasses import Endereco, Telefone, Pessoa, engine, Base

##from DBClasses_sqlite import Endereco, Base, Telefone, Pessoa, engine

##gerenciar quando entramos e saímos de uma sessão o que permite o controle de acesso ao banco e rollback quando necessário
DBSession = sessionmaker(bind=engine)

##def insertPessoa(nome_, cep_):
##session = DBSession()
##P = Pessoa(nome_, cep_)
##session.add(p)
##session.commit();
##session.close();
session = DBSession()


def insert(obj):
    ##inicia sessao

    session.add(obj)
    session.commit()

    ##encerra sessao


def getPessoas():
    session = DBSession()
    pessoas = session.query(Pessoa).all()
    return pessoas


def getTelefones():
    session = DBSession()
    telefones = session.query(Telefone).all()
    for t in telefones:
        print("Numero: " + t.numero)
    return telefones


def getEnderecos():
    session = DBSession()
    enderecos = session.query(Endereco).all()
    for e in enderecos:
        print("Rua: " + e.rua + " Numero: " + e.numero + " CEP: " + e.cep)
    return enderecos


def delete(nome):
    session = DBSession()
    p = session.query(Pessoa).filter_by(nome=nome).first()
    if None == p:
        return False

    elif None != p:
        session.delete(p)

    session.commit()
    session.close()
    return True
