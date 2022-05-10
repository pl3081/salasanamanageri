from importlib.resources import path
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *
import os
import hashlib

from matplotlib.style import use






class Register():
    

    
    
    def Main():
        def encrypt_password():
            password = password_entry.get().encode()
            encrypted_password = hashlib.sha256(password).hexdigest()
            return encrypted_password
            


        def registratration():
            par_directory = "../salasanamanageri/login_details"
            username = username_entry.get()
            password = encrypt_password()
            password_directory = username + "/" + "password"
            directory = username
            path = os.path.join(par_directory, directory)
            password_path = os.path.join(par_directory, password_directory)
            os.makedirs(path)
            os.makedirs(password_path)

            with open(password_path + "/" + "password.txt", 'x') as f:
                f.writelines(password)
                f.close()
            
        


        reg_root = Tk()
        base_text = tk.Label(text="Rekisteröidy")
        base_text.grid(row=0, column=0)

        username_text = tk.Label(text="Käyttäjänimi")
        username_text.grid(row=1, column=0)

        username_entry = tk.Entry()
        username_entry.grid(row=2, column=0)

        password_text = tk.Label(text="salasana")
        password_text.grid(row=3, column=0)

        password_entry = tk.Entry()
        password_entry.grid(row=4, column=0)

        registration_button = tk.Button(text="rekisteröidy", command=registratration)
        registration_button.grid(row=4,column=1)
        reg_root.mainloop()

    