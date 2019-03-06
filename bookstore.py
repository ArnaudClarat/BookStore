"""
A simple program that shows a list a books
and that allows the user to insert books, delete books and update books
It's done with sqlite3 as database and tkinter as gui.
"""

from tkinter import *
from tkinter import ttk
import backend as be

def get_selected_row(event):
	try:
		global selected_tuple
		index = list1.curselection()[0]
		selected_tuple = list1.get(index)
		e1.delete(0,END)
		e1.insert(END, selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END, selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END, selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END, selected_tuple[4])
	except IndexError:
		pass


def view_command():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in be.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END,row)

def add_command():
    be.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def update_command():
    be.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def delete_command():
    be.delete(selected_tuple[0])

# creating the GUI
window = Tk()
window.wm_title("Bookstore")

ttk.Style().configure("black.TLabel", foreground='blue')
ttk.Style().configure("blue/white.TButton", foreground='black')

l1 = ttk.Label(window, text="Title", style="black.TLabel")
l1.grid(row=0,column=0)

l2 = ttk.Label(window, text="Author", style="black.TLabel")
l2.grid(row=0,column=2)

l3 = ttk.Label(window, text="Year", style="black.TLabel")
l3.grid(row=1,column=0)

l4 = ttk.Label(window, text="ISBN", style="black.TLabel")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row=1,column=3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand= sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = ttk.Button(window, text="View all", width=12, command = view_command, style = "blue/white.TButton")
b1.grid(row=2, column=3)

b2 = ttk.Button(window, text="Search entry", width=12, command = search_command, style = "blue/white.TButton")
b2.grid(row=3, column=3)

b3 = ttk.Button(window, text="Add entry", width=12, command = add_command, style = "blue/white.TButton")
b3.grid(row=4, column=3)

b4 = ttk.Button(window, text="Update", width=12, command = update_command, style = "blue/white.TButton")
b4.grid(row=5, column=3)

b5 = ttk.Button(window, text="Delete", width=12, command = delete_command, style = "blue/white.TButton")
b5.grid(row=6, column=3)

b6 = ttk.Button(window, text="Exit", width=12, command=window.destroy, style = "blue/white.TButton")
b6.grid(row=7, column=3)


window.mainloop()
