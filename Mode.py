#perhaps this will be a mode. Modes determine the information needed to create and organize windows
import pygame
from Window import Display

#colour data
white = (255,255,255)
black = (0,0,0)



class Main_Mode:
	def __init__(self):
		self.font = pygame.font.SysFont(None, 18) #arguments are (name, size, bold=True/False, italic=True/False)
		self.window = Display(1280,720,"Ship Zone",0,0,0,self.font)
		self.container = []
		self.tablet_menu = []
		self.active_container = None


	def load_window(self):
		self.window.load()
		main = self.window.make_main(0,0,0,1.0,1.0,True,True,None,"Main")
		self.container.append(main)
		self.active_container = main

	#sets the active container. Active containers can be acted upon by keypresses, allow for different animations
	#or display different information in other containers
	def set_active_container(self, container):
		self.active_container.update_active()
		self.active_container = container
		self.active_container.update_active()

		
	#This function creates and organizes the UI elements for the tablet screen.
	def create_tablet(self):
		tablet = self.window.make_container(75,75,0,0.8,0.8,False,False,self.container[0]) #container is main window
		self.container.append(tablet)
		tab_menu = self.window.make_container(0,0,0,1.0,0.15,False,False,tablet)
		self.container.append(tab_menu)
		tab_screen = self.window.make_container(0,tab_menu.height,0,1.0,0.85,False,False,tablet)
		self.container.append(tab_screen)
		t = 0
		x = 0
		while x < 4:
			tab = self.window.make_button(t,0,0,0.25,1.0,False,False,tab_menu)
			tab.create_text_box()
			self.container.append(tab)
			t = t+tab_menu.width/4
			x=x+1
		self.tablet_menu = self.container[4:8]


	def compile_screen(self, screen):
		self.window.render(screen, self.container[0])

	#hoo boy this one needs some work
	def handle_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False #pygame window closed by user
			elif event.type == pygame.KEYDOWN: #should be all caps
				if event.key == pygame.K_ESCAPE:
					return False #user pressed ESC
				if event.key == pygame.K_m:
					if self.container[1].visible == False:
						self.container[1].set_visible()
						self.set_active_container(self.tablet_menu[0])
					elif self.container.visible == True:
						self.container[1].set_visible()
						self.set_active_container(self.container[0])
					else:
						pass
					return True
				
				if event.key == pygame.K_LEFT:
					if self.active_container.name == "Main":
						pass
					else:
						#OK, SO HOW THIS WORKS. It iterates over self.tablet_menu, looking for an active object, once it 
						#finds one, it also returns the index in the list. Then it sets a new active to the left of the object
						for i, b in enumerate(self.tablet_menu):
							if b.active == True:
								a = i
						if a > 0:
							self.set_active_container(self.tablet_menu[a-1])
						else:
							self.set_active_container(self.tablet_menu[len(self.tablet_menu)-1])

				if event.key == pygame.K_RIGHT:
					try:
						if self.active_container.name == "Main":
							pass
					except AttributeError:
						#SEE ABOVE
						for i, b in enumerate(self.tablet_menu):
							if b.active == True:
								a = i
						if a < len(self.tablet_menu)-1:
							self.set_active_container(self.tablet_menu[a+1])
						else:
							self.set_active_container(self.tablet_menu[0])

		return True