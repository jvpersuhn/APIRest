from dao.Conexao import Connection
from model.Cliente_model import ClienteModel

class ClienteDao(Connection):
    def insert(self, cliente : ClienteModel):
        self.session.add(cliente)
        self.session.commit()
        return "Cadastrado"

    def delete(self, id):
        try:
            user = self.session.query(ClienteModel).filter_by(id=id).first()
            self.delete(user)
            self.session.commit()
        except:
            return "Erro"
        else:
            return "Deleteado com sucesso"

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
        return "Deletado com sucesso"
