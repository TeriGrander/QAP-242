class Module27:
    '''Functions used in tasks of module 27'''

    def __init__(self):
        pass

    def is_triangle(self, a, b, c) -> bool:
        return (a + b > c) and (a + c > b) and (b + c > a)
