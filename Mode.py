#perhaps this will be a mode. Modes determine the information needed to create and organize windows
import pygame
from Window import Window

#colour data
white = (255,255,255)
black = (0,0,0)



class Main_Mode:
	def __init__(self):
		self.font = pygame.font.SysFont(None, 18) #arguments are (name, size, bold=True/False, italic=True/False)
		self.main = Window(1280,720,"Ship Zone",0,0,0,True,black,white,self.font)
		self.tablet = Window(800,400,"Tablet",50,50,1,True,black,white,self.font)

	def load_windows(self):
		self.main.load()
		self.tablet.load()

	def compile_screen(self, screen):
		self.main.render(screen)
		if self.tablet.visible == True:
			self.tablet.render(screen)