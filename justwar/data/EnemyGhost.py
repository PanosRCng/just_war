import pygame
from justwar.data.Warrior import Warrior
from justwar.data.Fire import Fire
from random import randint

class EnemyGhost(Warrior):

	def __init__(self, imagefile, coord, min_coord, max_coord, speed_x, speed_y):
		super(EnemyGhost, self).__init__(imagefile, coord, min_coord, max_coord)
		self.speed_x = speed_x
		self.speed_y = speed_y
		self.firespeed = 800
		
	def Move(self, time):
		super(EnemyGhost, self).Move(self.speed_x, self.speed_y, time)

		# change direction randomly and bouncing at walls
		if ( (self.rect[0] >= self.max_coord[0] or self.rect[0] <= self.min_coord[0]) or (randint(0,200) == 9) ):
			self.speed_x = -self.speed_x
		if ( (self.rect[1] >= self.max_coord[1] or self.rect[1] <= self.min_coord[1]) or (randint(0,200) == 10) ):
			self.speed_y = -self.speed_y

	def Fire(self):
		shot = Fire("fire_blue", (self.rect[0], self.rect[1]+self.midheight), self.firespeed)
		return shot
