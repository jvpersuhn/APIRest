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
            ret.append(i.__dict__())

        return ret

    def select_by_id(self, id):
        user = self.session.query(AdministradorModel).first()
        return user.__dict__

    def delete(self,id):
        self.cursor.execute(f"DELETE FROM Administrador where id={id}")
        self.connection.commit()
