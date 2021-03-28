import gi
import threading as t
import time
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

b = Gtk.Builder()
b.add_from_file("/tmp/a.glade")
win = b.get_object("window")
win.show_all()
Gtk.main()
