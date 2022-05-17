import tkinter as tk
from tkinter import *

root = Tk()
root.title("Password Manager")

PassAndURL = tk.Frame(root)
PassAndURL.grid()

listbox_URL = tk.Listbox(root, height=10, width=48)
listbox_URL.grid(row=0, column=1, rowspan=2)

Button1= tk.Button(root, text="Button 1", width=48, height=5)
Button1.grid(row=0, column=0)

Button2 = tk.Button(root, text="Button 2", width=48, height=5)
Button2.grid(row=1, column=0)

root.mainloop()