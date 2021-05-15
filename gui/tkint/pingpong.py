from tkinter import *

WIDTH = 800
HEIGHT = 600


root = Tk()
o = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
o.pack()

class Rectangle():
    def __init__(self):
        self.x1 = 0
        self.x2 = 40
        self.y1 = 0
        self.y2 = 100

    def offsetY(self, num):
        self.y1 += num
        self.y2 += num

    def offsetX(self, num):
        self.x1 += num
        self.x2 += num


class Player(Rectangle):
    def __init__(self):
        super().__init__()

p1 = Player()
"HEIGHT//2 - ((r_size.y1 + r_size.y2)//2)"
o.create_rectangle(p1.x1, p1.y1, p1.x2, p1.y2, fill="red")
print (

exit(0)

root.bind("<w>", lambda x: r_size.offsetY(-20))
root.bind("<s>", lambda x: r_size.offsetY(+20))

root.mainloop()