import tkinter as tk
from tkinter import *

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.buttons = []
        for i in range(6):
            self.buttons.append(tk.Button(self, text="Button %s" % (i+1,), background="gray"))
        self.main = tk.Frame(self, background="blue")
        self.buttons[0].grid(row=0, column=0, sticky="nsew")
        self.buttons[1].grid(row=1, column=0, sticky="nsew")
        self.main.grid(row=2, column=2, columnspan=2, rowspan=6)

        for row in range(8):
            self.grid_rowconfigure(row, weight=1)
        for col in range(3):
            self.grid_columnconfigure(col, weight=1)



if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.geometry("800x400")
    root.mainloop()
