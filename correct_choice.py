def correct_enter_choice():
    correct_choice = False
    while not correct_choice:
        choice = input("Ваш выбор: ")
        if not choice.isdigit():
            print("Вы ввели не число!")
            continue
        else:
            choice = int(choice)
            if (choice > 0) and (choice < 8):
                return choice
                correct_choice = True
            else:
                print("Такого пункта нет!")
                continue
