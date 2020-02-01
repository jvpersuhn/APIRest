class AdministradorModel:
    def __init__(self, user, email, password, id=None):
        self.id = id
        self.user = user
        self.email = email
        self.password = password

    def __dict__(self):
        return {
            "id" : self.id,
            "user" : self.user,
            "email" : self.email,
            "password" : self.password
        }