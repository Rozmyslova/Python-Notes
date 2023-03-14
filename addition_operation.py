from correct_note_length import correct_note_length
from Note import Note


def create_note():
    print('Напоминаем, что длина названия и сама заметки должны быть больше 6 символов')
    title = correct_note_length(
        input('Введите название заметки: '))
    body = correct_note_length(
        input('Введите саму заметку: '))
    return Note(title=title, body=body)


def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note(
                id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array


def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.to_string(notes))
        file.write('\n')
    file.close
