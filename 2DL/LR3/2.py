text = input("Введите текст: ")
characters_count = {}
for characters in text.lower():
    if characters in characters_count:
        characters_count[characters] += 1
    else:
        characters_count[characters] = 1
print(characters_count)