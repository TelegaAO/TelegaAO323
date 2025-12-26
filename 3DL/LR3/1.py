def power(a, n):
    # Базовый случай: любое число в степени 0 равно 1
    if n == 0:
        return 1
    # Рекурсивный шаг: a^n = a * a^(n-1)
    return a * power(a, n - 1)
# Примеры использования
print(power(2, 3)) 
print(power(5, 0)) 