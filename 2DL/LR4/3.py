tasks = []
while True:
    print("1 - Показать все задачи")
    print("2 - Добавить задачу") 
    print("3 - Удалить задачу")
    print("4 - Выйти")
    choice = input("Выбери пункт: ")
    if choice == '1':
        if not tasks:
            print("Задачи отсутствуют")
        else:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")            
    elif choice == '2':
        new_task = input("Введи задачу: ")
        tasks.append(new_task)
        print("Задача добавлена")      
    elif choice == '3':
        if not tasks:
            print("Задачи отсутствуют")
        else:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Какая задача сделана? ")) - 1
            if 0 <= num < len(tasks):
                removed = tasks.pop(num)
                print(f'Задача "{removed}" убрана')
            else:
                print("Ошибка!")           
    elif choice == '4':
        print("Завершение сеанса")
        break
    else:
        print("Ошибка!")