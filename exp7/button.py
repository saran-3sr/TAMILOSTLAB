from tkinter import *
root=Tk()
def callback():
    print("clicked ok")
a=Label(root,text='hello world')
b=Button(root,text='ok',command=callback)
a.pack()
b.pack()
root.mainloop()