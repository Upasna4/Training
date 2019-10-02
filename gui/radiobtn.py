import tkinter as t
from tkinter import messagebox

root = t.Tk()
value = t.StringVar()
r_button = t.Radiobutton(root,text="male",variable=value,value="male")
r_button.grid(row=0,column=0)

r_button = t.Radiobutton(root,text="female",variable=value,value="female")
r_button.grid(row=0,column=1)

def select():
    get_value = value.get()
    if get_value == "male":
        messagebox.showinfo("Gender","male selected")
    elif get_value == "female":
        messagebox.showinfo("Gender", "female selected")

show = t.Button(root,text="Show",command=select)
show.grid(row=1,column=0)


root.mainloop()




