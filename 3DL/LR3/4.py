def find_max(arr):
    # Базовый случай: если в списке один элемент — он и есть максимум
    if len(arr) == 1:
        return arr[0]
    
    # Делим список на две (примерно) равные части
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Рекурсивно находим максимум в каждой половине
    left_max = find_max(left_half)
    right_max = find_max(right_half)
    
    # Возвращаем больший из двух
    return left_max if left_max > right_max else right_max


# Проверка 
numbers = [3, 7, 1, 9, 4, 2]
print(find_max(numbers)) 