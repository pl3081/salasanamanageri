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
    password_root.geometry("300x150")
    password_frame = Frame(password_root)
    password_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
    
    website_label = Label(password_frame, text="verkkosivu")
    website_label.pack(side="top", fill=BOTH, expand=TRUE)

    website_entry = Entry(password_frame, textvariable="verkkosivu")
    website_entry.pack(side="top", fill=BOTH, expand=TRUE)

    password_label = Label(password_frame, text="salasana")
    password_label.pack(side="top", fill=BOTH, expand=TRUE)
   

    password_entry = Entry(password_frame, text="syötä verkkosivun salasana")
    password_entry.pack(side="top", fill=BOTH, expand=TRUE)

    submit_button = Button(password_frame, text="submit", command=add_password)
    submit_button.pack(side="top", fill=BOTH, expand=TRUE)

    password_frame.mainloop()



    



