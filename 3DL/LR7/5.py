# --- Миксин ---
class LoggableMixin:
    def log(self, message):
        class_name = self.__class__.__name__
        print(f"[INFO] {class_name}: {message}")
# --- Класс Employee из задачи 2 (с миксином) ---
class Employee(LoggableMixin):
    def __init__(self, name, salary):
        self.name = name
# Используем сеттер, если он был реализован
        self.salary = salary 
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной!")
        self._salary = value
# --- Класс Product (новая реализация с миксином; датаклассы не требуются) ---
class Product(LoggableMixin):
    def __init__(self, name, price, weight, is_available):
        self.name = name
        self.price = price
        self.weight = weight
        self.is_available = is_available
# Пример
emp = Employee("Manager", 50000)
emp.log("Сотрудник создан") 
prod = Product("Laptop", 50000.0, 2.5, True)
prod.log("Товар добавлен в каталог") 