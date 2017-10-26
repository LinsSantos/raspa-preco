import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Table, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


path = os.path.dirname(os.path.abspath(__file__))
engine = create_engine('sqlite:////' + path + '/raspa.db')
Base = declarative_base()

if __name__ == '__main__':
    Base.metadata.create_all(engine)


produto_procedimento = Table('association', Base.metadata,
                             Column('left_id', Integer,
                                    ForeignKey('procedimentos.id')),
                             Column('right_id', Integer,
                                    ForeignKey('produtos.id'))
                             )


class Procedimento(Base):
    """Guarda os dados do procedimento"""
    __tablename__ = 'procedimentos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20), unique=True)
    produtos = relationship(
        "Produto",
        secondary=produto_procedimento,
        back_populates="procedimentos")

    def __init__(self, nome):
        self.nome = nome


class Produto(Base):
    """Um produto a pesquisar"""
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), unique=True)
    procedimentos = relationship(
        "Procedimento",
        secondary=produto_procedimento,
        back_populates="produtos")

    def __init__(self, descricao):
        self.descricao = descricao


class Site(Base):
    """Um site que será fonte de dados"""
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    title = Column(String(20), unique=True)
    url = Column(String(200))

    def __init__(self, title, url):
        self.title = title
        self.url = url