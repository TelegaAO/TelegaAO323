number = int(input("Введите число: "))
print(f"Таблица умножения для числа {number}:")
for a in range(1, 11):
    result = number * a
    print(f"{number} * {a} = {result}")