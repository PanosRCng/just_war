import pygame
from justwar.data.Config import Config
from justwar.data.Warrior import Warrior
from justwar.data.Fire import FireGen
from justwar.data.Room import gates

class WarriorGhost(Warrior):

	def __init__(self):
		super(WarriorGhost, self).__init__("warrior1", (Config.screenWidth/4,Config.screenHeight/2), 8)

		self.throughGate = -1

		self.FireGen = FireGen("fire_red",  self.firespeed, self.sizeType)


	def Move(self, time):
		super(WarriorGhost, self).Move(self.speed_x, self.speed_y, time)

		for gate in gates.keys():
			if gates[gate].rect.colliderect(self.rect):
				self.throughGate = gates[gate].direction

		self.speed_x = 0
		self.speed_y = 0


	def Fire(self):
		
		self.fireForce = self.fireForce - 100

		return self.FireGen.Shot(self.rect, self.pointer.direction)



