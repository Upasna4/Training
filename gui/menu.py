import tkinter as t     # from tkinter import *
import ntpath       # from tkinter.filedialog import*
from tkinter.filedialog import askopenfilename, asksaveasfilename


#print(root.wm_title())
def undofun():
    mytext1.config(font = ("Arial",10,"bold"))
    mytext1.config(font = ("Arial",10,"underline"))
    mytext1.config(font = ("Arial",10,"italic"))
    mytext1.tag_add("start", "1.0", "end")
    mytext1.tag_config("start", background="red",
    foreground="yellow")
    mytext1.configure(autoseparators=True, maxundo=-1)
    mytext1.edit_undo()

def kill():

    root.destroy()

def clear():

    mytext1.delete(1.0 , 'END')

def copy():
    mytext1.clipboard_clear()
    mytext1.clipboard_append(mytext1.selection_get())

def paste():
    try:
        teext = mytext1.selection_get(selection='CLIPBOARD')
        mytext1.insert(t.INSERT, teext)
    except:
        pass
        #print("error")
        #tkMessageBox.showerror("Errore","Gli appunti sono vuoti!")

def NewFile():
    print ("New File!")


def OpenFile():
    #titlefile=root.wm_title()
    name = askopenfilename()#initialdir="")
    f = open(name,'r')
    text = f.read()
    f.close()

    mytext1.insert('1.0', text)
    full_path, file_name_wx = ntpath.split(name)
    fn, ext = file_name_wx.split(".")
    root.title(fn + " - Notepad")


def saveFile():
    filename = asksaveasfilename()
    if filename:
        a=open(filename, 'w')
        b=mytext1.get("1.0","end")
        a.write(b)
        a.close()

def About():
    print ("This is a simple example of a menu")


root = t.Tk()
root.title("Untitled - Notepad")

menu_obj = t.Menu(root)
root.config(menu=menu_obj)

file_menu = t.Menu(menu_obj)

menu_obj.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=NewFile, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=OpenFile, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=saveFile, accelerator="Ctrl+S")

def truncate():
    exit()


file_menu.add_command(label="Exit", command=exit, accelerator="Alt+X")

# filemenu.add_command(label="SaveAs...")
# filemenu.add_separator()
#
#
#
#
# filemenu.add_command(label="Exit", command=root.quit)
#
# helpmenu = t.Menu(menuobj)
# menuobj.add_cascade(label="Help", menu=helpmenu)
# helpmenu.add_command(label="About...", command=About)
#
# editmenu = t.Menu(menuobj)
# menuobj.add_cascade(label="Edit", menu=editmenu)
# editmenu.add_command(label="Undo...", command=undofun)
# editmenu.add_command(label="Cut...", command=About)
# editmenu.add_command(label="Copy...", command=copy)
# editmenu.add_command(label="Paste...", command=paste)
# editmenu.add_command(label="Del...", command=clear)


mytext1 = t.Text(root, undo=True, width=30, height=5)
mytext1.place(x=0, y=0, relwidth=1, relheight=1)


root.bind('<Control-o>', lambda event: OpenFile())

root.mainloop()
