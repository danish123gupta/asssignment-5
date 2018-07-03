#q.no.1
"""
from tkinter import *
from tkinter import messagebox
top= Tk()
top.geometry("100x100")
def helloCallBack():
    msg= messagebox.showinfo("Hello Python","Hello World")
B = Button(top,text ="Quit",command = quit).pack()
B = Button (top,text="hello",command= helloCallBack)
B.place(x=50,y=100)
top.mainloop()"""

#q.no.2
from tkinter import *
from tkinter import messagebox
top= Tk()
top.geometry("100x100")
def clicked():
    msg= messagebox.showinfo("gupta","cool")
B = Button (top,text="click me",command= clicked)
B.place(x=50,y=50)
top.mainloop()


#q.no.3
from tkinter import *
top = Tk()
top.title("welcome")
top.geometry('350x200')
def display():
    lbl.configure(text="i love u")
lbl=Label(top,text="dent")
lbl.pack(side="top")
btn1=Button(top,text="change text",command=display)
btn1.place(x=50,y=50)
btn= Button(top,text="exit",command=exit)
btn.place(x=10,y=20)
top.mainloop()



#q.no.4
from tkinter import *
def show_entry_fields():
    print("first name: %s\nlast name: %s"%(a1.get(),a2.get()))
dan= Tk()
Label(dan,text="first name").grid(row=0)
Label(dan,text="lastname").grid(row=1)
a1= Entry(dan)
a2= Entry(dan)
a1.grid(row=0,column=1)
a2.grid(row=1,column=1)
Button(dan,text="Show",
command=  show_entry_fields()).grid(row=3,column=1,sticky=W,pady=4)
mainloop()




