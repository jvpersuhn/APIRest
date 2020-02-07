from dao.Base_dao import BaseDao
from model.Cliente_model import ClienteModel

class ClienteDao(BaseDao):

    def __init__(self, model):
        super().__init__(model)