from tkinter import *

def change_text():
    button["text"] = "버튼이 클릭됨"

window = Tk()
button = Button(window, text="클릭", command=change_text)
button.pack()

window.mainloop()