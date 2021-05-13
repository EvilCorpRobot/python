from tkinter import filedialog
import tkinter
from hashlib import sha256
import os

keyss = "You!Are#The@Admin"
keys = sha256(keyss.encode())
key = keys.hexdigest()

def checkPass():
    global pass_crypt
    pass1 = entry_password.get()
    pass2 = entry_password1.get()
    if pass1 == pass2:
        pass_encode = sha256(pass1.encode())
        pass_crypt = pass_encode.hexdigest()
        label_password.destroy()
        entry_password.destroy()
        entry_password1.destroy()
        button_validation.destroy()
        passapp.destroy()
        passapp.quit()
        return
    else:
        pass

def getInputPassword():
    global passapp
    passapp = tkinter.Tk()
    passapp.geometry("250x150")
    global label_password
    label_password = tkinter.Label(passapp, text="Choissiser un mots de pass :")
    label_password.pack()
    global entry_password
    entry_password = tkinter.Entry(passapp, width=20, show='*')
    entry_password.pack()
    global entry_password1
    entry_password1 = tkinter.Entry(passapp, width=20, show='*')
    entry_password1.pack()
    global button_validation
    button_validation = tkinter.Button(passapp, text="Validé", command=checkPass)
    button_validation.pack()
    passapp.mainloop()
    return pass_crypt


def xorFile(name_src, password_encrypt):
    name_dest = name_src + ".loadcrypt"
    password = password_encrypt
    with open(name_src, "rb") as file_entry_bin:
        with open(name_dest, "wb") as file_exit_bin:
            i = 0
            while file_entry_bin.peek():
                octet_bin = bin(ord(file_entry_bin.read(1)))
                index_key = i % len(password)
                bin1 = bin(ord(password[index_key]))
                crypt_bin = bytes(int(octet_bin[2:])^int(bin1[2:]))
                file_exit_bin.write(crypt_bin)
                i += 1
                print(str(octet_bin))
    with open(name_dest, "rb") as file_entry_text:
        with open(name_dest + ".test", "wt") as file_exit_text:
            file_exit_text.write(password)
            bin1 = list(bytes(file_entry_text.read()))
            file_exit_text.write(str(bin1))

    '''print(name_dest)
    with open(name_dest + ".test", "rb") as file_entry_finally_bin:
        with open(name_src + ".crypt", "wb") as file_exit_finally_bin:
            i = 0
            print(name_dest)
            while file_entry_finally_bin.peek():
                    octet_bin = bin(ord(file_entry_finally_bin.read(1)))
                    index_key = i % len(key)
                    bin1 = bin(ord(key[index_key]))
                    crypt_bin = bytes(int(octet_bin[2:])^int(bin1[2:]))
                    file_exit_finally_bin.write(crypt_bin)
                    i += 1'''



def cryptFile():
    filenamee = tkinter.filedialog.askopenfile(initialdir="~",
                                                        title="Sélectionné un fichier à crypté",
                                                        filetypes=(("Fichier TEXTE","*.txt"),("Fichier PDF","*.pdf"), ("Tous les Fichier","*.*")))
    password_use = getInputPassword()
    filename_entry = filenamee.name
    xorFile(filename_entry, password_use)
