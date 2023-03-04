
def choice_menu():
    print('\nГлавное меню:')
    print('1. Показать список заметок')
    print('2. Показать заметку...')
    print('3. Добавить заметку...')
    print('4. Изменить заметку...')
    print('5. Удалить заметку...')
    print('0. Выйти из программы')
    choice = int(input('Выберите пункт: '))
    return choice

def print_note_added():
    print('\nЗаметка добавлена\n')

def print_note_deleted():
    print('\nЗаметка удалена\n')

def notes_file_tobe_created():
    print('\nПредыдущих заметок не найдено. Будет создан новый файл.\n')

def printNoteBook(notebook):
    for i, item in enumerate(notebook):
        print(i , item)

def printOneNote():
    None

def choice_to_delete():
    return int(input('Введите номер элемента для удаления: '))

