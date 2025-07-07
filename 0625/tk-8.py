from tkinter import *

def print_1():
    lbl1.config(text="첫 번째 버튼 클릭.")

def print_2():
    lbl1.config(text="두 번째 버튼 클릭.")

window = Tk()

lbl1 = Label(window, text="결과 출력 레이블")
btn1 = Button(window, text="One", command=print_1)
btn2 = Button(window, text="Two", command=print_2)

lbl1.pack()
btn1.pack()
btn2.pack()

window.mainloop()