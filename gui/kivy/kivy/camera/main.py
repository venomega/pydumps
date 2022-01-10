import os
import multiprocessing as m
import kivy
kivy.require("1.11.0")
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.core.window import Window
Window.size = (144,144)

class cam(Camera):
	def __init__(self, **kw):
		super().__init__(resolution=(144,144))
		self.count = 0
	def loop(self,*asd):
		if self.texture:
			print (self.texture.save(f"/tmp/asd/{self.count}.jpg"))
		#self.texture.save(f"/tmp/{count}.jpg")
		self.count += 1
	def on_touch_down(self,touch):
		print ("X:", touch.x,"Y:",touch.y, self.width, self.height)

o = App()
def build():
	c = cam(resolution=(144,144))
	Clock.schedule_interval(c.loop, 1.0/4.0)
	return c
o.build = build
o.run()
