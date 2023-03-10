from datetime import datetime

def choice_menu():
    print('\nГлавное меню:')
    print('1. Показать список заметок')
    print('2. Показать заметку...')
    print('3. Добавить заметку...')
    print('4. Изменить заметку...')
    print('5. Удалить заметку...')
    print('6. Показать список заметок с сортировкой по дате')
    print('0. Выйти из программы')
    choice = int(input('Выберите пункт: '))
    return choice

def print_note_added():
    print('\nЗаметка добавлена\n')

def print_note_deleted():
    print('\nЗаметка удалена\n')

def print_note_changed():
    print('\nЗаметка изменена\n')

def new_notes_tobe_created():
    print('\nПредыдущих заметок не найдено. Будет создан новый файл.\n')

def printNoteBook(notebook,splitter):
    print(f'ID\tДата-время\t\t\tНазвание')
    for item in notebook:
        temp = item.split(splitter) 
        print(f'{temp[0]}\t{temp[1]}\t{temp[2]}')

def printOneNote(item,splitter):
    temp = item.split(splitter) 
    print(f'\n{temp[2]}\n{temp[1]}\n{temp[3]}')

def choice_to_delete():
    return int(input('Введите индекс элемента для удаления: '))

def choice_to_show():
    return int(input('Введите индекс элемента для отображения: '))

def choice_to_change():
    return int(input('Введите индекс элемента для изменения: '))

def choice_to_change2():
    return int(input('Что изменяем (1-Название, 2-Текст заметки): '))

def new_name_add():
    return input('Введите новое название заметки: ')

def new_body_add():
    return input('Введите новый текст заметки: ')

def adding_name ():
    return input('Введите название заметки: ')

def adding_body():
    return input('Введите текст заметки: ')

def printNoteBook_sortByDate(notebook,splitter):
    tempbook = []
    tempbook = notebook.copy()
    while len(tempbook) != 0:
        i = 0
        temp = tempbook[i].split(splitter)
        minDate = datetime.strptime(temp[1],"%Y-%m-%d %H:%M:%S.%f")
        j = 0
        for item in tempbook:
            temp = item.split(splitter)
            tempDate = datetime.strptime(temp[1],"%Y-%m-%d %H:%M:%S.%f")
            if tempDate <= minDate:
                minDate = tempDate
                i = j
            j += 1
        temp = tempbook[i].split(splitter)
        print(f'{temp[0]}\t{temp[1]}\t{temp[2]}')
        tempbook.pop(i)