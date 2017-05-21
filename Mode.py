#perhaps this will be a mode. Modes determine the information needed to create and organize windows
import pygame
from Window import Display
import Formatting_Data as F
from Character import Entity, Player_Character
from Ship import Ship




class Main_Mode:
	def __init__(self):
		self.font = pygame.font.SysFont(None, 18) #arguments are (name, size, bold=True/False, italic=True/False)
		self.window = Display(1280,720,"Ship Zone",0,0,0,self.font)
		self.main = None
		self.tablet = None
		self.tablet_menu = []
		self.tablet_screen = None
		self.active_container = None
		self.health_bar = None
		self.character = None
		self.player = None
		self.ship = None


	def load_window(self):
		self.window.load()
		self.main = self.window.make_main(0,0,0,1.0,1.0,True,True,None,"Main")
		self.active_container = self.main

	#sets the active container. Active containers can be acted upon by keypresses, allow for different animations
	#or display different information in other containers
	def set_active_container(self, container):
		self.active_container.update_active()
		self.active_container = container
		self.active_container.update_active()

	#function for loading character
	def load_character(self):
		#arguments are x,y,z,width,height,visible,active,parent
		x = self.window.make_container(0,0,0,25,25,True,False,self.main)
		x.border = 0
		x.centre_horizontal()
		x.centre_vertical()
		self.character = x
		#the following attribute is not permanent
		self.player = Player_Character("Bosley McNutt", [100,100])


	#function for loading ship
	def load_ship(self):
		self.ship = Ship()
	
#	def draw_heart(self, screen):
#		pygame.draw.line(screen, (255,192,203), (640,560), (540,460), 10)
#		pygame.draw.line(screen, (255,192,203), (640,560), (740,460), 10)
#		pygame.draw.line(screen, (255,192,203), (540,460), (590,410), 10)
#		pygame.draw.line(screen, (255,192,203), (740,460), (690,410), 10)
#		pygame.draw.line(screen, (255,192,203), (590,410), (640,460), 10)
#		pygame.draw.line(screen, (255,192,203), (690,410), (640,460), 10)

		
	#This function creates and organizes the UI elements for the tablet screen.
	def create_tablet(self):
		self.tablet = self.window.make_container(75,75,0,0.8,0.8,False,False,self.main) #container is main window
		tab_menu = self.window.make_container(0,0,0,1.0,0.15,False,False,self.tablet)
		self.tablet_screen = self.window.make_container(0,tab_menu.height,0,1.0,0.85,False,False,self.tablet)
		t = 0
		x = 0
		string = 0
		while x < 4:
			tab = self.window.make_button(t,0,0,0.25,1.0,False,False,tab_menu,F.tablet_buttons[string])
			t = t+tab_menu.width/4
			x=x+1
			string=string+1
			self.tablet_menu.append(tab)
		text_box = self.window.make_text_box(10,10,0,1.0,1.0,False,False,self.tablet_screen,None)
		text_box.update_colour(F.black, F.white)


	def create_character_display(self):
		c = self.window.make_container(40,10,0,1,1,True,False,self.main)
		c.border = 0
		c.colour = F.black
		t = self.window.make_text_box(0,0,0,0,0,True,False,c,self.player.name)
		t.update_colour(F.black, F.white)
		x = self.window.make_container(0,40,0,200,25,True,False,c)
		y = self.window.make_container(0,0,0,self.player.hp[0]*2,25,True,False,x)
		y.border = 0
		self.health_bar = [y,x]


	def compile_screen(self, screen):
		self.window.render(screen, self.main)



	#the following functions run the game engine or update screen
	def run_engine(self):
		self.update_health_bar()


	def update_health_bar(self):
		self.health_bar[0].width = self.player.change_hp(0)*2
		if self.player.hp[0] == 0:
			self.player.hp[0] = 100

	def update_tablet_screen(self):
		if self.active_container == self.tablet_menu[0]:
			self.tablet_screen.children[0].update_text(self.player.name)
		elif self.active_container == self.tablet_menu[3]:
			self.tablet_screen.children[0].update_text(self.ship.name)
		else:
			self.tablet_screen.children[0].update_text(None)



	def handle_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False #pygame window closed by user
			if event.type == pygame.KEYDOWN: #should be all caps
				if event.key == pygame.K_ESCAPE:
					return False #user pressed ESC
				elif self.active_container == self.main:
					if event.key == pygame.K_LEFT:
						self.character.x = self.character.x-25
					if event.key == pygame.K_RIGHT:
						self.character.x = self.character.x+25
					if event.key == pygame.K_UP:
						self.character.y = self.character.y-25
					if event.key == pygame.K_DOWN:
						self.character.y = self.character.y+25
					if event.key == pygame.K_m:
						self.tablet.set_visible()
						self.set_active_container(self.tablet_menu[0])
						self.update_tablet_screen()
				elif self.active_container != self.main:
					if event.key == pygame.K_LEFT:
						for i, b in enumerate(self.tablet_menu):
							if b.active == True:
								a = i
						if a > 0:
							self.set_active_container(self.tablet_menu[a-1])
						else:
							self.set_active_container(self.tablet_menu[len(self.tablet_menu)-1])
						self.update_tablet_screen()
					if event.key == pygame.K_RIGHT:
						for i, b in enumerate(self.tablet_menu):
							if b.active == True:
								a = i
						if a < len(self.tablet_menu)-1:
							self.set_active_container(self.tablet_menu[a+1])
						else:
							self.set_active_container(self.tablet_menu[0])
						self.update_tablet_screen()
					if event.key == pygame.K_m:
						self.tablet.set_visible()
						self.set_active_container(self.main)
		return True