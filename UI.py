import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Password Manager")

PassAndURL = tk.Frame(root)
PassAndURL.pack()

listbox_URL = tk.Listbox(PassAndURL, height=10, width=48)
listbox_URL.pack(side=tk.TOP)

Button1= tk.Button(root, text="Button 1", width=48)
Button1.pack()

Button2 = tk.Button(root, text="Button 2", width=48)
Button2.pack()

root.mainloop()