class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'


a = Vector(1, 2)
b = Vector(3, 4)
print(a)
print(b)

c = a + b

print(c)
