from tkinter import *

def add():
    a = int(ent1.get())
    b = int(ent2.get())
    lbl1["text"] = a + b

window = Tk()

ent1 = Entry(window)
ent2 = Entry(window)
lbl1 = Label(window)
btn1 = Button(window, text="더하기", command=add)

ent1.pack()
ent2.pack()
lbl1.pack()
btn1.pack()

window.mainloop()
