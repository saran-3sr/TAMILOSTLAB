from tkinter import * 
root=Tk()
def on_press():
    b2=Button(root,text="Exit")
    b2.pack(side="top")
b1=Button(root,text="Hello",command=on_press)
b1.pack(side="top")
root.geometry("500x500")
root.mainloop()