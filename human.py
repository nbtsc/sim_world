

class Human:

	elapse_hunger = -60/86400
	elapse_thirst = -60/86400
	elapse_fatigue = 10/86400
	elapse_age = 1/365/86400
	elapse_stamia = 30/365/86400
	elapse_knowledge = 1/365/86400

	class_name = 'human'

	def __init__(self):
		self.age = 0
		self.stamia = 0
		self.knowledge = 0
		self.happiness = 50
		self.metabolism = 100

		self.hunger = 80
		self.thirst = 80
		self.fatigue = 0
		self.mood = 50

	def eat(self, food):
		self.body_effect(food.effect)

	def drink(self, drink):
		self.body_effect(drink.effect)

	def elapse(self):
		self.hunger += self.metabolism/100 * self.elapse_hunger
		self.thirst += self.metabolism/100 * self.elapse_thirst
		self.fatigue += self.metabolism/100 * self.elapse_fatigue

		self.age += self.elapse_age
		self.stamia += (self.hunger-50) * self.elapse_stamia
		self.stamia = max(self.stamia, 0)
		self.knowledge += self.elapse_knowledge

	def display(self):
		print('年龄:%d'%self.age)
		print('体力:%d'%self.stamia)
		print('知识:%d'%self.knowledge)
		print('幸福:%d'%self.happiness)
		print('新陈代谢:%d'%self.metabolism)

		print('饥饿:%d'%self.hunger)
		print('口渴:%d'%self.thirst)
		print('疲劳:%d'%self.fatigue)
		print('情绪:%d'%self.mood)

	def body_effect(self, effect):
		self.hunger += effect.hunger
		self.thirst += effect.thirst
		self.fatigue += effect.fatigue
		self.mood += effect.mood