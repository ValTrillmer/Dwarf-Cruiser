import pygame

string = "Hello, my friend, we meet again. It's been a while; where do we begin. Feels like forever."

font = None

def get_font():
	global font
	font = pygame.font.SysFont(None, 24)

def break_text(string, font, max_size):
	new_string = string
	string_length = len(new_string)
	wrapped = []
	pixel_length = font.size(new_string)[0]
	m = max_size
	done = False
	while not done:
		if pixel_length > m:
			line = False
			words = 0
			while not line:
				s = new_string.split(None, words)[0]
				print(s)
				if font.size(s)[0] > m:
					words = words+1
				else:
					wrapped.append(s)
					new_string = string[len(s):]
					words = 0
					line = True
		else:
			wrapped.append(new_string)
			done = True

	print(wrapped)


		



pygame.init()
get_font()
break_text(string, font, 250)