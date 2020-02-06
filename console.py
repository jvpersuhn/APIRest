from dao.Administrador_dao import AdministradorModel, AdministradorDao

dao = AdministradorDao()
adm = AdministradorModel("aaa","aaaa","aaa","a",1)

dao.update(adm)