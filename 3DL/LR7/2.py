class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  
# Используем сеттер, чтобы сразу провести валидацию
    @property
    def salary(self):
        """Геттер: возвращает текущую зарплату."""
        return self._salary
    @salary.setter
    def salary(self, value):
        """Сеттер: проверяет, что зарплата не отрицательная."""
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной!")
        self._salary = value
# Пример
emp = Employee("John", 50000)
try:
    emp.salary = -100  
except ValueError as e:
    print(e)
emp.salary = 60000  
print(emp.salary)   