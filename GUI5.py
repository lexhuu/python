from tkinter import *
master = Tk()

Label(master, text= "first").grid(row=0,sticky= N)
Label(master, text= "Second").grid(row=1,sticky=W)

e1= Entry(master)
e2= Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()