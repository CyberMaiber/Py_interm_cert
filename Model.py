notebook = []

splitter = "|"

path = ''

current_index = 1

def getIndex(element:str):
    return int(element[:element.index(splitter)])

def getNumByIndex(index):
    i = 0
    for item in notebook:
        if getIndex(item) == index:
            return i
        else:
            i += 1
    return -1
