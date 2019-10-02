import tkinter as t

root = t.Tk()
root.title("Tik Tak  Toe")
root.geometry("240x300")
root.resizable(0, 0)

b1 = t.Button(root, height=5, width=10)
b1.grid(row=0, column=0)

b2 = t.Button(root, height=5, width=10)
b2.grid(row=0, column=1)

b3 = t.Button(root, height=5, width=10)
b3.grid(row=0, column=2)

b4 = t.Button(root, height=5, width=10)
b4.grid(row=1, column=0)

b5 = t.Button(root, height=5, width=10)
b5.grid(row=1, column=1)

b6 = t.Button(root, height=5, width=10)
b6.grid(row=1, column=2)

b7 = t.Button(root, height=5, width=10)
b7.grid(row=2, column=0)

b8 = t.Button(root, height=5, width=10)
b8.grid(row=2, column=1)

b9 = t.Button(root, height=5, width=10)
b9.grid(row=2, column=2)

res = t.Button(root, text="Reset", height=2, width=10)
res.grid(sticky="W")

ex = t.Button(root, text="Exit", height=2, width=10)
ex.grid(row=3, column=2)

root.mainloop()
