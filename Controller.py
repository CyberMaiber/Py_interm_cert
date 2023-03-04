import Model
import Interact
import LoadSave
from datetime import datetime

def main_menu():
    while True:
        choice = Interact.choice_menu()
        match (choice):
            case 3:
                add_note()
                Interact.print_note_added()
            case 5:
                remove_note()
                Interact.print_note_deleted()
            case 4:
                change_note()
            case 1:
                show_all_notes()
            case 2:
                show_note()
            # case 6:
            #     find_contacts()
            # case 7:
            #     open_file()
            # case 8:
            #     save_file()
            #     print('\nФайл сохранен!\n')
            case 0:
                save_notes()
                break


def start():
    load_notes()
    # Interact.printNoteBook(Model.notebook)
    main_menu()


def load_notes():
    # while True:
        # input('Введите имя файла телефонной книги: ')
    Model.path = 'notebook.txt'
    try:
        Model.notebook = LoadSave.loadData(Model.path)
        Model.current_index = Model.getIndex(Model.notebook[-1]) + 1
    except:
        Interact.new_notes_tobe_created()
    # Interact.printNoteBook(Model.notebook)

def save_notes():
   LoadSave.saveData(Model.path, Model.notebook)

def add_note():
    name = input('Введите название заметки: ')
    body = input('Введите текст заметки: ')
    note = f'{Model.current_index}{Model.splitter}{datetime.now()}{Model.splitter}{name}{Model.splitter}{body}'
    Model.current_index += 1
    Model.notebook.append(note)
    Interact.printNoteBook(Model.notebook)

def remove_note():
    choice = Interact.choice_to_delete()
    Model.phonebook.pop(choice)
    Interact.printPhoneBook()

def change_note():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.notebook.insert(choice, ';'.join(contact))
    Interact.printNoteBook()

def show_all_notes():
    Interact.printNoteBook(Model.notebook)

def show_note():
    None
# def find_contacts():
#     toSearch = input('Введите данные для поиска: ')
#     View.printNoteBookFltr(toSearch)
