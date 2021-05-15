import kivy.app
import kivy.uix.video
import kivy.uix.button



class Asd(kivy.app.App):
    def build(self):
        return kivy.uix.button.Button(text="asd")



o =Asd()

o.run()