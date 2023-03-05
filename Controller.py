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
                Interact.print_note_changed()
            case 1:
                printNotebook()
            case 6:
                #печатаем с соритировкой по дате
                Interact.printNoteBook_sortByDate(Model.notebook,Model.splitter)
            case 2:
                show_note()
            case 0:
                save_notes()
                break


def start():
    load_notes()
    main_menu()


def load_notes():
    Model.path = 'notebook.txt'
    try:
        Model.notebook = LoadSave.loadData(Model.path)
        Model.current_index = Model.getIndex(Model.notebook[-1]) + 1
    except:
        Interact.new_notes_tobe_created()


def save_notes():
   LoadSave.saveData(Model.path, Model.notebook)

def add_note():
    name = Interact.adding_name()
    body = Interact.adding_body()
    note = f'{Model.current_index}{Model.splitter}{datetime.now()}{Model.splitter}{name}{Model.splitter}{body}'
    Model.current_index += 1
    Model.notebook.append(note)

def remove_note():
    choice = Model.getNumByIndex(Interact.choice_to_delete())
    Model.notebook.pop(choice)

def change_note():

    choice = Model.getNumByIndex(int(input('Введите индекс элемента для изменения: ')))
    choice2 = int(input('Что изменяем (1-Название, 2-Текст заметки): '))
    
    Interact.printOneNote(Model.notebook[choice],Model.splitter)

    match (choice2):
        case 1:
            Model.replaceName(choice,input('Введите новое название заметки: '))
        case 2:
            Model.replaceBody(choice,input('Введите новый текст заметки: '))
    

def show_note():
    i = Model.getNumByIndex(Interact.choice_to_show())
    Interact.printOneNote(Model.notebook[i],Model.splitter)

def printNotebook():
    Interact.printNoteBook(Model.notebook,Model.splitter)