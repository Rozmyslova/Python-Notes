import addition_operation
from Note import Note


def add():
    note = addition_operation.create_note()
    array = addition_operation.read_file()
    for notes in array:
        if Note.get_id(note) == Note.get_id(notes):
            Note.set_id(note)
    array.append(note)
    addition_operation.write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    global date
    logic = True
    array = addition_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.get_date(notes):
                print(Note.map_note(notes))
    if logic:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = addition_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = addition_operation.create_note()
                Note.set_title(notes, note.get_title())
                Note.set_body(notes, note.get_body())
                Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.map_note(notes))
    if logic:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    addition_operation.write_file(array, 'a')
