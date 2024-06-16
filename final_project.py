import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext

# Creating window
window = tkinter.Tk()
window.geometry("395x400") 
window.resizable(False, False)
window.title("To-Do List")
window.iconbitmap("pen.ico")
window.configure(background="#2A4494")

# Creating functions
def create_file():
	"""Function which creates a file if there is no file and then presents the content of the file in the text box widget."""
	file = open("to_do_list.txt", "a")
	with open("to_do_list.txt", "r") as file:
		content = file.read()
		box.insert(0.0, content)

def save_to_file():
	"""Function which checks if the text box widget is empty and deletes the content of the file if True and saves it otherwise writes the content of the text box widget to file and saves it."""
	file = open("to_do_list.txt", "a")
	if box.compare("end-1c", "==", "1.0"): # checks if the text box widget is empty
		file = open("to_do_list.txt", "w")
		file.close()
		messagebox.showinfo("File updated.", "to_do_list.txt was successfully saved.")
	else:
		content = box.get("end-1c linestart", "end-1c") # gets the last line input from the text box widget
		file.write(f"{content}\n")
		file.close()
		messagebox.showinfo("File updated.", "to_do_list.txt was successfully saved.")

# Creating the ScrolledText widget
box = scrolledtext.ScrolledText(window, width=34, height=10, font=("Segoe UI", 15))
box.place(x=0, y=0)

# Creating the button
button = Button(window, text="Save", command=save_to_file, font=("Segoe UI", 18, "bold"), bg="#4F5D75", fg="white")
button.place(x=95, y=315, width=200)

# Calling the create_file() function each time the program starts so that the content of the file can be loaded into the text box widget
create_file()

window.mainloop()




