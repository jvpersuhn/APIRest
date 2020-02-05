from dao.Base_dao import BaseDao
from model.Cliente_model import ClienteModel

class ClienteDao(BaseDao):

    def delete(self, id):
        return super().delete(id, ClienteModel)

    def insert(self, cliente : ClienteModel):
        return super().insert(cliente)

    def select_all(self):
        users = self.session.query(ClienteModel).all()
        ret = []
        for i in users:
            ret.append(i.serialize())

        return ret

    def select_by_id(self, id):
        user = self.session.query(ClienteModel).filter_by(id=id).first()
        return user.serialize()

    def update(self, cliente : ClienteModel):
        user = self.session.query(ClienteModel).filter_by(id=cliente.id).first()
        user.nome = cliente.nome
        user.usuario = cliente.usuario
        user.email = cliente.email
        user.senha = cliente.senha
        self.session.commit()
        return "Alterado com sucesso"
