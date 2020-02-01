from dao.Administrador_dao import AdministradorModel, AdministradorDao

dao = AdministradorDao()
#adm = AdministradorModel("Teste2","Teste2","Teste2",2)

for i in dao.select_all():
    print(i)