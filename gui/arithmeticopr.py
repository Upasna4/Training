import tkinter as t
from tkinter import messagebox

root = t.Tk()


def opr():
    val1 = text.get()
    val2 = text1.get()
    button = submit['text']
    if button == 'Addition':
        data = int(val1) + int(val2)
        #submit.insert(0,result)
        result['text'] = data
        submit['text'] = 'Subtraction'
    elif button == 'Subtraction':
        data = int(val1) - int(val2)
        #submit.insert(0,result)
        result['text'] = data
        submit['text'] = 'Multiplication'
    elif button == 'Multiplication':
        data = int(val1) * int(val2)
        #submit.insert(0, result)
        result['text'] = data
        submit['text'] = 'Division'
    elif button == 'Division':
        data = int(val1) / int(val2)
        #submit.insert(0, result)
        result['text'] = data
        submit['text'] = 'exit'
    elif button == 'exit':
        exit()


# def addition():
#     val1 = text.get()
#     val2 = text1.get()
#     data = int(val1) + int(val2)
#     result['text'] = data
#     submit.configure(text="Subtraction",command=subtraction)


# def subtraction():
#     val1 = text.get()
#     val2 = text1.get()
#     data = int(val1) - int(val2)
#     result['text'] = data
#     submit.configure(text="Multiplication", command=multiplication)


# def multiplication():
#     val1 = text.get()
#     val2 = text1.get()
#     data = int(val1) * int(val2)
#     result['text'] = data
#     submit.configure(text="Division", command=division)


# def division():
#     val1 = text.get()
#     val2 = text1.get()
#     data = int(val1) % int(val2)
#     result['text'] = data
#     submit.configure(text="Exit", command=exit)




root.geometry("750x650")
root.title("ARITHMETIC OPERATIONS")
root.iconbitmap(r"C:\Users\hp\Downloads\logo1.ico")
root.resizable(0,0)
root.configure(bg="red")

msg1 = t.Label(root,text="First Value",font="arial 20 bold underline italic",bg="red",fg="yellow")
msg1.grid(row=1,column=0)

text = t.Entry(root,font="arial 20 bold")
text.grid(row=1,column=1)

msg2 = t.Label(root,text="Second Value",font="arial 20 bold underline italic",bg="red",fg="yellow")
msg2.grid(row=2,column=0)

text1 = t.Entry(root,font="arial 20 bold")
text1.grid(row=2,column=1)

msg3 = t.Label(root,text="Result",font="arial 20 bold underline italic",bg="red",fg="yellow")
msg3.grid(row=3,column=0)

result = t.Label(root,text="result",font="arial 20 bold")
result.grid(row=3,column=1)

submit = t.Button(root, text="Addition",command=opr,font="tahoma 20 bold")
submit.grid(row=4,column=1)

#submit = t.Button(root,text="Subtraction",command=subtraction,font="tahoma 20 bold")
#submit.grid(row=4,column=1)

#submit = t.Button(root,text="Multiplication",command=multiplication,font="tahoma 20 bold")
#submit.grid(row=4,column=1)

#submit = t.Button(root,text="Division",command=division,font="tahoma 20 bold")
#submit.grid(row=4,column=1)


root.mainloop()