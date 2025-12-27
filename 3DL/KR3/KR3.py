# 10 Вариант
import time
def memoize(func):
    """Декоратор для кэширования результатов функции."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"[КЭШ] Возвращаем результат для аргументов {args} из кэша")
            return cache[args]
        else:
            print(f"[ВЫЧИСЛЕНИЕ] Вызываем функцию с аргументами {args}")
            result = func(*args)
            cache[args] = result
            return result
    return wrapper
@memoize
def factorial(n):
    """Рекурсивный факториал с выводом для отладки."""
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = 10
# Первый вызов - вычисление
print("=== Первый вызов ===")
start = time.time()
result1 = factorial(n)
time1 = time.time() - start
print(f"Результат: {result1}")
print(f"Время первого вызова: {time1:.6f} сек\n")
# 2-ой вызов - из кэша
print("=== Второй вызов (тот же n) ===")
start = time.time()
result2 = factorial(n)
time2 = time.time() - start
print(f"Результат: {result2}")
print(f"Время второго вызова: {time2:.6f} сек\n")
# Проверка
assert result1 == result2, "Результаты не совпадают!"