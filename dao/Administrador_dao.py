from dao.Conexao import Connection
from model.Administrador_model import AdministradorModel

class AdministradorDao(Connection):

    def insert(self, adm : AdministradorModel):
        self.session.add(adm)
        self.session.commit()

    def update(self, adm : AdministradorModel):
        user = self.session.query(AdministradorModel).filter_by(id=adm.id).first()
        user.nome = adm.nome
        user.usuario = adm.usuario
        user.email = adm.email
        user.senha = adm.senha
        self.session.commit()

    def select_all(self):
        user = self.session.query(AdministradorModel).all()
        ret = []
        for i in user:
            ret.append(i.serialize())

        return ret

    def select_by_id(self, id):
        user = self.session.query(AdministradorModel).first()
        return user.serialize()

    def delete(self,id):
        user = self.session.query(AdministradorModel).filter_by(id=id).first()
        self.session.delete(user)
        self.session.commit()
