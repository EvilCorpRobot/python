import tkinter
from hashlib import sha256
from login import *
from windowscrypt import *

startWindowsCrypt()

def startWindowsLogin():
    global app
    app = tkinter.Tk()
    app.geometry("250x200")
    #loginWindows()
    #app.mainloop()

def getEntryLogIn():
    str1 = entry_password.get()
    str2 = entry_username.get()
    if checkLogIn(login=str2, password=str1):
        app.destroy()
        startWindowsCrypt()
    else:
        pass
    

def registeryWindows():
    try:
        label_username.destroy()
        entry_username.destroy()
        label_password.destroy()
        entry_password.destroy()
        button_registery.destroy()
        button_logIn.destroy()
    except:
        pass
    global label_newUser
    label_newUser = tkinter.Label(app, text="Username :")
    label_newUser.pack()
    global entry_newUser
    entry_newUser = tkinter.Entry(app, width=20)
    entry_newUser.pack()
    global label_newPass
    label_newPass = tkinter.Label(app, text="Password :")
    label_newPass.pack()
    global entry_newPass
    entry_newPass = tkinter.Entry(app, width=20, show='*')
    entry_newPass.pack()
    global label_checkPass
    label_checkPass = tkinter.Label(app, text='Check your Password :')
    label_checkPass.pack()
    global entry_checkPass
    entry_checkPass = tkinter.Entry(app, width=20, show='*')
    entry_checkPass.pack()
    global button_logIn2
    button_logIn2 = tkinter.Button(app, text="Log-in", command=loginWindows)
    button_logIn2.pack()
        

def loginWindows():
    try:
        label_newUser.destroy()
        entry_newUser.destroy()
        label_newPass.destroy()
        entry_newPass.destroy()
        label_checkPass.destroy()
        entry_checkPass.destroy()
        button_logIn2.destroy()
    except:
        pass

    global label_username
    label_username = tkinter.Label(app, text='Username :')
    label_username.pack()
    global entry_username
    entry_username = tkinter.Entry(app, width=20)
    entry_username.pack()
    global label_password
    label_password = tkinter.Label(app, text="Password :")
    label_password.pack()
    global entry_password
    entry_password = tkinter.Entry(app, width=20, show='*')
    entry_password.pack()
    global button_logIn
    button_logIn = tkinter.Button(app, text='Log-in', command=getEntryLogIn)
    button_logIn.pack()
    global button_registery
    button_registery = tkinter.Button(app, text="Registery", command=registeryWindows)
    button_registery.pack()