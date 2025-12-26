temperatures = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]
max_temperature = max(temperatures)
min_temperature = min(temperatures)
avg_temperature = sum(temperatures) / len(temperatures)
days_above_avg = 0
for temperature in temperatures:
    if temperature > avg_temperature:
        days_above_avg += 1
sorted_temps = sorted(temperatures)
fahrenheit = []
for temperature in temperatures:
    f = temperature * 9/5 + 32
    fahrenheit.append(f)
print(f"Температуры: {temperatures}")
print(f"Максимальная: {max_temperature}°C")
print(f"Минимальная: {min_temperature}°C")
print(f"Средняя: {avg_temperature}°C")
print(f"Дней выше средней: {days_above_avg}")
print(f"Отсортированные: {sorted_temps}")
print(f"По Фаренгейту: {fahrenheit}")