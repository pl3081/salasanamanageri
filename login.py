from tkinter import * 
import tkinter as tk
from cryptography.fernet import Fernet
from registration import Register






root = Tk()


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


def login_button():
    pass

def registration_button():
    root.destroy()
    Register.Main()
    
    
    


login_button = tk.Button(text="login", command=login_button)
login_button.grid(row=4,column=1)

registation_button = tk.Button(text="Rekisteröidy", command=registration_button)
registation_button.grid(row=5, column=0)

    
root.mainloop()