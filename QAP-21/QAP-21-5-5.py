class Triangle:
    def __init__(self, a, b, c):
       self.a = a
       self.b = b
       self.c = c
    def is_triangle(self):
        if (self.a < self.b + self.c) and (self.b < self.a + self.c) and (self.c < self.a + self.b): return True
        else: return False

    def get_triangle_area(self):
        p = (self.a + self.b + self.c) / 2
        if self.is_triangle(): return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else: return 0

t1 = Triangle(a=3, b=4, c=5)
print(t1.is_triangle())

# True

print(t1.get_triangle_area())

# 6.0

t2 = Triangle(a=3, b=10, c=16)
print(t2.is_triangle())

# False

print(t2.get_triangle_area())