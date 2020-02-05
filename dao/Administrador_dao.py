from dao.Base_dao import BaseDao
from model.Administrador_model import AdministradorModel

class AdministradorDao(BaseDao):

    def delete(self,id):
        super().delete(id, AdministradorModel)

    def insert(self, adm : AdministradorModel):
        return super().insert(adm)

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


