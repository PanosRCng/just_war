import pygame
from justwar.data.Config import Config
from justwar.data.Warrior import Warrior
from justwar.data.Fire import Fire
from random import randint
from math import sqrt
from math import copysign

class EnemyGhost(Warrior):


	def __init__(self):
		super(EnemyGhost, self).__init__("warrior2", [randint(Config.screenWidth-700,Config.screenWidth-100), 
									randint(Config.screenHeight-400,Config.screenHeight-100)])

		self.speed_x = randint(50,100)
		self.speed_y = randint(50,100)
		self.life = 20
		self.inDanger = False
		
		# 1 for aggressive / 0 for defensive
		self.personality = randint(0,1)

	def Move(self, time):
		super(EnemyGhost, self).Move(self.speed_x, self.speed_y, time)

		if (self.inDanger == True):
			self.speed_x = (copysign(1,self.speed_x)) * randint(150,180)
			self.speed_y = (copysign(1,self.speed_y)) * randint(150,180)
		else:
			#change speed and direction randomly
			random_num = randint(0,200)
			if (random_num == 90):
				self.speed_x = (copysign(1,self.speed_x)) * randint(0,100)
				self.speed_y = 0
			elif (random_num == 1):
				self.speed_y = (copysign(1,self.speed_y)) * randint(0,100)
				self.speed_x = 0
			elif (random_num == 10):
				self.speed_x = -1 * (copysign(1,self.speed_x)) * randint(0,100)
				self.speed_y = 0
			elif (random_num == 12):
				self.speed_y = -1 * (copysign(1,self.speed_y)) * randint(0,100)
				self.speed_x = 0
			elif (random_num == 54):
				self.speed_x = (copysign(1,self.speed_x)) * randint(0,100)
				self.speed_y = (copysign(1,self.speed_y)) * randint(0,100)
			elif (random_num == 53):
				self.speed_x = -1 * (copysign(1,self.speed_x)) * randint(0,100)
				self.speed_y = -1 * (copysign(1,self.speed_y)) * randint(0,100)
		

		# bouncing at walls
		if ( self.rect[0] >= self.max_coord[0] or self.rect[0] <= self.min_coord[0] ):
			self.speed_x = -self.speed_x
		if ( self.rect[1] >= self.max_coord[1] or self.rect[1] <= self.min_coord[1] ):
			self.speed_y = -self.speed_y


	def Fire(self):	
		self.fireForce = self.fireForce - 10

		if self.firespeed != 0:
			shot = Fire("fire_blue", (self.rect[0], self.rect[1]+(self.height/2)), self.firespeed, "x")
		else:
			shot = Fire("fire_blue", (self.rect[0]+(self.width/2), self.rect[1]), self.firespeed_y, "y")

		return shot


	def checkArea(self, warrior_x, warrior_y):
		self.criticalDistance = sqrt(pow(warrior_x - self.x, 2) + pow(warrior_y - self.y, 2))

		x_dist = warrior_x-self.x
		y_dist = warrior_y-self.y

		warrior_x_direction =0
		warrior_y_direction = 0

		if abs(x_dist) > 20:
			warrior_x_direction = copysign(1,(x_dist))

		if abs(y_dist) > 20:
			warrior_y_direction = copysign(1,(y_dist))

		if (self.criticalDistance <= 400) and (self.criticalDistance >= 100):
			self.inDanger = True

			#change personality randomly
			if randint(0,100) == 10:
				# 1 for aggressive / 0 for defensive
				self.personality = randint(0,1)

			if self.personality == 0:
				warrior_x_direction = -1 * warrior_x_direction
				warrior_y_direction = -1 * warrior_y_direction

			self.speed_x = warrior_x_direction * abs(self.speed_x)
			self.speed_y = warrior_y_direction * abs(self.speed_y)

		elif self.criticalDistance < 100:

			self.speed_x = warrior_x_direction * 1
			self.speed_y = warrior_y_direction * 1

		else:
			self.inDanger = False
			self.speed_x = (copysign(1,self.speed_x)) * randint(0,100)
			self.speed_y = (copysign(1,self.speed_y)) * randint(0,100)



