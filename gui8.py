from tkinter import *
w=Tk()
l1=Label(text="UserName")
l1.grid(row=0, column=0)
e1=Entry()
e1.grid(row=0, column=1)
l2=Label(text="Password")
l2.grid(row=1, column=0)
e2=Entry()
e2.grid(row=1, column=1)

l3=Button(text="Register")
l3.grid(row=2,column=1)
def click():
    if e1.get()== "admin" and  e2.get()=="<PASSWORD>":
        import sqlite3
        con=sqlite3.connect("database.db")
        print("connection established")
        con.execute("CREATE TABLE HOSPITAL (EmployeeID int primary key, Ename varchar(20), DeptID int, Salary int, Dname varchar(20), Dlocation varchar(30))")
        con.execute("INSERT INTO HOSPITAL VALUES (7,'Alice',3,3500,'FINANCE','Mumbai')")
        for i in x:
            print(i)
        con.commit()
        con.close()
w.mainloop()
