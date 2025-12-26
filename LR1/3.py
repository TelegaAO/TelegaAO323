text = input("Введите строку: ")
ignore = text.lower().replace(" ","")
left = 0
right = len(ignore) - 1
print(f"Проверка строки: '{ignore}'")
while left < right:
    print(f"Сравниваем '{ignore[left]}' и '{ignore[right]}'")
    if ignore[left] != ignore[right]:
        print("Символы не подходят")
        break
    left += 1
    right -= 1
else:
    print(f"Строка '{text}' палиндром")
if left < right:
    print(f"Строка '{text}' не палиндром")