from model.Produto_model import ProdutoModel
from controller.Base_controller import BaseController

class ProdutoController(BaseController):

    def __init__(self):
        super().__init__(ProdutoModel)

    def post(self):
        return super().post(ProdutoModel(**super().getDados()))

    def put(self, id):
        dic = super().getDados()
        dic['id'] = id
        return super().put(ProdutoModel(**dic))


