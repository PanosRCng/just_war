import pygame
from justwar.data.Config import Config
from justwar.data.Warrior import Warrior
from justwar.data.Fire import Fire
from random import randint
from math import sqrt
from math import copysign

class EnemyGhost(Warrior):


	def __init__(self):
		super(EnemyGhost, self).__init__("warrior2", [randint(Config.screenWidth-200,Config.screenWidth-100), 
									randint(0,Config.screenHeight)])
		self.speed_x = randint(0,100)
		self.speed_y = randint(0,100)
		self.firespeed = 600
		self.inDanger = False
		
		# 1 for aggressive / 0 for defensive
		self.personality = randint(0,1)
		

	def Move(self, time):
		super(EnemyGhost, self).Move(self.speed_x, self.speed_y, time)

		#change direction randomly
		if (randint(0,200) == 9):
			self.speed_x = - self.speed_x
		if (randint(0,200) == 10):
			self.speed_y = - self.speed_y

		# bouncing at walls
		if ( self.rect[0] >= self.max_coord[0] or self.rect[0] <= self.min_coord[0] ):
			self.speed_x = -self.speed_x
		if ( self.rect[1] >= self.max_coord[1] or self.rect[1] <= self.min_coord[1] ):
			self.speed_y = -self.speed_y


	def Fire(self):	
		self.fireForce = self.fireForce - 10
		shot = Fire("fire_blue", (self.rect[0], self.rect[1]+self.midheight), self.firespeed)
		return shot


	def checkArea(self, warrior_x, warrior_y):
		self.criticalDistance = sqrt(pow(warrior_x - self.x, 2) + pow(warrior_y - self.y, 2))

		if self.criticalDistance <= 400:
			self.inDanger = True

			# change personality randomly
			if randint(0,10) == 10:
				# 1 for aggressive / 0 for defensive
				self.personality = randint(0,1)

			warrior_x_direction = copysign(1,(warrior_x-self.x))
			warrior_y_direction = copysign(1,(warrior_y-self.y))

			if self.personality == 0:
				warrior_x_direction = -1 * warrior_x_direction
				warrior_y_direction = -1 * warrior_y_direction

			self.speed_x = warrior_x_direction * randint(100,150)
			self.speed_y = warrior_y_direction * randint(100,150)
		else:
			self.inDanger = False
			self.speed_x = (copysign(1,self.speed_x)) * randint(0,100)
			self.speed_y = (copysign(1,self.speed_y)) * randint(0,100)



