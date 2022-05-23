import tkinter as tk
from tkinter import *
import generator

def main():
    root = tk.Tk()
    root.title("Password Manager")

    listbox_URL = tk.Listbox(root, height=10, width=48)
    listbox_URL.grid(row=0, column=1, rowspan=2)

    Button1= tk.Button(root, text="lisää salasana", width=48, height=5,)
    Button1.grid(row=0, column=0)

    Button2 = tk.Button(root, text="salasanageneraattori", width=48, height=5, command=generator.main)
    Button2.grid(row=1, column=0)

    root.mainloop()