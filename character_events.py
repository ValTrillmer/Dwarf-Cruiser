import random
from name_data import male_given
from name_data import female_given
from name_data import surname

#character stories are formed by the vevents of their lives

class event:
	def generate(self):
		pass

class birth(event):
	def __init__(self, date, memory, reaction, event):
		self.date = date
		self.memory = memory
		self.reaction = reaction
		self.event = event

	def __repr__(self):
		pass

	def generate(self):
		