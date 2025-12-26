class Vector3D:
# Фиксируем только эти атрибуты
    __slots__ = ('x', 'y', 'z')  
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
# Создаём объект
v = Vector3D(1, 2, 3)
# Проверяем, что __dict__ отсутствует
print("Есть ли __dict__?", hasattr(v, '__dict__'))  
# добавляем новый атрибут
try:
    v.color = "red"
except AttributeError as e:
    print("Ошибка при добавлении color:", e)