from tkinter import *
w=Tk()
l1=Label(text="n1")
l1.grid(row=0, column=0)
e1=Entry()
e1.grid(row=0, column=1)
l2=Label(text="n2")
l2.grid(row=1, column=0)
e2=Entry()
e2.grid(row=1, column=1)

b1=Button(text="Add",command="add")
b1.grid(row=2,column=1)
e3=Entry()
e3.grid(row=2,column=1)

def add():
    sum=int(e1.get()+int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,sum)
    
    