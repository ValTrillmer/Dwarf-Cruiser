#perhaps this will be a mode. Modes determine the information needed to create and organize windows
import pygame
from Window import Window

#colour data
white = (255,255,255)
black = (0,0,0)

class Mode:
	def __init__(self, screen):
		self.screen = screen
		self.fill_colour = black
		self.text_colour = white
		self.font = pygame.font.SysFont(None, 18) #arguments are (name, size, bold=True/False, italic=True/False)

	def render(self):
		self.screen.blit(self.surface, (self.x,self.y))
