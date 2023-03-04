notebook = []

splitter = "|"

path = ''

current_index = 1

def getIndex(element:str):
    # print (element[:element.index(splitter)])
    # print (int(element[element.index(splitter) - 1:]))
    return int(element[:element.index(splitter)])
