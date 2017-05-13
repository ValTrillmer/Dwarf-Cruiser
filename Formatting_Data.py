import pygame

white = (255,255,255)
black = (0,0,0)

font = None

tablet_buttons = ["Crew", "Systems", "Logs", "Command"]

def set_font():
	global font
	font = pygame.font.SysFont(None, 30) #arguments are (name, size, bold=True/False, italic=True/False)