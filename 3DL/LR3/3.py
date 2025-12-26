def binary_search(arr, target, left=0, right=None):
    # При первом вызове right не задан — устанавливаем его в конец списка
    if right is None:
        right = len(arr) - 1

    # Базовый случай: если левая граница пересекла правую — элемента нет
    if left > right:
        return -1

    #Середина
    mid = (left + right) // 2
    # Если нашел элемент — возвращаем индекс
    if arr[mid] == target:
        return mid
    # Если искомое меньше — ищет в левой половине
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    # Если искомое больше — ищет в правой половине
    else:
        return binary_search(arr, target, mid + 1, right)
# Проверка
my_list = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(my_list, 40))  
print(binary_search(my_list, 99))  