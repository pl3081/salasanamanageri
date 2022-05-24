from logging import root
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *
import os
import hashlib





class Register():
    

    
    
    def Main():
        #encrypts the given password in hash256
        def encrypt_password():
            password = password_entry.get().encode()
            encrypted_password = hashlib.sha256(password).hexdigest()
            return encrypted_password
                

        #creates the folders and password files needed for login
        def registratration():
            par_directory = "../salasanamanageri/login_details"
            username = username_entry.get()
            password = encrypt_password()
            login_directory = username + "/" + "password"
            passwords_directory = username + "/" + "passwords"
            directory = username
            path = os.path.join(par_directory, directory)
            login_path = os.path.join(par_directory, login_directory)
            passwords_path = os.path.join(par_directory, passwords_directory)
            os.makedirs(path)
            os.makedirs(login_path)
            os.makedirs(passwords_path)

            with open(passwords_path + "/" + "passwords.txt", 'x') as f:
                f.close()

            with open(login_path + "/" + "password.txt", 'x') as f:
                f.writelines(password)
                f.close()
            reg_root.destroy()
            

        


        
        


        reg_root = tk.Tk()
        reg_frame = Frame(reg_root)
        reg_root.geometry("300x150")
        reg_frame.pack(side=TOP,fill=BOTH, expand=TRUE)
        
        base_text = tk.Label(reg_frame,text="Rekisteröidy")
        base_text.pack(side=TOP, fill=BOTH, expand=TRUE, padx= 10)

        username_text = tk.Label(reg_frame,text="Käyttäjänimi")
        username_text.pack(side=TOP, fill=BOTH, expand=TRUE, padx= 10)

        username_entry = tk.Entry(reg_frame,)
        username_entry.pack(side=TOP, fill=BOTH, expand=TRUE, padx= 10)

        password_text = tk.Label(reg_frame,text="salasana")
        password_text.pack(side=TOP, fill=BOTH, expand=TRUE, padx= 10)

        password_entry = tk.Entry(reg_frame,)
        password_entry.pack(side=TOP, fill=BOTH, expand=TRUE, padx= 10)

        registration_button = tk.Button(reg_frame,text="rekisteröidy", command=registratration)
        registration_button.pack(side=TOP, fill=BOTH, expand=TRUE, padx= 10)
        reg_root.mainloop()

    