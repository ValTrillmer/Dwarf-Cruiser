import random
import time
import sys

active_ships = []
queue = []
ship_names = ["Inscrutible", "Majestic", "Unassailable"]
given_names = ["Gary", "Carol", "Francis", "Francine", "Rory", "Susan", "Lorne", "Kimberly"]
surnames = ["Smith", "Carter", "Wang", "Meguid", "Takarada", "Singh", "Cano"]
room_types = ["engineering", "bridge", "maintenance", "living quarters", "battery"]
system_list = ["life_support", "communications", "power", "weapons"]

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

	#room generators
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


	#system generators
	def gen_systems(self):
		for s in system_list:
			x = getattr(self,s)(s)
			self.systems.append(x)

	def life_support(self, s):
		return life_support(s, self, True, 100, None)

	def communications(self, s):
		return communications(s, self, True, 100, None)

	def power(self, s):
		return power(s, self, True, 100, None, 1000, 1000)

	def weapons(self,s):
		return weapons(s, self, True, 100, None)


	#crew generator
	def populate(self):
		full = False
		while not full:
			x = len(self.crew)
			if x < self.max_crew:
				n = given_names[random.randint(0, len(given_names)-1)]+" "+surnames[random.randint(0, len(surnames)-1)]
				c = crew_member(n,"swabby",self,100,100,None,None)
				self.crew.append(c)
				a = random.randint(0,len(self.layout)-1)
				self.layout[a].living.append(c)
				c.room = self.layout[a]
			else:
				full = True


	def sys_online(self):
		for s in self.systems:
			s.start()
	
	#update functions
	def update(self):
		for s in self.systems:
			s.degrade()
			s.update()
			if s.hp > 100:
				s.hp = 100




#ship system classes
class system:
	def __init__(self, name, ship, active, hp, p):
		self.name = name
		self.ship = ship
		self.active = active
		self.hp = hp
		self.p = p

	def __repr__(self):
		return self.name

	def start(self):
		pass

	def status(self):
		pass

	def update(self):
		pass

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


class life_support(system):
	def __init__(self, name, ship, active, hp, p):
		system.__init__(self, name, ship, active, hp, p)

	def update(self):
		for r in self.ship.layout:
			r.oxygen = self.hp
			if r.oxygen > 100:
				r.oxygen = 100

class communications(system):
	def __init__(self, name, ship, active, hp, p):
		system.__init__(self, name, ship, active, hp, p)

class power(system):
	def __init__(self, name, ship, active, hp, p, output, reserve):
		system.__init__(self, name, ship, active, hp, p)
		self.output = output
		self.reserve = reserve

	def start(self):
		for s in self.ship.systems:
			if s != self:
				s.p = 100
				self.reserve = self.reserve - s.p
		print(str(self.reserve)+" power reserved.")

class weapons(system):
	def __init__(self, name, ship, active, hp, p):
		system.__init__(self, name, ship, active, hp, p)

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
	def __init__(self, name, rank, ship, vitals, oxygen, room, action):
		self.name = name
		self.rank = rank
		self.ship = ship
		self.vitals = vitals
		self.oxygen = oxygen
		self.room = room
		self.action = action

	#update functions
	def update(self, tick):
		self.move(tick)
		self.status()
		self.repair(tick)

	def status(self):
		self.oxygen = self.room.oxygen
		if self.oxygen == 0:
			self.vitals = 0
			print(self.name+" has asphyxiated.")
		if self.vitals == 0:
			self.ship.crew.remove(self)
			self.room.living.remove(self)
			self.room.dead.append(self)


	def move(self, tick):
		if tick%60 == 0:
			selected = False
			while not selected:
				new_room = random.randint(0,len(self.ship.layout)-1)
				if self.room != self.ship.layout[new_room]:
					selected = True
			self.room = self.ship.layout[new_room]
			self.ship.layout[new_room].living.append(self)

	def repair(self, tick):
		if tick%30 == 0:
			if self.room.name == "maintenance":
				self.ship.systems[0].hp = self.ship.systems[0].hp + 5
				self.action = "repairing "+self.room.name
			else:
				self.action = None

	def __repr__(self):
		return self.name



#ship generator
def generate_ship():
	n = ship_names[random.randint(0,len(ship_names)-1)]
	s = ship(n,[],5,5,100,[],[],[])
	active_ships.append(s)
	s.gen_rooms()
	s.populate()
	s.gen_systems()
	s.init_display()
	s.sys_online()



#game
generate_ship()

#game loop
def update(tick):
	for s in active_ships:
		for c in s.crew:
			c.update(tick)
		if tick%30 == 0:
			s.update()
