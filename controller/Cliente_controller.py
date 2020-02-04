from flask_restful import Resource
from flask import request,json

from dao.Cliente_dao import ClienteDao,ClienteModel

class ClienteController(Resource):
    def __init__(self):
        self.dao = ClienteDao()

    def get(self,id=None):
        if id:
            return self.dao.select_by_id(id)
        return self.dao.select_all()

    def delete(self,id):
        return self.dao.delete(id)

    def post(self):
        nome = request.json['nome']
        usuario = request.json['usuario']
        email = request.json['email']
        senha = request.json['senha']
        cliente = ClienteModel(nome,usuario,email,senha)
        return self.dao.insert(cliente)

    def put(self,id):
        nome = request.json['nome']
        usuario = request.json['usuario']
        email = request.json['email']
        senha = request.json['senha']
        idR = request.json['id']

        if idR != id:
            return "Ids diferentes"

        cliente = ClienteModel(nome,usuario,email,senha,id)

        return self.dao.update(cliente)
