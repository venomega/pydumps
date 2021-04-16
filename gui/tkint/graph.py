from tkinter import *
import tkinter.messagebox


class Func(Canvas):
    def __init__(self, frame, **kwords):
        if 'width' in kwords.keys():
            self.width = kwords["width"]
            self.height= kwords["height"]
            super().__init__(frame, kwords)
        else:
            Canvas(frame, kwords)
        
        self.build()

    def build(self):
        #draw y
        self.create_line(self.width//2, 0, self.width//2, self.height)
        #draw x
        self.create_line(0, self.height//2 , self.width, self.height//2)

        self.entry = Entry(root)
        self.entry.grid(row=1, column=0, columnspan=2)
        self.button = Button(text="Graph", command=self.on_press)
        self.button.grid(row=1, column=2)

    def clean(self):
        self.string = self.entry.get()
        self.entry.delete(0, len(self.string))
        self.delete(ALL)
        self.build()

    def on_press(self):
        self.clean()
        self.ords=[]
        for i in range(-10, 11):
            x = i
            y = eval(self.string)
            self.ords.append((x, y))
        self.graph()

    def graph(self):
        prev=self.ords[0]
        for i in range(1,len(self.ords)):
            x1, y1 = prev
            x2, y2 = self.ords[i]
            self.create_line(
                self.width/2 + x1 * 10,
                self.height/2 - y1,
                self.width/2 + x2 * 10,
                self.height/2 - y2,
                fill="red")
            prev = (x2, y2)


if __name__ == "__main__":
    root = Tk()

    o = Func(root, width=200, height=200)
    o.grid(row=0, column=0, columnspan=3)
    root.mainloop()
    
