from tkinter import *
import tkinter as tk

def main(path):


    def add_password():
        website = website_entry.get()
        password = password_entry.get()
        line = website + ":" + password
        with open(path + "/" + "passwords.txt", "a+") as a_file:
            a_file.write(line + "\n")
        a_file.close()
    password_root = tk.Tk()
    password_frame = Frame(password_root)
    password_frame.grid()

    website_entry = Entry(password_frame, text="syötä verkkosivun nimi")
    website_entry.grid(row=0, column=0)

    password_entry = Entry(password_frame, text="syötä verkkosivun salasana")
    password_entry.grid(row=1, column=0)

    submit_button = Button(password_frame, text="submit", command=add_password)
    submit_button.grid(row=2, column=0)

    password_frame.mainloop()



    



