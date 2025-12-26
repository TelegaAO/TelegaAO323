numbers = [11, 11, 33, 57, 16, 19, 66, 77, 88, 99]
even_integer = []
for num in numbers:
    if num % 2 == 0:
        even_integer.append(num)

big_numbers = []
for num in numbers:
    if num > 50:
        big_numbers.append(num)
print(f"Все числа: {numbers}")
print(f"Четные числа: {even_integer}")
print(f"Числа больше 50: {big_numbers}")