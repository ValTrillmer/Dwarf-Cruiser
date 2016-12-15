import random
import time
import sys

active_ships = []
queue = []
ship_names = ["Inscrutible", "Majestic", "Unassailable"]
given_names = ["Gary", "Carol", "Francis", "Francine", "Rory", "Susan"]
surnames = ["Smith", "Carter", "Wang", "Meguid", "Takarada"]
room_types = ["engineering", "bridge", "maintenance", "living quarters"]

#game classes
class ship:
	def __init__(self, name, crew, batteries, engines, layout):
		self.name = "The "+name
		self.crew = crew
		self.batteries = batteries
		self.engines = engines
		self.layout = layout

	def __repr__(self):
		return self.name

class crew_member:
	def __init__(self, name, rank, vitals, room):
		self.name = name
		self.rank = rank
		self.vitals = vitals
		self.room = room

	def status(self):
		if self.vitals > 5:
			print(self.name+" is healthy.")
			return True
		elif self.vitals < 5 and self.vitals > 0:
			print(self.name+" is not feeling well.")
			return True
		else:
			print(self.name+" has died.")
			return False
	
	def breathing(self):
			if self.room.oxygen == False:
				print(self.name+" has asphyxiated.")
				self.vitals = 0
				return False
			else:
				print(self.name+" is healthy.")
				return True

	def location(self):
		print(self.name+" is in "+self.room.name)

	def __repr__(self):
		return self.name

class room:
	def __init__(self, name, living, dead, oxygen):
		self.name = name
		self.living = living
		self.dead = dead
		self.oxygen = oxygen

	def __repr__(self):
		return self.name

#generator functions
def generate_ship():
	n = ship_names[random.randint(0,len(ship_names)-1)]
	c = []
	b = []
	e = []
	l = []
	s = ship(n,c,b,e,l)
	active_ships.append(s)
	generate_rooms()

def populate_ship():
	full = False
	while not full:
		x = len(active_ships[0].crew)
		if x < 6:
			n = given_names[random.randint(0, len(given_names)-1)]+" "+surnames[random.randint(0, len(surnames)-1)]
			r = "swabby"
			v = 10
			rm = None
			c = crew_member(n,r,v,rm)
			active_ships[0].crew.append(c)
			a = random.randint(0,len(active_ships[0].layout)-1)
			active_ships[0].layout[a].living.append(c)
			c.room = active_ships[0].layout[a]
		else:
			full = True

def generate_rooms():
	for x in room_types:
		l = []
		d = []
		o = True
		r = room(x,l,d,o)
		active_ships[0].layout.append(r)

def fill_queue(ship):
	for c in ship.crew:
		queue.append(c)

def crew_update():
	y = list(active_ships[0].crew)
	for c in y:
		if c.breathing() == False:
			active_ships[0].crew.remove(c)
			c.room.living.remove(c)
			c.room.dead.append(c)
		c.location()

generate_ship()
populate_ship()

#game loop
running = True
while running:
	print(active_ships[0])
	print(active_ships[0].layout)
	for c in active_ships[0].crew:
		print(c)
	crew_update()
	running = False