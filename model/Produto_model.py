from sqlalchemy import Column,Integer,String,Float, ForeignKey
from sqlalchemy.orm import relationship

from model.Base import Base
from model.Distribuidor import Distribuidor

class ProdutoModel(Base):

    __tablename__ = "Produto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    preco = Column(Float)
    id_distribuidor = Column(Integer, ForeignKey('Distribuidor.id'))
    distribuidor = relationship(Distribuidor)

    def __init__(self,nome,preco,id=None):
        self.id = id
        self.nome = nome
        self.preco = preco

    def serialize(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "preco" : self.preco
        }