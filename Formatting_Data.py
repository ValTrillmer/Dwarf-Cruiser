import pygame

white = (255,255,255)
black = (0,0,0)

font = None

def set_font():
	global font
	font = pygame.font.SysFont(None, 18) #arguments are (name, size, bold=True/False, italic=True/False)