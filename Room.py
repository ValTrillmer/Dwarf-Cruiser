import numpy
import pygame

tiles = {0 : "floor", 1 : "wall"}

class Room:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.grid = self.make_grid()
		self.tiles = []
		self.define_walls()

	def make_grid(self):
		return numpy.zeros((self.width, self.height))

	def define_walls(self):
		for x in range(len(self.grid[0])-1):
			self.grid[0][x] = 1
		n = len(self.grid)-1
		for y in range(len(self.grid[n])-1):
			self.grid[n][y] = 1
		for x in self.grid:
			x[0], x[len(x)-1] = 1, 1
		print(self.grid)