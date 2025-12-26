class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    def __mul__(self, other):
        # Умножение на число (int/float)
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        # Скалярное произведение с другим вектором
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

# Пример
v1 = Vector(2, 3)
v2 = Vector(4, 1)
print(v1 + v2)          
print(v1 - v2)          
print(v1 * 3)           
print(v1 * v2)         
print(v1 == Vector(2, 3)) 