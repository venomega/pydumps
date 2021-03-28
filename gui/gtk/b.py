import gi
import threading as t
import time
import tkinter
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class window():
    def __init__(self):
        self.w = 200
        self.h = 200
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk-theme-name", "Numix")
        settings.set_property("gtk-application-prefer-dark-theme", True)
        self.win = Gtk.Window()
        self.win.show_all()
        self.win.connect("destroy", lambda x: Gtk.main_quit())

        self.button = Gtk.Button(label="Hello")
        self.button.connect("clicked", lambda x: self.button.hide())
        self.grid = Gtk.Grid()
        help(self.grid)
        self.win.add(self.button)
        self.win.show_all()
    def resize(self, w, h):
        self.win.resize(w, h)

    def main(self):
        Gtk.main()

class window2(window):
    def __init__(self):
        super().__init__()

base = window()
t.Thread(target=base.main).start()
time.sleep(3)
base.resize(400, 400)
