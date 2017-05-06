#perhaps this will be a mode. Modes determine the information needed to create and organize windows
import pygame
from Window import Display

#colour data
white = (255,255,255)
black = (0,0,0)



class Main_Mode:
	def __init__(self):
		self.font = pygame.font.SysFont(None, 18) #arguments are (name, size, bold=True/False, italic=True/False)
		self.window = Display(1280,720,"Ship Zone",0,0,0,black,white,self.font)
		self.container = []


	def load_window(self):
		self.window.load()
		main = self.window.make_container("Main",0,0,0,1.0,1.0,5,True,None)
		self.container.append(main)
		tablet = self.window.make_container("Tablet",50,50,0,0.4,0.4,5,False,main)
		self.container.append(tablet)
		sub = self.window.make_container("Sub",50,50,0,0.4,0.4,5,True,tablet)
		self.container.append(sub)



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
					for w in self.container:
						if w.name == "Tablet" and w.visible == False:
							w.visible = True
						elif w.name == "Tablet" and w.visible == True:
							w.visible = False
						else:
							pass
					return True
				elif event.key == pygame.K_n:
					for w in self.container:
						if w.name == "Sub" and w.visible == False:
							w.visible = True
						elif w.name == "Sub" and w.visible == True:
							w.visible = False
						else:
							pass
		return True
