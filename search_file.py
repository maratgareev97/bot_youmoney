import os
def searchFile(name):
    dir = "file_token"
    os.chdir(dir)
    dir = os.getcwd()
    if os.path.exists(name):
        f = open(name)
        fileRead = f.readline()
    else:
      fileRead = "false"
    return fileRead

print(searchFile("5678.txt"))
