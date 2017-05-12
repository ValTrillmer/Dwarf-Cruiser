#contains the Window class, which holds drawing functions.
import pygame
from ui_container import Container, Main, Button

#The following functions create and modify surfaces.

#The following functions create displays with the drawing functions using input from the engine.

#Notes on creating and drawing on new surfaces. Draw new surface. Blit is putting a surface on a surface. First make text, then blit the text to the background,
	#then blit the background to the screen. This is just an example function. Be sure to assemble surfaces before
	#displaying them.

class Display:
	def __init__(self, width, height, title, x, y, z, font):
		self.width = width
		self.height = height
		self.title = title
		self.x = x
		self.y = y
		self.z = z
		self.font = font
		self.surface = None

	#creates a surface to draw on and stores it under self.surface
	def load(self):
		self.surface = pygame.Surface((self.width, self.height)) #create empty pygame surface
		self.surface.fill((0,0,0)) #fills background with colour1 colour
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
	def make_text(self, string, colour1, colour2):
		text = self.font.render(string, True, colour1, colour2)
		return text

	#creates the container object
	def make_container(self,x,y,z,width,height,visible,active,parent):
		if parent != None:
			offset = (parent.x,parent.y,parent.width,parent.height)
		else:
			offset = (0,0,1280,720)
		container = Container(x,y,z,offset,width,height,visible,active)
		if parent != None:
			parent.children.append(container)
		return container

	#for making main game container
	def make_main(self,x,y,z,width,height,visible,active,parent,name):
		if parent != None:
			offset = (parent.x,parent.y,parent.width,parent.height)
		else:
			offset = (0,0,1280,720)
		container = Main(x,y,z,offset,width,height,visible,active,name)
		if parent != None:
			parent.children.append(container)
		return container

	#function works just like the make container function, but it makes a button (a subclass of the
	#container Container class) instead. For the moment it works the same, but will alow for special
	#button animations and etc.
	def make_button(self,x,y,z,width,height,visible,active,parent):
		if parent != None:
			offset = (parent.x,parent.y,parent.width,parent.height)
		else:
			offset = (0,0,1280,720)
		container = Button(x,y,z,offset,width,height,visible,active,"123")
		if parent != None:
			parent.children.append(container)
		return container

	# runs through the container list and draws every container whose visibility is set to True
	def render(self, screen, main):
		self.surface.fill((0,0,0))
		if main.visible == True:
			main.render(self.surface)
		screen.blit(self.surface, (self.x,self.y))