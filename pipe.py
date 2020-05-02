from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image
from kivy.clock import Clock



class Pipe(Widget):
	GAP_SIZE = NumericProperty(64)
	CAP_WIDTH = NumericProperty(66)
	CAP_HEIGHT = NumericProperty(22)
	BODY_WIDTH = NumericProperty(60)
	BODY_HEIGHT = NumericProperty(20)

	pipe_center = NumericProperty(0)
	bottom_b_pos = NumericProperty(0)
	bottom_c_pos = NumericProperty(0)
	top_b_pos = NumericProperty(0)
	top_c_pos = NumericProperty(0)

	#Texture
	pipe_b_texture = ObjectProperty(None)
	pipe_c_texture = ObjectProperty(None)
	lower_pipe_tex_coords = ListProperty((0,0,1,0,1,4,0,4))
	top_pipe_tex_coords = ListProperty((0,0,1,0,1,1,0,1))


	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.pipe_b_texture = Image(source = "assets/pipeB.png").texture
		self.pipe_b_texture.wrap = 'repeat'
		self.pipe_c_texture = Image(source = "assets/pipeT.png").texture
		self.pipe_c_texture.wrap = 'repeat'

	def on_size(self, *args):
		lower_body_size = self.bottom_c_pos - self.bottom_b_pos

		top_body_size =  self.top - self.top_b_pos

		self.lower_pipe_tex_coords[5] = lower_body_size/self.BODY_HEIGHT
		self.lower_pipe_tex_coords[7] = lower_body_size/self.BODY_HEIGHT


		self.top_pipe_tex_coords[5] = top_body_size/self.BODY_HEIGHT
		self.top_pipe_tex_coords[7] = top_body_size/self.BODY_HEIGHT

	def on_pipe_center(self, *args):
		Clock.schedule_once(self.on_size,0)
