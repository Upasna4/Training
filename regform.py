import tkinter as t
root = t.Tk()


def register():
    val1 = text.get()
    val2 = text1.get()
    val3 = text2.get()


root.geometry("750x650")
root.title("REGISTRATION FORM")
root.configure(bg="red")
heading = t.Label(root,text="REGISTRATION FORM",font="arial 30 bold underline italic",bg="yellow",fg="black")
heading.grid(padx=10,pady=10,row=0,column=0)

name = t.Label(root,text="NAME",font="arial 20 bold italic",fg="black")
name.grid(row=1,column=0)

text = t.Entry(root,font="arial 20 bold")
text.grid(row=1,column=1)

email = t.Label(root,text="EMAIL",font="arial 20 bold italic",fg="black")
email.grid(row=2,column=0)

text1 = t.Entry(root,font="arial 20 bold")
text1.grid(row=2,column=1)

gender = t.Label(root,text="GENDER",font="arial 20 bold  italic",fg="black")
gender.grid(row=3,column=0)

text2 = t.Entry(root,font="arial 20 bold")
text2.grid(row=3,column=1)

submit = t.Button(root,text="REGISTER",command=register,font="tahoma 20 bold")
submit.grid(row=4,column=1)



root.mainloop()
