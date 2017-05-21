import random

#a base ship class. The generalized class allows the program to create multiple and varied ships
class Ship:
	def __init__(self):
		self.name = "The Voidcraft"
		self.hull_integrity = 100
		self.rooms = []

	def __repr__(self):
		pass