def sum_digits(number):
# Базовый случай: если число состоит из одной цифры
    if number < 10:
        return number     
# Рекурсивный шаг:
# последняя цифра — это number % 10
# остальные цифры — number // 10
    return (number % 10) + sum_digits(number // 10)
# Примеры использования
print(sum_digits(123))   
print(sum_digits(0))  