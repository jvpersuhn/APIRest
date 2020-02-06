from dao.Base_dao import BaseDao
from model.Cliente_model import ClienteModel

class ClienteDao(BaseDao):

    def delete(self, id):
        return super().delete(id, ClienteModel)

    def insert(self, cliente : ClienteModel):
        return super().insert(cliente)

    def select_all(self):
        return super().select_all(ClienteModel)

    def select_by_id(self, id):
        return super().select_by_id(ClienteModel, id)

    def update(self, cliente : ClienteModel):
        return super().update(cliente)
