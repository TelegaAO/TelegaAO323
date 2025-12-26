phone_book = {'Мама': '777', 'Папа': '999', 'Шиздиспансер': '666'}
while True:
    print("1 - Показать все контакты")
    print("2 - Добавить контакт") 
    print("3 - Удалить контакт")
    print("4 - Выйти")   
    choice = input("Выбери действие: ")
    if choice == '1':
        print("Телефонная книга:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")         
    elif choice == '2':
        name = input("Введи имя: ")
        if name in phone_book:
            print("Уже существует")
        else:
            phone = input("Введи телефон: ")
            phone_book[name] = phone
            print("Контакт добавлен")         
    elif choice == '3':
        name = input("Введи имя для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print("Контакт удален")
        else:
            print("Такого контакта нет")  
    elif choice == '4':
        print("Завершение сеанса")
        exit()
    else:
        print("Ошибка!")