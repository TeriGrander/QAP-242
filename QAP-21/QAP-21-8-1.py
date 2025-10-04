class SellItem:
    def __init__(self, name: str, price) -> None:
        self.name = name
        self.price = price

class House(SellItem):
    def __init__(self, name: str, price, material: str, square) -> None:
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem):
    def __init__(self, name: str, price, size, rooms) -> None:
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Agency():
    def __init__(self, name: str) -> None:
        self.name = name
        self.objs = []
    def add_object(self, obj):
        self.objs.append(obj)
    def remove_object(self, obj):
        self.objs.remove(obj)
    def get_objects(self):
        return self.objs