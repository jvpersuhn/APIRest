from dao.Conexao import Connection

class BaseDao(Connection):
    def delete(self, id, model):
        try:
            user = self.session.query(model).filter_by(id=id).first()
            self.session.delete(user)
            self.session.commit()
        except:
            return "Erro"
        else:
            return "Deu certo"

    def insert(self, model):
        try:
            self.session.add(model)
            self.session.commit()
        except:
            return "Erro ao inserir dado"
        else:
            return "Inserido com sucesso"

