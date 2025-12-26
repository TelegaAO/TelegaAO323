number = int(input("Введите число: "))
num = 0
for a in range(1, number+1):
    num += a
print(f"Сумма чисел от 1 до {number} = {num}")