from tkinter import *
top=Tk()
top.geometry("400x400")
w=Text(top,height=1,width=10)
w.insert(INSERT,"Hello world")
w.grid(row=0,column=1)
name=Label(top,text="Name").grid(row=1,column=0)
e1=Entry(top).grid(row=1,column=1)
password=Label(top,text="Password").grid(row=2,column=0)
e1=Entry(top).grid(row=2,column=1)
submit=Button(top,text="Submit").grid(row=4,column=0)
exit=Button(top,text="Exit",command=top.destroy).grid(row=4,column=1)
top.mainloop()