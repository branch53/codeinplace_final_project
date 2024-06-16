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

def create_file():
	file = open("to_do_list.txt", "a")
	with open("to_do_list.txt", "r") as file:
		content = file.read()
		box.insert(0.0, content)

def save_to_file():
	file = open("to_do_list.txt", "a")
	if box.compare("end-1c", "==", "1.0"):
		file = open("to_do_list.txt", "w")
		file.close()
		messagebox.showinfo("File updated.", "to_do_list.txt was successfully saved.")
	else:
		content = box.get("end-1c linestart", "end-1c")
		file.write(f"{content}\n")
		file.close()
		messagebox.showinfo("File updated.", "to_do_list.txt was successfully saved.")


box = scrolledtext.ScrolledText(window, width=34, height=10, font=("Segoe UI", 15))
box.place(x=0, y=0)

button = Button(window, text="Save", command=save_to_file, font=("Segoe UI", 18, "bold"), bg="#4F5D75", fg="white")
button.place(x=95, y=315, width=200)

# Creating functions

#with open("to_do_list.txt", "a") as todolist:
	#todolist.write(box.get("1.0", tkinter.END))
	#box.insert(0.0, todolist)
	
create_file()

window.mainloop()




