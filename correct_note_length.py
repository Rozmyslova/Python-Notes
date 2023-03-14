def correct_note_length(text: object) -> object:
    while len(text) <= 4:
        print(f'Текст должен быть больше 4 символов\n')
        text = input('Введите тескт: ')
    else:
        return text
