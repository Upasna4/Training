import tkinter as t
from tkinter import messagebox

root = t.Tk()
root.title("check box gui")
root.geometry("200x200")

def show():
    if var1.get() == 1:
        messagebox.showinfo("selected",chk1['text'])
    elif var1.get() == 1:
        messagebox.showinfo("selected",chk2['text'])
    elif var1.get() == 1:
        messagebox.showinfo("selected",chk3['text'])


var1 = t.IntVar()
chk1 = t.Checkbutton(root,text="mtech",variable=var1)
chk1.grid(row=0,column=0)

var2 = t.IntVar()
chk2 = t.Checkbutton(root,text="btech",variable=var2)
chk2.grid(row=1,column=0)

var3 = t.IntVar()
chk3 = t.Checkbutton(root,text="mba",variable=var3)
chk3.grid(row=2,column=0)

output = t.Button(root,text="Check Select",command=show)
output.grid(row=3,column=0)


root.mainloop()