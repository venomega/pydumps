import curses
import time
import win
import time
import threading as t
import memory


def delay(ms):
        for i in range(25000000 * ms):
                pass


class monitor(win.window):
    def __init__(self):
        super().__init__(0.5, 0.8, 0.1, 0.1)
        self.build()

    def loop(self):
        status = len(self.buffer)
        while True:
            if len(self.buffer) != status or self.changed:
                self.write_buffer()
                self.notch()
                status = len(self.buffer)
                self.changed = False
            #    self.write(10,1,str(self.buffer))
            #delay(1)
            time.sleep(1)
            #self.refresh()


class cmd(win.window):
    def __init__(self):
        super().__init__(0.2, 0.8, 0.70, 0.1)
        self.build()

    def loop(self):
        buffer = ""
        while True:
            key = self.win.getch()
            if key in [curses.KEY_ENTER, 10]:
                memory.bridge[0].buffer_add(buffer)
                buffer = ""
            if key in [x for x in range(97,123)]:
                buffer += key.to_bytes(1, 'little').decode()
            if key in [x for x in range(48,58)]:
                buffer += key.to_bytes(1, 'little').decode()
            if key == 32:
                buffer += " "
            if key in [curses.KEY_BACKSPACE, 127]:
                buffer = buffer[:-1]
            if key == 65:
                memory.bridge[0].up_marging()
            if key == 66:
                memory.bridge[0].down_marging()
            self.clean()
            self.write(1, 1, buffer)
            



def mon_handler():
    o = monitor()
    memory.bridge.append(o)
    #win.l[0].buffer.append("sadasdasd")
    #o.write(1, 1, str(win.h))
    t.Thread(target=memory.bridge[0].loop).start()


def input_handler():
    o = cmd()
    o.loop()
 


def a(screen):
    cols = curses.COLS
    lines = curses.LINES
    mon_handler()

    input_handler()

    time.sleep(5)

curses.wrapper(a)