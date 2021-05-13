from tkinter import filedialog
import tkinter
from hashlib import sha256
import os
from cryptfiles import *

keyss = "You!Are#The@Admin"
keys = sha256(keyss.encode())
key = keys.hexdigest()

def startWindowsCrypt():
    global app
    app = tkinter.Tk()
    app.geometry("400x300")
    adminWindowsCrypt()
    app.mainloop()


    







def cryptFile1():
    try:
        print(pass_crypt)
        filename_sortie1 = filename.name + ".loadcrypt1"
        with open(filename.name, "rb") as f_entree1:
            with open(filename_sortie1, "wb") as f_sortie1:
                try:
                    while True:
                        record = f.read(1)
                        if len(record) != 1:
                            break
                    octect_bin = ord(record)
                    print("1")
                    index_key = i % len(key)
                    print("2")
                    crypt_bin = bytes([octect_bin^key[index_key]])
                    f_sortie1.write(crypt_bin)
                except IOError:
                    pass
        filename_sortie = filename.name + ".loadcrypt123"
        with open(filename.name, "rt") as f_entree:
            lignes = f_entree.readlines()
            with open(filename_sortie, "wt") as f_sortie:
                f_sortie.write(pass_crypt)
                print("1")
                for ligne in lignes:
                    f_sortie.write(ligne)
        print("1")
        filename_sortie2 = filename.name + ".crypt"
        print(filename_sortie2)
        with open(filename_sortie1, "rb") as f_entree2:
            lignes = f_entree2.readlines()
            with open(filename_sortie2, "wb") as f_sortie2:
                i = 0
                for ligne in lignes:
                    octect_bin = ord(ligne)
                    index_key = i % len(pass_crypt)
                    crypt_bin = bytes([octect_bin^pass_crypt[index_key]])
                    f_sortie2.write(crypt_bin)
                    i += 1

            
    except:
        pass

def decryptFile():
    
    try:
        filename = tkinter.filedialog.askopenfile(initialdir="~",
                                                    title="Sélectionné un fichier à décrypté",
                                                    filetypes=(("Fichier CRYPTE","*.crypt"),))
        filename_sortiee = filename.name.split(".crypt")
        filename_sortie = filename_sortiee[0]
        with open(filename.name, "rb") as f_entree:
            with open(filename_sortie, "wb") as f_sortie:
                i = 0
                while f_entree.peek():
                    octect_bin = ord(f_entree.read(1))
                    index_key = i % len(key)
                    decrypt_bin = bytes([octect_bin^key[index_key]])
                    f_sortie.write(decrypt_bin)
                    i += 1
    except:
        pass


def adminWindowsCrypt():
    global button_crypt
    button_crypt = tkinter.Button(app, text="Crypt your file", command=cryptFile)
    button_crypt.pack()
    global button_decrypt
    button_decrypt = tkinter.Button(app, text="Décrypt your file", command=decryptFile)
    button_decrypt.pack()
    global admin_mode
    admin_mode = tkinter.Button(app, text="Admin Mode")
    admin_mode.pack()

