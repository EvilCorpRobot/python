from hashlib import sha256

user, password1 = ("neewz", "1234")

def checkLogIn(login=None, password=None):
    password_encode = sha256(password.encode())
    password1_encode = sha256(password1.encode())
    if login == user:
        if password_encode.hexdigest() == password1_encode.hexdigest():
            return True
        else:
            print("1")
            return False
    else:
        print("2")
        return False

