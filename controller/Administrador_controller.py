from model.Administrador_model import AdministradorModel
from controller.Base_controller import BaseController

class AdministradorController(BaseController):
    def __init__(self):
        super().__init__(AdministradorModel)

    def post(self):
        return super().post(AdministradorModel(**super().getDados()))

    def put(self, id):
        dic = super().getDados()
        dic['id'] = id
        super().put(AdministradorModel(**dic))
