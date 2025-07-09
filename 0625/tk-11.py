from tkinter import *

root = Tk()
root.title("배치관리자")
root.geometry("300x200")

# Label로 변경
btn_1 = Label(root, text="(0,0)", bg="green")
btn_2 = Label(root, text="(0,1)", bg="red")
btn_3 = Label(root, text="(0,2)", bg="blue")

btn_4 = Label(root, text="(1,0)", bg="gray")
btn_5 = Label(root, text="(1,1)", bg="yellow")
btn_6 = Label(root, text="(1,2)", bg="pink")

btn_7 = Label(root, text="(2,0)", bg="purple")
btn_8 = Label(root, text="(2,1)", bg="orange")
btn_9 = Label(root, text="(2,2)", bg="cyan")

btn_10 = Label(root, text="(3,0)", bg="royalblue")
btn_11 = Label(root, text="(3,1)", bg="beige")
btn_12 = Label(root, text="(3,2)", bg="brown")

widgets = [
    btn_1, btn_2, btn_3,
    btn_4, btn_5, btn_6,
    btn_7, btn_8, btn_9,
    btn_10, btn_11, btn_12
]

for i, widget in enumerate(widgets):
    row = i // 3
    col = i % 3
    widget.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# 행, 열 weight
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=3)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=3)

root.mainloop()
