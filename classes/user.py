class User:
    id = None
    login = None
    password = None
    name = None
    surname = None

    def __init__(self, id, login, password, name, surname):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname