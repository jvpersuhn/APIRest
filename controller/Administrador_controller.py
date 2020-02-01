from flask_restful import Resource
from flask import request,json

from dao.Administrador_dao import AdministradorModel, AdministradorDao

class AdministradorController(Resource):
    def __init__(self):
        self.admDao = AdministradorDao()

    def get(self,id=None):
        if id:
            return self.admDao.select_by_id(id)
        return self.admDao.select_all()

    def post(self):
        usuario = request.json['usuario']
        email = request.json['email']
        senha = request.json['senha']
        adm = AdministradorModel(usuario,email,senha)
        self.admDao.insert(adm)

        return "Cadastrado com sucesso"

    def delete(self,id):
        try:
            self.admDao.delete(id)
        except:
            return "Id não existe"
        else:
            return "Deletado com sucesso"

    def put(self,id):
        usuario = request.json['usuario']
        email = request.json['email']
        senha = request.json['senha']
        adm = AdministradorModel(usuario,email,senha,id)
        self.admDao.update(adm)
        return "Alterado"