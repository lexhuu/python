from tkinter import *
from tkinter import messagebox
import sqlite3
con= sqlite3.connect("database.db")
w= Tk()
def r():
    w1=Tk()
    def db():
        u=e1.get()
        p=e2.get()
        con.execute("INSERT INTO register values (?,?)",(u,p))
        con.commit()
        messagebox.showinfo("Register","Success")
        w1.destroy()
    l1=Label(w1,text="Username")
    e1=Entry(w1,width=20)
    l2=Label(w1,text="Password")
    e2=Entry(w1,width=20)
    l1.grid()
    e1.grid()
    l2.grid()
    e2.grid()
    reg1= Button(w1, text="Create", command=db)
    reg1.grid(row=3, column=1)
    mainloop()

def l():
    w2= Tk()
    def f():
        u=e1.get()
        p=e2.get()
        k=con.execute("SELECT * FROM register where Username= ? AND Password= ?",(u,p))
        for i in k:
            messagebox.showinfo("Login","Success")
            break
        else:
            messagebox.showinfo("Login","Invalid")
        w2.destroy()
    l1=Label(w2, text="Username")
    e1=Entry(w2, width=20)
    l2=Label(w2, text="Password")
    e2=Entry(w2, width=20)
    l1.grid() 
    e1.grid()
    l2.grid()
    e2.grid()
    lg2= Button(w2, text="Login", command=f)
    lg2.grid(row=3, column=1)
    mainloop()

ug= Button(w, text="Register", command=r)
lg= Button(w, text="Login", command=l)

ug.grid()
lg.grid()
mainloop() 