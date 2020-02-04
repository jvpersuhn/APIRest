from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float

Base = declarative_base()

class ProdutoModel(Base):

    __tablename__ = "Produto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    preco = Column(Float)

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