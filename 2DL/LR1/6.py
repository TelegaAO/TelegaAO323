symbol = input("Введите символ для рисования: ")
height = int(input("Введите высоту прямоугольник: "))
width = int(input("Введите ширину прямоугольний: "))
a = 0
while a < height:
    b = 0
    while b < width:
        print(symbol, end="")
        b += 1
    print()
    a += 1