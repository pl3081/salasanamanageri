from tkinter import * 
import tkinter as tk
from cryptography.fernet import Fernet
from registration import Register
import hashlib
import os
import UI





root = tk.Tk()


base_text = tk.Label(text="Kirjaudu sisään")
base_text.grid(row=0, column=0)

username_text = tk.Label(text="Käyttäjänimi")
username_text.grid(row=1, column=0)

username_entry = tk.Entry()
username_entry.grid(row=2, column=0)

password_text = tk.Label(text="salasana")
password_text.grid(row=3, column=0)

password_entry = tk.Entry()
password_entry.grid(row=4, column=0)

#defines what the login button does
def login_button():
    get_username = username_entry.get()
    get_password = password_entry.get().encode()
    encrypted_password = hashlib.sha256(get_password).hexdigest()
    parent_directory = "../salasanamanageri/login_details"
    password_directory = get_username + "/" + "password"
    path = os.path.join(parent_directory, password_directory)
    try:
        with open(path + "/" + "password.txt", 'r') as f:
            data = f.readline()
            f.close()
        if encrypted_password == data:
            print("kirjautuminen onnistui")
            root.destroy()
            UI.main()
        else:
            print("syöttämäsi salasana ei ole oikea")
    except:
        print("kirjoittamaasi käyttäjänimeä ei ole olemassa")

#opens the registeration screen
def registration_button():
    Register.Main()
    
    
    


login_button = tk.Button(text="login", command=login_button)
login_button.grid(row=4,column=1)

registation_button = tk.Button(text="Rekisteröidy", command=registration_button)
registation_button.grid(row=5, column=0)


if not os.path.exists("../salasanamanageri/login_details"):
    os.makedirs("../salasanamanageri/login_details")

    
root.mainloop()