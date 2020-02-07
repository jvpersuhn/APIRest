from dao.Base_dao import BaseDao
from model.Administrador_model import AdministradorModel

class AdministradorDao(BaseDao):

    def __init__(self, model):
        super().__init__(model)
