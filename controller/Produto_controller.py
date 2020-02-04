from flask_restful import Resource
from flask import json,request

from dao.Produto_dao import ProdutoDao, ProdutoModel

class ProdutoController(Resource):

    def __init__(self):
        self.produtoDao = ProdutoDao()

    def get(self,id=None):
        if id:
            return self.produtoDao.select_by_id(id)
        return self.produtoDao.select_all()

    def post(self):
        nome = request.json['nome']
        preco = request.json['preco']
        p = ProdutoModel(nome,preco)
        return self.produtoDao.insert(p)

    def put(self, id):
        idR = request.json['id']
        nome = request.json['nome']
        preco = request.json['preco']

        if id != idR:
            return "Ids nao combinam"

        p = ProdutoModel(nome,preco,id)

        return self.produtoDao.update(p)

    def delete(self, id):
        return self.produtoDao.delete(id)
