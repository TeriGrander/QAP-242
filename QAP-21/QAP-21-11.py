class User:
    PASSWORD_MIN_LEN = 5
    PASSWORD_MAX_LEN = 16

    def __init__(self, login, password, name, email, role):
        self.__validate_password(password)
        self.__login = login
        self.__password = password
        self.name = name
        self.email = email
        self.role = role

    @classmethod
    def __validate_password(cls, password):
        if not (cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN and type(password) == str):
            raise AttributeError('Password not valid')

    def get_login(self):
        return self.__login

    def set_login(self, new_login):
        self.__login = new_login

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__validate_password(new_password)
        self.__password = new_password

    login = property(get_login, set_login)
    password = property(get_password, set_password)

u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')

# В момент переопределения значения вызывается метод set_password
u1.password = 'Krop88'
# В момент получения доступа к значению вызывается метод get_password
print(u1.password)
# Krop88

u1.password = '123'
# AttributeError: Password not valid
print(u1.password)