from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

class AdministradorModel:

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    usuario = Column(String(100), unique=True)
    email = Column(String(200), unique=True)
    senha = Column(String(100))

    def __init__(self, nome,usuario,email,senha,id=None):
        self.id = id
        self.nome = nome
        self.usuario = usuario
        self.email = email
        self.senha = senha
