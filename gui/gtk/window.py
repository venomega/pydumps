import gi
#gi.require_version("Gtk","3.0")
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
## SIGNALS NAME
#   destroy
#   clicked

## FUNCAO
# Gtk.main_quit

## OBJECTS
# \/- this gets the object window
#var = Gtk.Window() <- args none jet
# \/- this get the object button
#var = Gtk.Button() <-label=
#\/-var containing object
#||         \/- signal name
#var.connect(1,2) <
#              ^funcao to call on signal

import time
def _clicked(self):
    self.set_label("world")
    
    Gtk.main_quit()

win = Gtk.Window()
win.connect("destroy",Gtk.main_quit)

button = Gtk.Button(label="Hello")
button.connect("clicked", _clicked)

win.add(button)
win.show_all()
Gtk.main()
