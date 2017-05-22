import pygame
import Formatting_Data as F

#needs to be written to allow for inheritence, the nest attribute needs to change to a child attribute
class Container:
	def __init__(self, x, y, z, offset, width, height, visible, active):
		self.x = x+offset[0]
		self.y = y+offset[1]
		self.z = z
		self.offset = offset
		if isinstance(width, float) == True:
			self.width = width*offset[2]
		else:
			self.width = width
		if isinstance(height, float) == True:
			self.height = height*offset[3]
		else:
			self.height = height
		self.visible = visible
		self.active = active
		self.children = []
		self.border = 5
		self.colour = F.white

	def __repr__(self):
		pass

	def render(self, display):
		if self.visible == True:
			pygame.draw.rect(display, self.colour, (self.x,self.y,self.width,self.height),self.border)
			for c in self.children:
				c.render(display)

	#sets visibility for children. If not visible, its children won't be either
	def set_visible(self):
		self.visible = not self.visible
		for c in self.children:
			c.set_visible()

	def update_active(self):
		self.active = not self.active

	#centres text horizontally using offset data
	def centre_horizontal(self):
		x = (self.offset[2]-self.width)/2
		self.x = x+self.offset[0]

	#centres text vertically using offset data
	def centre_vertical(self):
		y = (self.offset[3]-self.height)/2
		self.y = y+self.offset[1]



#for main game screen
class Main(Container):
	def __init__(self, x, y, z, offset, width, height, visible, active, name):
		Container.__init__(self, x, y, z, offset, width, height, visible, active)
		self.name = name



#for buttons, will probably have a lot more functionality
class Button(Container):
	def __init__(self, x, y, z, offset, width, height, visible, active, string):
		Container.__init__(self, x, y, z, offset, width, height, visible, active)
		self.font = F.font
		self.border = 0
		self.string = string #this string is for the text box
		self.create_text_box()

	def render(self, display):
		if self.visible == True and self.active == False:
			pygame.draw.rect(display, self.colour, (self.x,self.y,self.width,self.height),self.border)
			for c in self.children:
				c.render(display)
		elif self.visible == True and self.active == True:
			pygame.draw.rect(display, self.colour, (self.x,self.y,self.width,self.height),self.border)
			for c in self.children:
				c.render(display)

		else:
			pass

	def create_text_box(self):
		offset = (self.x,self.y,self.width,self.height)
		x = Text_Box(0,0,0,offset,0,0,False,False,self.string)
		x.centre_horizontal()
		x.centre_vertical()
		self.children.append(x)

	#set the active parameter and any rules that may result from the change.
	def update_active(self):
		if self.active == True:
			self.active = False
			self.border = 0
			c = self.children[0]
			c.text = c.font.render(c.string, True, c.text_colour, c.colour)
		else:
			self.active = True
			self.border = 5
			c = self.children[0]
			c.text = c.font.render(c.string, True, F.white, F.black)



#new class for creating text boxes. The button container calls it, but 
#other functions may as well
class Text_Box(Container):
	def __init__(self, x, y, z, offset, width, height, visible, active, string):
		Container.__init__(self, x, y, z, offset, width, height, visible, active)
		self.font = F.font
		self.border = 0
		self.string = string
		self.text_colour = F.black
		self.text = self.font.render(self.string, True, self.text_colour, self.colour)
		self.width = self.text.get_width()
		self.height = self.text.get_height()

	#makes a text object. I'd like to flesh this out in the future for nicer text.
	#render creates an image of the text and then blits it onto a surface or rect.
	#render arguments are (text, antialiasing, text colour, background colour).
	def render(self, display):
		if self.visible == True:
			display.blit(self.text, (self.x,self.y))
			for c in self.children:
				c.render(display)

	def update_colour(self, c1, c2):
		self.colour = c1
		self.text_colour = c2
		self.text = self.font.render(self.string, True, self.text_colour, self.colour)

	def set_text(self):
		self.text = self.font.render(self.string, True, self.text_colour, self.colour)