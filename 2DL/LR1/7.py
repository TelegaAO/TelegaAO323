symbol = input("Введите символ для рисования: ")
height = int(input("Введите высоту прямоугольник: "))
width = int(input("Введите ширину прямоугольний: "))
a = 1
while a <= height:
    if a == 1 or a == height:
        print(symbol * width)
    else:
        print(symbol + ' ' * (width - 2) + symbol)
    a += 1
