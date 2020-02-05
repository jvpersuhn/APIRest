from dao.Base_dao import BaseDao
from model.Produto_model import ProdutoModel

class ProdutoDao(BaseDao):

    def delete(self, id):
        return super().delete(id, ProdutoModel)

    def insert(self, produto : ProdutoModel):
        return super().insert(produto)

    def update(self, produto : ProdutoModel):
        user = self.session.query(ProdutoModel).filter_by(id=produto.id).first()
        user.nome = produto.nome
        user.preco = produto.preco
        self.session.commit()
        return "Alterado com sucesso"

    def select_all(self):
        users = self.session.query(ProdutoModel).all()
        ret = []
        for i in users:
            ret.append(i.serialize())

        return ret

    def select_by_id(self, id):
        user = self.session.query(ProdutoModel).filter_by(id=id).first()
        return user.serialize()

