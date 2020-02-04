from dao.Conexao import Connection
from model.Produto_model import ProdutoModel

class ProdutoDao(Connection):
    def insert(self, produto : ProdutoModel):
        self.session.add(produto)
        self.session.commit()


