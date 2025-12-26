text = ""
while True:
    line = input()
    if line == "":
        break
    text += line + " "
words = text.split()
statistics = {}
for word in words:
    key = word.lower().strip('.,!?;:')
    if key in statistics:
        statistics[key] += 1
    else:
        statistics[key] = 1
print(f"Статистика слов: {statistics}")