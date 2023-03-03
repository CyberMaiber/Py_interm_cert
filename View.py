import Model


def printNoteBook():
    for i, item in enumerate(Model.notebook):
        print(i , item)


def printOneNote():
    None

def printNoteBookFltr(textToFind:str):
    lst = []
    lst = list(filter(lambda x: textToFind in x, Model.notebook))
    for i, item in enumerate(lst):
        print(i , item)
    if len(lst) == 0: print('Ничего не найдено.')