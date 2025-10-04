class Circle:
    def __init__(self, radius):
        self._radius = radius

    @classmethod
    def validate_radius(cls, radius):
        if radius < 0:
            raise ValueError ('Radius cannot be negative')
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self.validate_radius(radius)
        self._radius = radius
    
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
    
    @property
    def diameter(self):
        return 2 * self._radius

# Создадим экземпляр класса Circle с радиусом 5
circle_1 = Circle(5)
print(f"Радиус круга: {circle_1.radius}")
print(f"Площадь круга: {circle_1.area}")
print(f"Диаметр круга: {circle_1.diameter}")


# Изменим радиус круга на 10
circle_1.radius = 10
print(f"Площадь круга после изменения радиуса: {circle_1.area}")
print(f"Диаметр круга после изменения радиуса: {circle_1.diameter}")


# Попробуем установить отрицательный радиус
try:
    circle_1.radius = -5
except ValueError as ve:
    print(ve)


# Радиус круга: 5
# Площадь круга: 78.5
# Диаметр круга: 10
# Площадь круга после изменения радиуса: 314.0
# Диаметр круга после изменения радиуса: 20
# Radius cannot be negative




# Создадим экземпляр класса Circle с радиусом 15 для другого проекта
circle_2 = Circle(15)
print(f"Радиус другого круга: {circle_2.radius}")
print(f"Площадь другого круга: {circle_2.area}")
print(f"Диаметр другого круга: {circle_2.diameter}")


# Радиус другого круга: 15
# Площадь другого круга: 706.5
# Диаметр другого круга: 30
