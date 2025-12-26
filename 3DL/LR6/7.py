class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __setattr__(self, name, value):
        if name == "age":
            if value < 0:
                print("Нельзя быть младше 0")
                value = 0
            # Устанавливаем значение безопасно, чтобы не вызывать рекурсию
            self.__dict__[name] = value
        else:
            # Для всех остальных атрибутов — стандартное поведение
            super().__setattr__(name, value)
    def __getattr__(self, name):
        # Вызывается если атрибут не найден
        return None
# Пример
p = Person("Ivan", 30)
p.age = -5            
print(p.age)          
print(p.name)  
print(p.job)           