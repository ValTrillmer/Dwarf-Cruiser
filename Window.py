#contains the Window class, which holds drawing functions.
import pygame

#The following functions create and modify surfaces.

#The following functions create displays with the drawing functions using input from the engine.

#Notes on creating and drawing on new surfaces. Draw new surface. Blit is putting a surface on a surface. First make text, then blit the text to the background,
	#then blit the background to the screen. This is just an example function. Be sure to assemble surfaces before
	#displaying them.

class Window:
	def __init__(self, width, height, title, x, y, z, visible, fill_colour, text_colour, font):
		self.width = width
		self.height = height
		self.title = title
		self.x = x
		self.y = y
		self.z = z
		self.visible = visible
		self.fill_colour = fill_colour
		self.text_colour = text_colour
		self.font = font
		self.surface = None

	#creates a surface to draw on and stores it under self.surface
	def load(self):
		self.surface = pygame.Surface((self.width, self.height)) #create empty pygame surface
		self.surface.fill(self.fill_colour) #fills background with fill_colour colour
		self.surface = self.surface.convert() #convert surface to make blitting faster. Just a thing you do.

	#simple formula for horizontally centering surfaces on other surfaces. Looks at the surface width and calculates accordingly.
	def horizontal_centre(self, nest):
		return (self.surface.get_width()-nest.get_width())/2

	#formula for vertically centering one surface onto another.
	def vertical_centre(self, nest):
		return (self.surface.get_height()-nest.get_height())/2

	#makes a text object. I'd like to flesh this out in the future for nicer text.
	#render creates an image of the text and then blits it.
	#render arguments are (text, antialiasing, text colour, background colour).
	def make_text(self, string):
		text = self.font.render(string, True, self.text_colour, self.fill_colour)
		return text

	#draws the base bordered screen
	#blit arguments are (source, destination, area, special flags)
	def draw_screen(self, width):
		self.surface.fill(self.fill_colour)
		t = self.make_text(self.title)
		x = 5
		y = self.surface.get_height() - x
		z = self.surface.get_width() - x
		pygame.draw.line(self.surface, self.text_colour, (x,x), (x,y), width)
		pygame.draw.line(self.surface, self.text_colour, (x,x), (z,x), width)
		pygame.draw.line(self.surface, self.text_colour, (z,x), (z,y), width)
		pygame.draw.line(self.surface, self.text_colour, (x,y), (z,y), width)
		self.surface.blit(t, (self.horizontal_centre(t),0))

	#the 5 in th render function is arbitrary. Could be changed to be an attribute of the class.
	def render(self, screen):
		self.draw_screen(5)
		screen.blit(self.surface, (self.x,self.y))