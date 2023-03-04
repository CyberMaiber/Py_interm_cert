def loadData(file_name):
    with open(file_name, "r", encoding="UTF-8") as data:
        return data.read().split("\n")

def saveData(file_name,notebook):
    with open(file_name, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(notebook)))