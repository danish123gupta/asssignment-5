from tkinter import *
top=Tk()
mb= Menubutton(top,text="menu")
mb.grid()
mb.menu = Menu(mb,tearoff=0)
mb['menu']= mb.menu
cVar=IntVar()
aVar=IntVar()
mb.menu.add_checkbutton(label ='contact',variable=cVar)
mb.menu.add_checkbutton(label ='about',variable=aVar)
mb.pack()
top.mainloop()


from tkinter import *
root= Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='file',menu =filemenu)
filemenu.add_command(label="new")
filemenu.add_command(label="open")
filemenu.add_separator()
filemenu.add_command(label='exit',command=root.quit)
helpmenu= Menu(menu)
menu.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='about')
root.mainloop()




from tkinter import *
root = Tk()
root.title('ruby')
top= Toplevel()
top.title('dan')
top.mainloop()



from tkinter import *
master = Tk()
w = Spinbox(master,from_=0,to=10)
w.pack()
mainloop()


from tkinter import *
m1=PanedWindow()
m1.pack(fill=BOTH,expand=1)
left=Entry(m1,bd=5)
m1.add(left)
m2=PanedWindow(m1,orient=VERTICAL)
m1.add(m2)
top=Scale(m2,orient=HORIZONTAL)
m2.add(top)
mainloop()


from tkinter import *
from tkinter import messagebox
top= Tk()
def helloCallBack():
    msg= messagebox.showinfo("gupta","kingdom")
B = Button (top,text="hello",command= helloCallBack)
B.place(x=50,y=100)
top.mainloop()