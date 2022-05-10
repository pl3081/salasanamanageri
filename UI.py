import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('1280x720')
root.title('Password manager UI')

# Buttons
button1=tk.Button(root, text="button1")
button1.grid(row=0,column=0)

button2=tk.Button(root, text="button2")
button2.grid(row=1,column=0)

# Passwords
D = {'d1': {'a':'1'}, 'd2': {'b':'2'}, 'd3': {'c':'3'}}

lb = Label(root, text='')
lb['text'] = '\n'.join('{} {}'.format(k, d) for k, d in D.items())
lb.grid(row=2, column=0)

# Websites

root.mainloop()