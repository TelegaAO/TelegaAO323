text = input("Введите текст: ")
vowels = "ауоиэыяюеёaeiouy"
result = ""
i = 0
while i < len(text):
    if text[i] not in vowels:
        result += text[i]
    i += 1
print("Результат", result)
