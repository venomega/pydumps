from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget



class Scene(Widget):
    def __init__(self):
        super().__init__(size=(self.width, self.height))

    def a(self):
        self.size = (self.width, self.height)
        self.size = (200,200)
        print (self.size)
        self.add_widget(Button(
            pos_hint={'x':0.01, 'y':0.01},
            size_hint=(0.01, 0.01),
        ))

class HelloApp(App):
    def build(self):
        o = Scene()
        o.a()
        return o
    

HelloApp().run()