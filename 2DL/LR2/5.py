digits = int(input("Сколько чисел вы хотите ввести? "))
numbers = []
for i in range(digits):
    number = int(input(f"Введите число {i+1}: "))
    numbers.append(number)
max_number = numbers[0]
min_number = numbers[0]
sum_number = 0
for number in numbers:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
    sum_number += number
average = sum_number / digits
mta = 0
for number in numbers:
    if number > average:
        mta += 1
print("Результат:")
print(f"Максимальное: {max_number}")
print(f"Минимальное: {min_number}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {mta}")
