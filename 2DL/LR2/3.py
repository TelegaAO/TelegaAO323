text = input("Введите текст: ")
characters = 0
digits = 0
marks = 0
spaces = 0
letters ='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '0123456789'
mark = '.,!&:;'
space = ' '
for char in text:
    if char in letters:
        characters += 1
    elif char in digit:
        digits += 1
    elif char in mark:
        marks += 1
    elif char in space:
        spaces += 1
print("Результат: ")
print(f"Букв:{characters}")
print(f"Цифр:{digits}")
print(f"Знаков препинания:{marks}")
print(f"Пробелов:{spaces}")