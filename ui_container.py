#needs to be written to allow for inheritence, the nest attribute needs to change to a child attribute
class Container:
	def __init__(self, name, x, y, z, nest, width, height, border, visible):
		self.name = name
		self.x = x
		self.y = y
		self.z = z
		self.nest = nest
		self.width = width
		self.height = height
		self.border = border
		self.visible = visible

		if self.nest != None:
			self.x = x+nest.x
			self.y = y+nest.y

		if self.nest == None:
			self.width = 1280
			self.height = 720
		else:
			self.width = self.nest.width * self.width
			self.height = self.nest.height * self.height