from dao.Conexao import Connection
from model.Cliente_model import ClienteModel

class ClienteDao(Connection):
    def insert(self, cliente : ClienteModel):
        self.cursor.execute(f"INSERT INTO Cliente(nome,email,senha) VALUES ('{cliente.nome}','{cliente.email}','{cliente.senha}')")
        self.connection.commit()
        return "Inserido com sucesso"

    def delete(self, id):
        try:
            self.cursor.execute(f"DELETE FROM Cliente WHERE id={id}")
            self.connection.commit()
        except:
            return "Id inexistente"
        else:
            return "Deleteado com sucesso"

    def select_all(self):
        self.cursor.execute("SELECT * FROM Cliente")
        lista = self.cursor.fetchall()
        ret = []
        for i in lista:
            cm = ClienteModel(i[1],i[2],i[3],i[0])
            ret.append(cm.__dict__)

        return ret

    def select_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM Cliente WHERE id={id}")
        cl = self.cursor.fetchone()
        cm = ClienteModel(cl[1],cl[2],cl[3],cl[0])
        return cm.__dict__

    def update(self, cliente : ClienteModel):
        try:
            self.cursor.execute(f"UPDATE Cliente set nome='{cliente.nome}',email='{cliente.email}',senha='{cliente.senha}' WHERE id={cliente.id}")
            self.connection.commit()
        except:
            return "Id inexistente"
        else:
            return "Alterado com sucesso"
