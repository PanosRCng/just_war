import pygame
from justwar.data.Config import Config
from justwar.data.Warrior import Warrior
from justwar.data.Fire import Fire
from justwar.data.Room import gateList

class WarriorGhost(Warrior):


	def __init__(self):
		super(WarriorGhost, self).__init__("warrior1", (Config.screenWidth/4,Config.screenHeight/2))
		self.speed_x = 0
		self.speed_y = 0
		self.firespeed = 800
		self.throughGate = -1

	def Move(self, time):
		super(WarriorGhost, self).Move(self.speed_x, self.speed_y, time)

		for gate in gateList:
			if gate.rect.colliderect(self.rect):
				self.throughGate = gate.direction

		self.speed_x = 0
		self.speed_y = 0


	def Fire(self):
		self.fireForce = self.fireForce - 100
		shot = Fire("fire_red", (self.rect[0], self.rect[1]+self.midheight), self.firespeed)
		return shot
