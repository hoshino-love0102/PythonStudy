from tkinter import *
window = Tk()

lal1 = Label(window, text="레이블입니다.")
btn1 = Button(window, text = "1번 버튼")
btn2 = Button(window, text = "2번 버튼")

lal1.pack()
btn1.pack()
btn2.pack()

window.mainloop()