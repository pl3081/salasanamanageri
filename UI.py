import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.tix import ROW
from turtle import right
import generator
import new_password



def main(user):
    
    #key = file_encryption.load_key(user)
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
    
    
    Button1.pack(side=TOP, fill=BOTH, expand=TRUE ,padx= 10)
    Button2.pack(side=TOP, fill=BOTH, expand=TRUE ,padx= 10)
    tree.pack(side=RIGHT, fill=BOTH, expand=TRUE, padx= 10)
    root.mainloop()