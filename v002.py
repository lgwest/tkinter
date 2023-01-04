from tkinter import *

root = Tk()

# alternative way, fuluent style
#mylabel1 = Label(root, text="Hello World").grid(row=0, column=0)
#mylabel2 = Label(root, text="Hello again").grid(row=1, column=1)

mylabel1 = Label(root, text="Hello World")
mylabel2 = Label(root, text="Hello again")

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)

root.mainloop()

