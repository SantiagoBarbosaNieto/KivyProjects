import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.window import Window
from kivy.clock import Clock

from random import randint

from pipe import Pipe



class Background(Widget):
	base_texture = ObjectProperty(None)
	bg_texture = ObjectProperty(None)

	BASE_HEIGHT = NumericProperty(100)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		#Create textures
		self.bg_texture = Image(source = "assets/bg.png").texture
		self.bg_texture.wrap = 'repeat'
		self.bg_texture.uvsize = (0.5, -1)


		self.base_texture = Image(source = "assets/base.png").texture
		self.base_texture.wrap = 'repeat'
		self.base_texture.uvsize = (1, -1)


	def scroll_textures(self, time_passed):
		#Update the uvpos of the texture
		self.base_texture.uvpos = ((self.base_texture.uvpos[0]+time_passed/2)%Window.width, self.base_texture.uvpos[1])
		self.bg_texture.uvpos = ((self.bg_texture.uvpos[0]+time_passed/8)%Window.width, self.bg_texture.uvpos[1])
		#Redraw the texture
		texture = self.property('base_texture')
		texture.dispatch(self)
		texture = self.property('bg_texture')
		texture.dispatch(self)

class MainApp(App):

	pipes = []
	def on_start(self):
		scrolling = Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60.)
		pass

	def start_game(self):
		#create pipes
		num_pipes = 5
		pipes_gap = Window.width/(num_pipes-1)	
		for i in range(num_pipes):
			pipe = Pipe()
			#                          (Base Height + Body Height + Cap height + 30, root Height - Body Height - Cap height - 30) 
			pipe.pipe_center = randint(100 +20+20 +30, self.root.height - 20-20 -30)
			pipe.size_hint = (None,None)
			pipe.pos = (pipes_gap*i, 100)
			#           (Cap width, root height - base height)  
			pipe.size = (66, self.root.height - 100)

			self.pipes.append(pipe)
			self.root.add_widget(pipe)

		#move pipes

		Clock.schedule_interval(self.move_pipes, 1/60.)

	def move_pipes(self, time_passed):
		for pipe in self.pipes:
			pipe.x -= time_passed * 150


		num_pipes = 5
		pipes_gap = Window.width/(num_pipes-1)	

		pipes_xs = list(map(lambda pipe: pipe.x, self.pipes))
		right_most_x = max(pipes_xs)
		if right_most_x <= Window.width - pipes_gap:
			left_most_pipe = self.pipes[pipes_xs.index(min(pipes_xs))]
			left_most_pipe.x = Window.width
			left_most_pipe.pipe_center = randint(100 +20+20 +30, self.root.height - 20-20 -30)

MainApp().run()