
class ClienteModel:
    def __init__(self,nome,email,senha,id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha