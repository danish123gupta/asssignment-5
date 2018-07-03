import tkinter as tk
r= tk.Tk()
r.title("counting seconds")
def hello():
    print("hello")
button = tk.Button(r,text='Stop',width = 25,command=r.hello)
button.pack()
r.mainloop()