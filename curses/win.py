import curses


class window():
    def __init__(self, h=0, w=0, y=0, x=0):
        count = 0
        ww = curses.COLS
        hh = curses.LINES
        #if there is a float on [h, w]
        if type(float()) in [type(h), type(w)]:
            self.x = int(ww * x)
            self.y = int(hh * y)
            self.h = int(hh * h)
            self.w = int(ww * w)
        else:
            self.x = int(x)
            self.y = int(y)
            self.w = int(w)
            self.h = int(h)

    def refresh(self):
        """
        Update the window content
        """
        self.win.refresh()

    def build(self):
        """
        Create the window with borders
        """
        self.win = curses.newwin(self.h, self.w, self.y, self.x)
        self.win.border()
        self.refresh()

    def write(self, y, x, string):
        """
        Write a string to the screen
        """
        self.win.addstr(y, x, string)
        self.refresh()

    def clean(self):
        """
        Clean the whole screen
        """
        lock = 0
        for i in range(self.h - 1):
            if lock == 0:
                lock = 1
                continue
            self.write(i, 1, " "*(self.w - 2))

    def notch(self):
        """
        Change the cursor to the start of the window
        """
        self.write(0, 0, "")

    def scroll_on(self):
        """
        Enable window for scroll
        """
        self.win.scrollok(True)
        self.win.idlok(True)

    def scroll_off(self):
        """
        Disable window for scroll
        """
        self.win.scrollok(False)
        self.win.idlok(False)


