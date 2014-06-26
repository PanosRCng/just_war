import pygame
from justwar.data.Warrior import Warrior
from justwar.data.Fire import Fire

class WarriorGhost(Warrior):

	def __init__(self, imagefile, coord, min_coord, max_coord):
		super(WarriorGhost, self).__init__(imagefile, coord, min_coord, max_coord)
		self.speed_x = 0
		self.speed_y = 0
		self.firespeed = 800

	def Move(self, time):
		super(WarriorGhost, self).Move(self.speed_x, self.speed_y, time)

		self.speed_x = 0
		self.speed_y = 0

	def Fire(self):
		shot = Fire("fire_red", (self.rect[0], self.rect[1]+self.midheight), self.firespeed)
		return shot


