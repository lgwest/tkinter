# v003
from tkinter import *

root = Tk()

def myClick():
    mylabel = Label(root, text="Look I clicked a button!!")
    mylabel.pack()

#myButton = Button(root, text='Click me!', state=DISABLED)
#myButton = Button(root, text='Click me!', padx=50, pady=30)
myButton = Button(root, text='Click me!', 
                command=myClick, bg="yellow", fg="#ff0000")
myButton.pack()

root.mainloop()

