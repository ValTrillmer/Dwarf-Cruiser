class Entity:
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp

	def __repr__(self):
		pass

class Player_Character:
	def __init__(self, name, hp):
		Entity.__init__(self, name, hp)

	def change_hp(self, x):
		self.hp[0] = self.hp[0]-x
		return self.hp[0]