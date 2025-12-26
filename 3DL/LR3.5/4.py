import time
import random

# Дано:
def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

# Быстрое решение за O(n)
def find_pair_fast(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

# Демонстрация разницы в скорости
random.seed(42)
arr = [random.randint(1, 10000) for _ in range(10_000)]
target = 15000  

# Замер медленной версии
print("Запускаем медленную версию (O(n²))...")

start_time = time.time()
result_slow = find_pair_slow(arr, target)
time_slow = time.time() - start_time

# Замер быстрой версии
print("Запускаем быструю версию (O(n))...")

start_time = time.time()
result_fast = find_pair_fast(arr, target)
time_fast = time.time() - start_time

#Результаты
print(f"\nМедленная версия: {result_slow}, время: {time_slow:.4f} сек")
print(f"Быстрая версия:  {result_fast}, время: {time_fast:.6f} сек")

# Вывод по скорости
if time_slow > 0:
    speedup = time_slow / time_fast if time_fast > 0 else float('inf')
    print(f"\nУскорение: в {speedup:.0f} раз быстрее!")