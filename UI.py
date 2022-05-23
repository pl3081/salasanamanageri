from importlib.resources import path
import tkinter as tk
from tkinter import *
from tkinter import ttk
import generator
import new_password


def main(user):
    
    
    root = tk.Tk()
    root.title("Password Manager")

    columns = ("website", "password")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    tree.heading("website", text="website")
    tree.heading("password", text="password")
    
    passwords = []

    with open(user + "/" + "passwords.txt", "r") as a_file:

        for line in a_file:
            splitted_line = line.split(":")
            passwords.append((f'{splitted_line[0]}', f'{splitted_line[1]}'))
        a_file.close()
        
    # add data to the treeview
    for password in passwords:
        tree.insert('', tk.END, values=password)


    def add_password():
        new_password.main(user)

    
    Button1= tk.Button(root, text="lisää salasana", width=48, height=5,command=add_password)

    Button2 = tk.Button(root, text="salasanageneraattori", width=48, height=5, command=generator.main)
    
    
    Button1.grid(row=0, column=0)
    Button2.grid(row=1, column=0)
    tree.grid(row=0, column=1, rowspan=2)
    root.mainloop()