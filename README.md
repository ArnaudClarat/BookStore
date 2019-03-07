# BookStore
A program that store some books. In python with sqlite3 and Tkinter

## What I learned
the use of tkinter

## What it does
the user can create his bookstore that allows him to store a list of books in the database

It stores an id, the title, the author's name, the year of publication, the isbn number

The user can add a new book in the list, update the informations of a book, delete a book, view all the books
and also looking for one or all the informations.

## What to do next
- [ ] clean the code
- [ ] error handling
- [ ] delete the global variable (?)
- [ ] bug management

## how to create an executable
>pip install pyinstaller

>pyinstaller --onefile --windowed bookstore.py
