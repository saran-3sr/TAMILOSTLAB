from tkinter import *
root=Tk()
menubar=Menu(root)
file=Menu(menubar,tearoff=0)
file.add_command(label="File")
file.add_command(label="open")
file.add_separator()
menubar.add_cascade(label="FIle",menu=file)
root.config(menu=menubar)
root.mainloop()