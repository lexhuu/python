import sqlite3
from tkinter import *

def register_user():
    username= username_entry.get()
    password= password_entry.get()
    
    conn=sqlite3.connect('database.db')
    c= conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    
    conn.commit()
    conn.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    status_label.config(text= "Registration Successfull !")

root=Tk()
root.title("Registration Form")

Label(root, text="Username:").pack()
username_entry= Entry(root)
username_entry.pack()

Label(root, text="Password:").pack()
password_entry= Entry(root, show="*")
password_entry.pack()

register_button = Button(root, text="Register", command=register_user)
register_button.pack()

status_label = Label(root, text="")
status_label.pack()

root.mainloop()