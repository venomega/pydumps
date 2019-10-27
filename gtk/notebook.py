import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk




win = Gtk.Window(title="Simple Notebook Example")
win.set_border_width(3)

notebook = Gtk.Notebook()
win.add(notebook)

notebook.page1 = Gtk.Box()
notebook.page1.set_border_width(10)
notebook.page1.add(Gtk.Label('Default Page!'))
notebook.append_page(notebook.page1, Gtk.Label('Plain Title'))

notebook.page2 = Gtk.Box()
notebook.page2.set_border_width(10)
notebook.page2.add(Gtk.Label('A page with an image for a Title.'))
notebook.append_page(notebook.page2,Gtk.Image.new_from_icon_name("help-about",Gtk.IconSize.MENU))


win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
