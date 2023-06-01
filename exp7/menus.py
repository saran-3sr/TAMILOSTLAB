from tkinter import *
top=Tk()
def newwindow():
    neww=Toplevel()
    b=Label(newwindow,text="New WIndow ")
    newwindow.mainloop()
menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label='New',command=newwindow)
file.add_command(label='open')
file.add_separator()
menubar.add_cascade(label= 'file',menu=file)
top.config(menu=menubar)
top.mainloop()
