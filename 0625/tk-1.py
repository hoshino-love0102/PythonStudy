from tkinter import *
window = Tk()

label = Label(window, text="Hello World")
label.pack()

window.mainloop()

# TK_4
from tkinter import *
window = Tk()

lal1 = Label(window, text="이것은 레이블입니다.")
lal2 = Label(window, text = "문자를", font = ("궁서체", 20, "bold"))
lal3 = Label(window, text = "출력하는", bg = "yellow", fg = "red", anchor="w")
lal4 = Label(window, text = "위젯입니다.", width = 20, height = 3, bg = "skyblue", anchor = "se")

lal1.pack()
lal2.pack()
lal3.pack()
lal4.pack()

window.mainloop()