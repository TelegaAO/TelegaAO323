def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
n = int(input("Количество чисел Фибоначчи: "))
for num in fibonacci(n):
    print(num)