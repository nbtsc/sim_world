from collections import defaultdict

class World:

	def __init__(self):
		self.things = defaultdict(list)
		self.elaspse_list = []

	def new(self, thing):
		self.things[thing.class_name].append(thing)
		if hasattr(thing, 'elapse'):
			self.elaspse_list.append(thing)

	def elapse(self, count):
		for i in range(count):
			for thing in self.elaspse_list:
				thing.elapse()