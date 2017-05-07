import pygame

#needs to be written to allow for inheritence, the nest attribute needs to change to a child attribute
class Container:
	def __init__(self, name, x, y, z, offset, width, height, colour, border, visible, active):
		self.name = name
		self.x = x+offset[0]
		self.y = y+offset[1]
		self.z = z
		self.offset = offset
		self.width = width*offset[2]
		self.height = height*offset[3]
		self.colour = colour
		self.border = border
		self.visible = visible
		self.active = active
		self.children = []

	def __repr__(self):
		return self.name

	def render(self, display):
		if self.visible == True:
			pygame.draw.rect(display, self.colour, (self.x,self.y,self.width,self.height),self.border)
			for c in self.children:
				c.render(display)


	def set_visible(self):
		if self.visible == False:
			self.visible = True
			for c in self.children:
				c.set_visible()
		else:
			self.visible = False
			for c in self.children:
				c.set_visible()

class Button(Container):
	def __init__(self, name, x, y, z, offset, width, height, colour, border, visible, active):
		Container.__init__(self, name, x, y, z, offset, width, height, colour, border, visible, active)

	def render(self, display):
		if self.visible == True and self.active == False:
			pygame.draw.rect(display, self.colour, (self.x,self.y,self.width,self.height),self.border)
			for c in self.children:
				c.render(display)
		elif self.visible == True and self.active == True:
			pygame.draw.rect(display, self.colour, (self.x,self.y,self.width,self.height),5)
			for c in self.children:
				c.render(display)
		else:
			pass

