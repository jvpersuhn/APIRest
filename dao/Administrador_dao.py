from dao.Base_dao import BaseDao
from model.Administrador_model import AdministradorModel

class AdministradorDao(BaseDao):

    def delete(self,id):
        super().delete(id, AdministradorModel)

    def insert(self, adm : AdministradorModel):
        return super().insert(adm)

    def update(self, adm):
        super().update(adm)

    def select_all(self):
        return super().select_all(AdministradorModel)

    def select_by_id(self, id):
        super().select_by_id(AdministradorModel, id)

