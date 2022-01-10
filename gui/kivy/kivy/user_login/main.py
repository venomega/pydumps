import kivy
kivy.require("1.6.0")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.size= (400,100)
"""
class asd(GridLayout):
	def __init__(self, **dsa):
		super().__init__(**dsa)
		self.cols = 2
		self.add_widget(Label(text="Username"))
		self.add_widget(TextInput(multiline=False))
		self.add_widget(Label(text="Password"))
		self.add_widget(TextInput(password=True,multiline=False))
"""

box = BoxLayout(orientation="vertical")
grid = GridLayout()
grid.cols = 2
grid.add_widget(Label(text="Username"))
grid.add_widget(TextInput(multiline=False))

grid2 = GridLayout()
grid2.cols = 2
grid2.add_widget(Label(text="Password"))
grid2.add_widget(TextInput(multiline=False,password=True))

box.add_widget(grid)
box.add_widget(grid2)

box.add_widget(Button(text="Check",on_release=lambda x: ["pressed",setattr(x,"text","Done")]))

class app(App):
	def build(self):
		return box
app().run()


