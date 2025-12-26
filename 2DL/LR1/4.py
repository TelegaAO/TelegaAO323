from random import randint
random_num = randint(1, 100)
guess = None
print("Угадайте число от 1 до 100")
while guess != random_num:
    guess = int(input("Ваша попытка: "))
    if guess < random_num:
        print("Больше")
    elif guess > random_num:
        print("Меньше")
    else:
        print("Угадал")