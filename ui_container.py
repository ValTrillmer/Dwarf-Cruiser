import pygame

#needs to be written to allow for inheritence, the nest attribute needs to change to a child attribute
class Container:
	def __init__(self, name, x, y, z, offset, width, height, border, visible):
		self.name = name
		self.x = x+offset[0]
		self.y = y+offset[1]
		self.z = z
		self.offset = offset
		self.width = width*offset[2]
		self.height = height*offset[3]
		self.border = border
		self.visible = visible
		self.children = []

	def render(self, display, colour):
		if self.visible == True:
			pygame.draw.rect(display, colour, (self.x,self.y,self.width,self.height),self.border)
			for c in self.children:
				c.render(display, colour)