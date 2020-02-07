from dao.Conexao import Connection

class BaseDao(Connection):

    def __init__(self, model):
        super().__init__()
        self.model = model

    def delete(self, id):
        try:
            user = self.session.query(self.model).filter_by(id=id).first()
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

    def select_all(self):
        user = self.session.query(self.model).all()
        ret = []
        for i in user:
            ret.append(i.serialize())

        return ret

    def select_by_id(self, id):
        user = self.session.query(self.model).filter_by(id=id).first()
        return user.serialize()

    def update(self, novo):
        try:
            self.session.merge(novo)
            self.session.commit()
        except:
            return "Erro"
        else:
            return "Alterado"

