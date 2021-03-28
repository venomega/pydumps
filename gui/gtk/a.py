import gi
import threading as t
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class window():
    def __init__(self):
        self.w = 300
        self.h = 300
        self.win = Gtk.Window()
        self.win.show()
        self.resize(self.w, self.h)

    settings = Gtk.Settings.get_default()
    settings.set_property("gtk-theme-name", "Numix")
    settings.set_property("gtk-application-prefer-dark-theme", False)
    def resize(self, w, h):
        self.win.resize(w, h)

    def main(self):
        Gtk.main()

d = {
    "exit": exit(0),
    "resize": base.resize(w, h)
}

if __name__ == "__main__":
    base = window()
    base.main()
    #t.Thread(target=base.main).start()
    """
    while True:
        asd = str(input(">> "))

        if asd == "exit":
            exit(0)
        if asd == "resize":
            base.resize(400,400)
            
        print ("Result: " + asd)

"""
