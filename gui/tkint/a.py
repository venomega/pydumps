from tkinter import *
import tkinter.messagebox

def notify(string="Info of The Heaven"):
    tkinter.messagebox.showinfo("Info of The Heaven", string)

f1 = Tk()
l1 = Label(f1, text="Username")
l1.grid(row=0)
e1 = Entry(f1)
e1.grid(row=0, column=1)
l2 = Label(f1, text="Password")
l2.grid(row=1)
e2 = Entry(f1)
e2.grid(row=1,column=1)
c = Checkbutton(text="Remember me")
c.grid(row=2, columnspan=3)
b1 = Button(f1, text="Info of The Heaven", command=notify)
b1.grid(row=3, columnspan=3)


canvas = Canvas(f1, width=200, height=200)
canvas.grid(row=4, rowspan=3, columnspan=3)
canvas.create_line(200/2,0,200/2,200)



f1.mainloop()