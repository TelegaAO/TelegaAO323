import time
import random

def find_duplicates(arr):
    """Наивный поиск дубликатов с O(n^2) сложностью."""
    duplicates = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

# Генерация случайных данных
random.seed(42)  # для воспроизводимости

# Тест 1: список из 5000 элементов
arr1 = [random.randint(1, 1000) for _ in range(5000)]

start_time = time.time()
result1 = find_duplicates(arr1)
time1 = time.time() - start_time

# Тест 2: список из 10000 элементов (в 2 раза больше)
arr2 = [random.randint(1, 1000) for _ in range(10000)]
start_time = time.time()
result2 = find_duplicates(arr2)
time2 = time.time() - start_time

# Вывод результатов
print(f"Размер списка: 5000  → Время выполнения: {time1:.4f} секунд")
print(f"Размер списка: 10000 → Время выполнения: {time2:.4f} секунд")

# Анализ: во сколько раз выросло время?
if time1 > 0:
    ratio = time2 / time1
    print(f"\nДанные увеличились в 2 раза, а время выросло примерно в {ratio:.1f} раз(а).")
else:
    ratio = "∞"
    print("\nВремя на первом тесте было слишком мало для точного расчёта.")

#Объяснение:
#Теоретически, при O(n²), если n → 2n, то время → (2n)² = 4n²,
#то есть должно вырасти в ~4 раза.
# На практике — получаем близко к 4 (например, 3.8, 4.2 и т.д.).