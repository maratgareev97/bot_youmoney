fileInput = input()
def searchFile(name):
    if fileInput == "1234":
        f = open("file_token/1234.txt")
        fileRead = f.readline()
    elif fileInput == "5678":
        f = open("file_token/5678.txt")
        fileRead = f.readline()
    else:
        fileRead = "Такой файл не найден!"
    return fileRead

print(searchFile("12121212"))
