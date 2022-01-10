import kivy
kivy.require("1.6.0")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


def send(destinatario):
	d = {"USER":"guilleps92@nauta.cu",
		"PASS":"DHthhnZN",
		"DEST":destinatario}
	return sendmail(d)

destinatario = TextInput(multiline=False)
destinatario_g = GridLayout()
destinatario_g.cols = 2
destinatario_g.size_hint = (1, 0.1)
destinatario_g.add_widget(Label(size_hint=(0.25,1),text="Dest:"))
destinatario_g.add_widget(destinatario)
#------------
subject = TextInput(multiline=False)
subject_g = GridLayout()
subject_g.cols = 2
subject_g.size_hint = (1,0.1)
subject_g.add_widget(Label(size_hint=(0.25,1),text="Subject:"))
subject_g.add_widget(subject)
#------------
field = TextInput()
clear = Button(text="Clear", on_release=lambda x: setattr(field,"text",""))
submit = Button(text="Send", on_release=lambda x: [
	print(sendmail(destinatario.text)),
	setattr(field,"text",""),
	setattr(subject,"text","")])
buttons = GridLayout()
buttons.cols = 2
buttons.size_hint = (1,0.2)
buttons.add_widget(clear)
buttons.add_widget(submit)
#------------
box = BoxLayout(orientation="vertical")
box.add_widget(destinatario_g)
box.add_widget(subject_g)
box.add_widget(field)
box.add_widget(buttons)


class app(App):
	def build(self):
		return box

app().run()
