from tkinter import *
top=Tk()
menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label='New')
file.add_command(label='open')
file.add_separator()
menubar.add_cascade(label= 'file',menu=file)
top.config(menu=menubar)
top.mainloop()
