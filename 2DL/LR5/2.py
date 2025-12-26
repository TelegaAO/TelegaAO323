students = [
    ("Анна", 21, 4.5),
    ("Петр", 22, 4.2),
    ("Мария", 19, 4.8),
    ("Антон", 23, 3.6),
    ("Владмир", 18, 4.9)
]
print("Студенты старше 20 лет:")
for name, age, points in students:
    if age > 20:
        print(f"- {name} ({age}), средний балл: {points}")
best_student = max(students, key=lambda x: x[2])
print(f"Лучший студент: {best_student[0]}, средний балл: {best_student[2]}")
sorted_students = sorted(students, key=lambda x: x[0])
print("Отсортированные студенты:")
for name, age, points in sorted_students:
    print(f"- {name} ({age}), средний балл: {points}")