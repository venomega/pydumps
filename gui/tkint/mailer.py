from tkinter import *

root = Tk()

l = Listbox(root)
l.pack()
root.bind("<a>",func=lambda x: print(x))
grid = Frame(l)
grid.pack()

label = Label(l,text="john")
label.pack()

label2 = Label(grid, text="grid")
label2.grid(row=0)

pi = PhotoImage(file="rss-custom.png")
label3 = Button(root, text="Buy", font="serif 18", bg="green",)
label3.pack()


root.mainloop()