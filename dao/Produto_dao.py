from dao.Conexao import Connection
from model.Produto_model import ProdutoModel

class ProdutoDao(Connection):
    def insert(self, produto : ProdutoModel):
        self.session.add(produto)
        self.session.commit()
        return "Inserido com sucesso"

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

    def delete(self, id):
        try:
            user = self.session.query(ProdutoModel).filter_by(id=id).first()
            self.delete(user)
            self.session.commit()
        except:
            return "Erro"
        else:
            return "Deu certo"
