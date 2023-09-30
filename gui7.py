from tkinter import *
master = Tk()


label1=Label(text="Enter first number")
label1.grid(sticky=E)
e1=Entry()
e1.grid(row=0, column=1)
label2=Label(text="Enter second number")
label2.grid(sticky=E)
e2=Entry()
e2.grid(row=1, column=1)

e3=Entry(text="0")
e3.grid(row=3, column=1)

def add():
    sum= (int(e1.get())+int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,sum)
def sub():
    min= (int(e1.get())-int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,min)
def mul():
    prod= (int(e1.get())*int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,prod)
def div():
    div= (int(e1.get())/int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,div)
b1=Button(text="Add", command=add)
b1.grid(row=2, column=1)
b2=Button(text="Sub", command=sub)
b2.grid(row=2, column=2)
b3=Button(text="Mul", command=mul)
b3.grid(row=2, column=3)
b4=Button(text="Div", command=div)
b4.grid(row=2, column=4)
master.mainloop()