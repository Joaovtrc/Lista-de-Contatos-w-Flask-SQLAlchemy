from sqlalchemy.orm import sessionmaker
from DBClasses import Endereco, Telefone, Contato, engine, db

DBSession = sessionmaker(bind=engine)



def insertEdit(obj):
    session = DBSession()
    session.add(obj)
    session.commit()
    session.close()

def getContatos():
    session = DBSession()
    contatos = session.query(Contato).all()
    session.close()
    return contatos


def deletarContato(id):
    session = DBSession()
    c = session.query(Contato).filter_by(id=id).first()
    session.delete(c)
    session.commit()
    session.close()

def deletarTelefone(id):
    session = DBSession()
    t = session.query(Telefone).filter_by(id=id).first()
    session.delete(t)
    session.commit()
    session.close()

def deletarEndereco(id):
    session = DBSession()
    e = session.query(Endereco).filter_by(id=id).first()
    session.delete(e)
    session.commit()
    session.close()

def getSingleContato(id):
    session = DBSession()
    c = session.query(Contato).filter_by(id=id).first()
    session.close()
    return c