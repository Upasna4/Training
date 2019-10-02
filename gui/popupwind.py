import tkinter as t
from tkinter import messagebox
#messagebox.showinfo("Show Info","hello world")
#vall=messagebox.showinfo("Show Info","hello world")
#print(vall)

#messagebox.showerror()
#messagebox.showerror("Show Info","hello world")

#messagebox.showwarning("Show Info","hello world")
check = messagebox.askokcancel("Show Info","hello world")
print(check)
# messagebox.askyesno()
# messagebox.askyesnocancel()
# messagebox.askretrycancel()
# messagebox.askquestion()

root=t.Tk()
root.title("Pop Up Window")
root.geometry("500x500")
root.resizable(0,0)

text=t.Entry(root,text="click to show")
text.grid(row=1,column=0)

root.mainloop()