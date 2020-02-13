from sqlalchemy import Column,Integer,String,Float, ForeignKey

from model.Base import Base

class Distribuidor(Base):
    __tablename__ = "Distribuidor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))

    def __str__(self, nome, id=None):
        self.id = id
        self.nome = nome

    def serialize(self):
        return {
            "id" : self.id,
            "nome" : self.nome
        }