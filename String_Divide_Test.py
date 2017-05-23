import pygame

string = "Hello, my fiend. We meet again. It's been a while; where do we begin. Feels like forever."

font = None

def get_font():
	global font
	font = pygame.font.SysFont(None, 24)

def break_text(string, font, max_size):
	if string == None:
		return
	text_boxes = []
	words = string.split(None)
	m = max_size
	space = " "
	space_length  = font.size(space)[0]
	l = ""
	for s in words:
		if font.size(l)[0]+space_length+font.size(s)[0] < m:
			l = l+space+s
			if words.index(s) == len(words)-1:
				text_boxes.append(l)
		else:
			text_boxes.append(l)
			l = s
	print(text_boxes)




pygame.init()
get_font()
break_text(string, font, 250)