# 10 Вариант
# Ввод зашифрованной строки (можно вставить свой текст)
s = input("Введите зашифрованную строку: ")
# Очистка строки: оставляем только латинские буквы и приводим к нижнему регистру
cleansed = ""
for char in s:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        cleansed += char.lower()
# Если после при очистке cтрока пустая
if not cleansed:
    print("Нет латинских букв в строке.")
else:
# Общее количество букв
    total = len(cleansed)  
    # Подсчитываем частоту каждой буквы в строке
    freq = {}
    for char in cleansed:
        freq[char] = freq.get(char, 0) + 1
    # Переводим в проценты
    for char in freq:
        freq[char] = round(freq[char] / total * 100, 2)
    # Находим топ-3 буквы
    sorted_letters = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_letters[:3]
    print("Топ-3 самых частых букв:")
    for i, (letter, percentage) in enumerate(top3, 1):
        print(f"{i}. '{letter}' — {percentage}%")
    # Проверяем гипотезу про язык
    most_common = sorted_letters[0][0]
    if most_common == 'e':
        print("Вероятно, английский язык")
    else:
        print("Язык не определен")