from correct_choice import correct_enter_choice
import functional as f


def menu():
    note_menu = True
    while note_menu:
        print("Приложение Заметки имеет следующий функционал:\n\
                1 - создать заметку;\n\
                2 - редактировать заметку;\n\
                3 - показать все заметки;\n\
                4 - показать заметки по дате;\n\
                5 - показать заметки по id;\n\
                6 - удалить заметку;\n\
                7 - закрыть приложение")
        choice = correct_enter_choice()
        f.functional(choice)
        if choice == 7:
            print("Спасибо за работу в приложении")
            break

