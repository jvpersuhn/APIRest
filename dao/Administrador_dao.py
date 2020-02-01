from dao.Conexao import Connection
from model.Administrador_model import AdministradorModel

class AdministradorDao(Connection):
    def insert(self, adm : AdministradorModel):
        self.cursor.execute(f"INSERT INTO Administrador(usuario,email,senha) values ('{adm.user}','{adm.email}','{adm.password}')")
        self.connection.commit()

    def update(self, adm : AdministradorModel):
        self.cursor.execute(f"UPDATE Administrador set usuario='{adm.user}',email='{adm.email}',senha='{adm.password}' where id={adm.id}")
        self.connection.commit()

    def select_all(self):
        self.cursor.execute("SELECT * FROM Administrador")
        lista = self.cursor.fetchall()
        ret = []
        for i in lista:
            adm = AdministradorModel(i[1],i[2],i[3],i[0])
            ret.append(adm.__dict__())

        return ret

    def select_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM Administrador WHERE id={id}")
        adm = self.cursor.fetchone()
        a = AdministradorModel(adm[1],adm[2],adm[3],adm[0])
        return a.__dict__()

    def delete(self,id):
        self.cursor.execute(f"DELETE FROM Administrador where id={id}")
        self.connection.commit()
