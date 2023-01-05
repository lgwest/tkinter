# video 004
from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0, "enter your name")

def myClick():
    mylabel = Label(root, text=e.get())
    mylabel.pack()

myButton = Button(root, text='Enter your name', command=myClick)
myButton.pack()

root.mainloop()

