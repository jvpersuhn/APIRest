from dao.Base_dao import BaseDao
from model.Produto_model import ProdutoModel

class ProdutoDao(BaseDao):

    def __init__(self, model):
        super().__init__(model)


