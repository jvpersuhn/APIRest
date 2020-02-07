from model.Cliente_model import ClienteModel
from controller.Base_controller import BaseController

class ClienteController(BaseController):
    def __init__(self):
        super().__init__(ClienteModel)

    def post(self):
        return super().post(ClienteModel(**super().getDados()))

    def put(self,id):
        dic = super().getDados()
        dic['id'] = id
        return super().put(ClienteModel(**dic))

