from tkinter import *

window = Tk()

lbl1 = Label(window, text="레이블입니다")
btn1 = Button(window, text="첫번째 버튼")
btn2 = Button(window, text="두번째 버튼")

lbl1.pack()
btn1.pack(side=LEFT, padx=10)
btn2.pack(side=LEFT, padx=10)

btn1["text"] = "One"
btn2["text"] = "Two"

btn1.config(text="One")

window.mainloop()
