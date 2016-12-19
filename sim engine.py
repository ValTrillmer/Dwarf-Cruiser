import random
import time
import sys

active_ships = []
queue = []
ship_names = ["Inscrutible", "Majestic", "Unassailable"]
given_names = ["Gary", "Carol", "Francis", "Francine", "Rory", "Susan"]
surnames = ["Smith", "Carter", "Wang", "Meguid", "Takarada"]
room_types = ["engineering", "bridge", "maintenance", "living quarters", "battery"]
system_list = ["life support", "communications", "gravity"]

#ship classes
class ship:
	def __init__(self, name, crew, max_crew, max_batteries, hull, engines, layout, systems):
		self.name = "The "+name
		self.crew = crew
		self.max_crew = max_crew
		self.max_batteries = max_batteries
		self.hull = hull
		self.engines = engines
		self.layout = layout
		self.systems = systems

	def __repr__(self):
		return self.name

	def init_display(self):
		print(self.name+"\n"+str(self.layout))
		for c in self.crew:
			print(c)

	#generator functions
	def gen_rooms(self):
		rooms = ["bridge", "engineering", "maintenance"]
		lq = 0
		for lq in range(self.max_crew):
			rooms.append("living_quarters")
			lq = lq+1
		b = 0
		for b in range(self.max_batteries):
			rooms.append("battery")
			b = b+1
		for r in rooms:
			x = getattr(self,r)(r)
			self.layout.append(x)

	def bridge(self, r):
		return bridge(r,[],[],100)

	def engineering(self, r):
		return engineering(r,[],[],100)

	def maintenance(self, r):
		return maintenance(r,[],[],100)

	def living_quarters(self, r):
		return living_quarters(r,[],[],100)

	def battery(self, r):
		return battery(r,[],[],100,10)

	def populate(self):
		full = False
		while not full:
			x = len(self.crew)
			if x < self.max_crew:
				n = given_names[random.randint(0, len(given_names)-1)]+" "+surnames[random.randint(0, len(surnames)-1)]
				c = crew_member(n,"swabby",10,100,None)
				self.crew.append(c)
				a = random.randint(0,len(self.layout)-1)
				self.layout[a].living.append(c)
				c.room = self.layout[a]
			else:
				full = True

	def gen_ls(self):
		ls = life_support(system_list[0],True,100)
		self.systems.append(ls)

	
	#update functions
	def update(self):
		for r in self.systems:
			r.degrade()
		self.systems[0].update()



#ship system classes
class life_support:
	def __init__(self, name, active, hp):
		self.name = name
		self.active = active
		self.hp = hp

	def __repr__(self):
		return self.name

	def update(self):
		if self.hp > 100:
			self.hp = 100
		for r in active_ships[0].layout:
			r.oxygen = self.hp

	def degrade(self):
		if self.active == True:
			self.hp = self.hp-1
			if self.hp > 0:
				print(self.name+" has taken damage.")
			else:
				print(self.name+" has been destroyed.")
				self.active = False
		else:
			print(self.name+" is inactive.")



#room classes
class room:
	def __init__(self, name, living, dead, oxygen):
		self.name = name
		self.living = living
		self.dead = dead
		self.oxygen = oxygen

	def __repr__(self):
		return self.name

	def status(self):
		pass

#room subclasses
class battery(room):
	def __init__(self, name, living, dead, oxygen, dmg):
		room.__init__(self, name, living, dead, oxygen)
		self.dmg = dmg

	def status(self):
		room.status()
		print(self.dmg)

class bridge(room):
	def __init__(self, name, living, dead, oxygen):
		room.__init__(self, name, living, dead, oxygen)

class maintenance(room):
	def __init__(self, name, living, dead, oxygen):
		room.__init__(self, name, living, dead, oxygen)

class engineering(room):
	def __init__(self, name, living, dead, oxygen):
		room.__init__(self, name, living, dead, oxygen)

class living_quarters(room):
	def __init__(self, name, living, dead, oxygen):
		room.__init__(self, name, living, dead, oxygen)





#people classes
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
		print(self.name+" is in the "+self.room.name)

	def move(self):
		selected = False
		while not selected:
			new_room = random.randint(0,len(active_ships[0].layout)-1)
			if self.room != active_ships[0].layout[new_room]:
				selected = True
		self.room = active_ships[0].layout[new_room]
		active_ships[0].layout[new_room].living.append(self)

	def repair(self):
		if self.room.name == "maintenance":
			active_ships[0].systems[0].hp = active_ships[0].systems[0].hp + 5
			print(self.name+" is repairing "+active_ships[0].systems[0].name)

	def __repr__(self):
		return self.name



#ship generator
def generate_ship():
	n = ship_names[random.randint(0,len(ship_names)-1)]
	s = ship(n,[],5,5,100,[],[],[])
	active_ships.append(s)
	s.gen_rooms()
	s.populate()
	s.gen_ls()
	s.init_display()


#update functions
def crew_update():
	for c in list(active_ships[0].crew):
		c.move()
		c.location()
		c.status()
		c.repair()



#game
generate_ship()

#game loop
running = True
while running:
	crew_update()
	print("")
	for s in active_ships:
		s.update()
	print("")
	i = input()
	if i == "oxygen":
		for r in active_ships[0].layout:
			print(r.name+" "+str(r.oxygen))
	elif i == "dead":
		print(active_ships[0].crew)
		for d in active_ships[0].layout:
			print(d.name+" "+str(d.dead))
	else:
		pass