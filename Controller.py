import Model
import View


def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Показать список заметок')
        print('2. Показать заметку')
        print('3. Добавить заметку')
        print('4. Изменить заметку')
        print('5. Удалить заметку')
        
        
        
        # print('6. Поиск контакта')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                add_note()
                print('\nЗаметка добавлена\n')
            case 2:
                remove_note()
                print('\nЗаметка удалена\n')
            case 3:
                change_note()
                
            # case 6:
            #     find_contacts()
            # case 7:
            #     open_file()
            # case 8:
            #     save_file()
            #     print('\nФайл сохранен!\n')
            case 0:
                break


def start():
    open_file()
    View.printNoteBook()
    main_menu()


def open_file():
    # while True:
        # input('Введите имя файла телефонной книги: ')
    file_name = 'notebook.txt'
    try:
        with open(file_name, "r", encoding="UTF-8") as data:
            Model.path = file_name
            notes_list = data.read().split("\n")
            Model.notebook = notes_list
    except:
        print('Предыдущих заметок не найдено. Будет создан новый файл.')
        # if file_name == 'exit': break
    View.printNoteBook()

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.notebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.notebook.insert(choice, ';'.join(contact))
    View.printNoteBook()

def find_contacts():
    toSearch = input('Введите данные для поиска: ')
    View.printNoteBookFltr(toSearch)
