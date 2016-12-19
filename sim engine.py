import random
import time
import sys

active_ships = []
queue = []
ship_names = ["Inscrutible", "Majestic", "Unassailable"]
given_names = ["Gary", "Carol", "Francis", "Francine", "Rory", "Susan"]
surnames = ["Smith", "Carter", "Wang", "Meguid", "Takarada"]
room_types = ["engineering", "bridge", "maintenance", "living quarters"]
system_list = ["life support", "communications", "gravity"]

#ship classes
class ship:
	def __init__(self, name, crew, hull, batteries, engines, layout, systems):
		self.name = "The "+name
		self.crew = crew
		self.hull = hull
		self.batteries = batteries
		self.engines = engines
		self.layout = layout
		self.systems = systems

	def __repr__(self):
		return self.name

#ship system classes
class life_support:
	def __init__(self, name, active, hp):
		self.name = name
		self.active = active
		self.hp = hp

	def __repr__(self):
		return self.name

	def update(self, active_ships):
		for r in active_ships[0].layout:
			r.oxygen = self.hp

class room:
	def __init__(self, name, living, dead, oxygen):
		self.name = name
		self.living = living
		self.dead = dead
		self.oxygen = oxygen

	def __repr__(self):
		return self.name

class battery:
	def __init__(self, name, active, dmg, hp):
		self.name = name
		self.active = active
		self.dmg = dmg
		self.hp = hp

	def __repr__(self):
		return self.name




class crew_member:
	def __init__(self, name, rank, vitals, oxygen, room):
		self.name = name
		self.rank = rank
		self.vitals = vitals
		self.oxygen = oxygen
		self.room = room

	def status(self):
		self.oxygen = self.room.oxygen
		if self.oxygen == 0:
			self.vitals = 0
			print(self.name+" has asphyxiated.")
		if self.vitals == 0:
			active_ships[0].crew.remove(self)
			self.room.living.remove(self)
			self.room.dead.append(self)


	def location(self):
		print(self.name+" is in "+self.room.name)

	def move(self, active_ships):
		selected = False
		while not selected:
			new_room = random.randint(0,len(active_ships[0].layout)-1)
			if self.room != active_ships[0].layout[new_room]:
				selected = True
		self.room = active_ships[0].layout[new_room]
		active_ships[0].layout[new_room].living.append(self)

	def __repr__(self):
		return self.name



#ship generator functions
def generate_ship():
	n = ship_names[random.randint(0,len(ship_names)-1)]
	c = []
	h = 100
	b = []
	e = []
	l = []
	sy = []
	s = ship(n,c,h,b,e,l,sy)
	active_ships.append(s)
	generate_rooms()
	generate_battery()
	generate_ls()

def generate_ls():
	n = system_list[0]
	a = True
	h = 2
	ls = life_support(n,a,h)
	active_ships[0].systems.append(ls)

def generate_rooms():
	for x in room_types:
		l = []
		d = []
		o = 100
		r = room(x,l,d,o)
		active_ships[0].layout.append(r)

def generate_battery():
	n = "fore battery"
	a = True
	d = 10
	h = 2
	b = battery(n,a,d,h)
	active_ships[0].batteries.append(b)


#crew populator
def populate_ship():
	full = False
	while not full:
		x = len(active_ships[0].crew)
		if x < 6:
			n = given_names[random.randint(0, len(given_names)-1)]+" "+surnames[random.randint(0, len(surnames)-1)]
			r = "swabby"
			v = 10
			o = 100
			rm = None
			c = crew_member(n,r,v,o,rm)
			active_ships[0].crew.append(c)
			a = random.randint(0,len(active_ships[0].layout)-1)
			active_ships[0].layout[a].living.append(c)
			c.room = active_ships[0].layout[a]
		else:
			full = True



#update functions
def fill_squeue():
	s = []
	for b in active_ships[0].systems:
		s.append(b)
	for x in active_ships[0].batteries:
		s.append(x)
	return s

def crew_update():
	for c in list(active_ships[0].crew):
		c.status()
		#if c.breathing() == False:
		#	active_ships[0].crew.remove(c)
		#	c.room.living.remove(c)
		#	c.room.dead.append(c)
		c.location()
	for x in active_ships[0].crew:
		if x.vitals > 0:
			x.move(active_ships)
		else:
			pass

def ship_update():
	s = fill_squeue()
	for r in s:
		degrade(r)
	active_ships[0].systems[0].update(active_ships)

def degrade(r):
	if r.active == True:
		r.hp = r.hp-1
		if r.hp > 0:
			print(r.name+" has taken damage.")
		else:
			print(r.name+" has been destroyed.")
			r.active = False
	else:
		print(r.name+" is inactive.")


#game
generate_ship()
populate_ship()

print(active_ships[0])
print(active_ships[0].layout)
for c in active_ships[0].crew:
	print(c)
print(active_ships[0].batteries)

#game loop
running = True
while running:
	crew_update()
	print("")
	ship_update()
	print("")
	i = input()
	if i == "oxygen":
		for r in active_ships[0].layout:
			print(r.name+" "+str(r.oxygen))
	else:
		pass
	#running = False