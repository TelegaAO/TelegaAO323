import time
# 1. Обычная рекурсия
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# 2. Хвостовая рекурсия с аккумулятором
def tail_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return tail_fibonacci(n - 1, b, a + b)
# Сравнение производительности
n = 35
# Замер обычной рекурсии
start_time = time.time()
result1 = fibonacci(n)
elapsed1 = time.time() - start_time
print(f"Fibonacci({n}) = {result1}")
print(f"Time taken (Naive): {elapsed1:.6f} seconds")
# Замер хвостовой рекурсии
start_time = time.time()
result2 = tail_fibonacci(n)
elapsed2 = time.time() - start_time
print(f"Tail Fibonacci({n}) = {result2}")
print(f"Time taken (Tail): {elapsed2:.6f} seconds")