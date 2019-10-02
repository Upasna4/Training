from tkinter import ttk,messagebox
import tkinter as t


def get_value():
    data=value.get()
    messagebox.showinfo("City",data)
root=t.Tk()
value=t.StringVar()
box=ttk.Combobox(root,textvariable=value,state='readonly')
box['values']=('Select City','Chd','Pune','Delhi','Goa')
box.current(0)
box.grid(column=0,row=0)
button1=t.Button(root,text="Show",command=get_value)
button1.grid(column=0,row=1)
root.mainloop()