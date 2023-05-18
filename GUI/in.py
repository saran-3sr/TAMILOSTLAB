from tkinter import * 
root=Tk()
def on_press():
    b2=Button(root,text="Exit")
    b2.pack(side="top")
b1=Button(root,text="Hello",command=on_press)
l1=Label(text="Hello just checking idiot").pack(side="left")
b1.pack(side="top")
root.geometry("500x500")
root.mainloop()