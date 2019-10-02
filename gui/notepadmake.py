import tkinter as t
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, \
    asksaveasfilename
# import ntpath


# def open_file():
#     filename = askopenfilename()
#     with open(filename, "r") as f:
#         data = f.read()
#
#     text.insert("1.0", data)
#     path, name = ntpath.split(filename)
#     fn, ext = name.split(".")
#     root.title(fn+" - Notepad")

def terminate():
    data = text.get("1.0", "end")
    if len(data) == 1:
        exit()
    else:
        return_value = messagebox.askyesnocancel\
            ("Notepad", "Confirm")
        if return_value is True:
            exit()
        elif return_value is False:
            filename = asksaveasfilename()+".txt"
            with open(filename, "w") as f:
                f.write(data)
            exit()


root = t.Tk()
root.title("Untitled - Notepad")
root.geometry("300x300")

mainMenu = t.Menu(root)
subMenu = t.Menu(mainMenu)
root.config(menu=mainMenu)

mainMenu.add_cascade(label="File", menu=subMenu)
# mainMenu.add_cascade(label="Edit")
# mainMenu.add_cascade(label="Format")
# mainMenu.add_cascade(label="View")
# mainMenu.add_cascade(label="Help")

subMenu.add_command(label="New",  accelerator="Ctrl + N")
subMenu.add_command(label="Open",accelerator="Ctrl + O")
subMenu.add_separator()
subMenu.add_command(label="Save", accelerator="Ctrl + S")
subMenu.add_command(label="Save As",  accelerator="F12")
subMenu.add_separator()
subMenu.add_command(label="Exit", command=terminate,  accelerator="Alt + F4")
# subMenu.add_command(label="Page Setup")
# subMenu.add_command(label="Print")
#
# subMenu.add_separator()
#

text = t.Text(root, height=30, width=30)
text.place(x=0, y=0, relheight=1, relwidth=1)

# root.bind('<Control-o>', lambda event: open_file())

root.mainloop()
