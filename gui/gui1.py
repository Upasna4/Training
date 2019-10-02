import tkinter as t
root = t.Tk()    #cls ka obj bnaya..instance is creatd when we make obj
def addition():
    val1 = text.get()
    val2 = text1.get()
    data = int(val1) + int(val2)
    #result.config(state=t.NORMAL)
    result['text'] = data
    #result.delete(0,t.END)
    #result.insert(0)
    #result.config(state="disabled")

root.geometry("750x650")   #width aur height dena  .GEOMETRY IS METHOD
root.title("GUI Application")     #.TITLE IS METHOD  yha title dia
root.iconbitmap(r"C:\Users\hp\Downloads\logo1.ico")
root.resizable(0,0)    #to give fixe size..not it will not maximize
root.configure(bg="red")        #to give background color
heading = t.Label(root,text="GUI Window",font="arial 50 bold underline italic",bg="green",fg="black")
heading.grid(padx=10,pady=10,row=0,column=0)

msg1 = t.Label(root,text="First Value",font="arial 20 bold underline italic",bg="green",fg="black")
msg1.grid(row=1,column=0)

text = t.Entry(root,font="arial 20 bold")
text.grid(row=1,column=1)

msg2 = t.Label(root,text="Second Value",font="arial 20 bold underline italic",bg="green",fg="black")
msg2.grid(row=2,column=0)

text1 = t.Entry(root,font="arial 20 bold")
text1.grid(row=2,column=1)

msg3 = t.Label(root,text="Result",font="arial 20 bold underline italic",bg="green",fg="black")
msg3.grid(row=3,column=0)

result = t.Label(root,text="result",font="arial 20 bold")
result.grid(row=3,column=1)

submit = t.Button(root,text="Addition",command=addition,font="tahoma 20 bold")
submit.grid(row=4,column=1)


root.mainloop()    #window is created #mainloop se usko show kraya