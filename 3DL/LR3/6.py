def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            # Если элемент — список, рекурсивно его разглаживаем
            # и добавляем его элементы в result
            result.extend(deep_flatten(item))
        else:
            # Если это обычный элемент — просто добавляем его
            result.append(item)
    return result
# Проверка (с исправленным именем переменной!)
complex_lst = [1, [2, [3, 4], 5], 6, [[7], 8]]
print(deep_flatten(complex_lst))