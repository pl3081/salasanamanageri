import string
import random
from tkinter import *
import tkinter as tk
import pyperclip


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def main():
	def generate_random_password(length):

		## shuffling the characters
		random.shuffle(characters)
		
		## picking random characters from the list
		password = []
		for i in range(length):
			password.append(random.choice(characters))

		## shuffling the resultant password
		random.shuffle(password)

		## converting the list to string
		## printing the list
		print("".join(password))
		password_label.config(text="".join(password))
		return "".join(password)

	root = Tk()
	generator_frame = Frame(root)
	generator_frame.grid()
	#used because tkinter buttons don't take arguments without executing the command before the button is pressed
	def generate():
		generate_random_password(int(password_length.get()))

	#copies the password to clipboard
	def copy_to_clipboard():
		pyperclip.copy(password_label.cget("text"))
		
	
	password_length = tk.Entry(generator_frame,text="Enter password length: ")
	
	submit_button = tk.Button(generator_frame,text="submit", command=generate)
	
	password_label = Label(generator_frame,text="")
	
	copy_password = Button(generator_frame,text="copy to clipboard", command=copy_to_clipboard)
	
	
		
	password_length.grid(row=0, column=0)
	submit_button.grid(row=1, column=0)
	password_label.grid(row=3, column=0)
	copy_password.grid(row=4, column=0)
	root.mainloop()
