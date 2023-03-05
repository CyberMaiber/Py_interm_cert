from datetime import datetime

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
    return None

def replaceName(number,newName):
    temp = notebook[number].split(splitter)
    notebook[number] = notebook[number].replace(temp[2],newName)
    replaceDate(number)

def replaceBody(number,newBody):
    temp = notebook[number].split(splitter)
    notebook[number] = notebook[number].replace(temp[3],newBody)
    replaceDate(number)

def replaceDate(number):
    temp = notebook[number].split(splitter)
    notebook[number] = notebook[number].replace(temp[1],str(datetime.now()))