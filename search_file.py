import string
tokenString = input(("Введите токен: "))
def searchFile(name):
    f = open("file_token/1234.txt")
    tokenRead = f.readline()

    r = open("file_token/5678.txt")
    tokenRead2 = r.readline()
    token = tokenString
    if token == tokenRead:
        token = tokenRead

    elif token == tokenRead2:
        token = tokenRead2
    else:
        token = "Токен не найден!"
    return token

print(searchFile("12121212"))
