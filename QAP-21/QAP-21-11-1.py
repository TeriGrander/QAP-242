class Model:
    MIN_NAME_LENGTH = 3
    MAX_NAME_LENGTH = 15

    def __init__(self):
        self.__name = None
    
    @classmethod
    def validate_name(cls, name):
        if cls.MIN_NAME_LENGTH <= len(name) <= cls.MAX_NAME_LENGTH: return True
        else: return False

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if self.validate_name(name): self.__name = name


# Создаем экземпляр класса Model
m = Model()

# Проверяем начальное значение имени модели (должно быть None)
print(m.name) 
# Выведет: None

# Пытаемся установить значение имени, которое не соответствует условиям
m.name = "AB"
print(m.name) 
# Выведет: None

# Пытаемся установить значение имени, которое не соответствует условиям
m.name = "A" * 16
print(m.name) 
# Выведет: None

# Устанавливаем корректное значение имени
m.name = "ValidModelName"
print(m.name) 
# Выведет: ValidModelName
