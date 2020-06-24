from . import *

class Apple(Food):

	class_name = 'apple'

	def __init__(self):
		super().__init__()
		self.effect = Effect(hunger=5, thirst=5, mood=2)