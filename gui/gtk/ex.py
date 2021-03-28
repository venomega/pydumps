import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
from gi.repository import GObject as gobject
import os
from subprocess import Popen, PIPE
import fcntl

wnd = gtk.Window()
wnd.set_default_size(800, 600)
wnd.connect("destroy", gtk.main_quit)

textview = gtk.TextView()
#textview.modify_font(fontdesc)

scroll = gtk.ScrolledWindow()
scroll.add(textview)
#exp = gtk.Expander()
#exp.add(scroll)
wnd.add(scroll)
wnd.show_all()
sub_proc = Popen("python3 pychat/a.py", stdout=PIPE, shell=True)
sub_outp = ""


def non_block_read(output):
    fd = output.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    try:
        return output.read().decode("utf-8")
    except:
        return ''


def update_terminal():
    textview.get_buffer().insert_at_cursor(non_block_read(sub_proc.stdout))
    return sub_proc.poll() is None

gobject.timeout_add(100, update_terminal)
gtk.main()