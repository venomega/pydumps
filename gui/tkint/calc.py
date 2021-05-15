from tkinter import *

#Entry()

class Calc(Tk):
    def __init__(self, width=300, height=450):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.build()

    def build(self):
        entry = Entry( font="serif 24", bg="black", fg="white")
        entry.grid(row=0,column=0, columnspan=4)
        buttons= {"7":1, "8":1, "9":1, "+":2,
                "4":1, "5":1, "6":1, "-":2,
                "1":1, "2":1, "3":1, "*":2,
                "0":0, "=":3}
        row = 1
        column=0
        
        for i in buttons.keys():
            if buttons[i] == 1:
                token = Button(text=i, bg="black",fg="white", font="serif 12")
                token.grid(row=row, column=column)
                column+=1
            if buttons[i] == 2:
                token = Button(text=i, bg="black",fg="white", font="serif 12")
                token.grid(row=row, column=column)
                row+=1
                column=0
            if buttons[i] == 0:
                token = Button(text=i, bg="black",fg="white", font="serif 12")
                token.grid(row=row,column=column, columnspan=3)
                column=4
            if buttons[i] == 3:
                token = Button(text=i, bg="black",fg="white", font="serif 12")
                token.grid(row=row, column=3)
        



o = Calc()
o.mainloop()