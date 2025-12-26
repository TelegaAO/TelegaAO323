height = int(input("Введите высоту пирамиды: "))
for a in range(1, height + 1):
    left = ''.join(str(j) for j in range(1, a + 1))
    right = ''.join(str(j) for j in range(a - 1, 0, -1))
    full = left + right
    total = height * 2 - 1
    spaces = ' ' * (height - a)
    print(spaces + full)
