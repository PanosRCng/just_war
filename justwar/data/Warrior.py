import pygame
from justwar.data.GameElement import GameElement
from justwar.data.Fire import Fire
from math import copysign

class Warrior(GameElement):

	def __init__ (self, imagefile, coord, min_coord, max_coord):

		GameElement.__init__(self)

		# initially load all shapes -- fewer disk I/O during the game
	        self.posShape = self.load_image(imagefile+".png")
	        self.negShape = self.load_image(imagefile+"_neg"+".png")
		self.posShieldShape = self.load_image(imagefile+"_shield"+".png")
		self.negShieldShape = self.load_image(imagefile+"_shield"+"_neg"+".png")

	        self.shape = self.posShape
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(coord,(self.width, self.height))

		self.min_coord = min_coord
		self.max_coord = (max_coord[0]-self.width, max_coord[1]-self.height)
		self.midheight = self.height/2

		self.firespeed = 800

		self.imagefile = imagefile

		self.x = 0
		self.y = 0

		self.shieldForce = 0


	def Show(self, surface):

		imagefile = self.imagefile

		if self.shieldForce > 0:
			if self.firespeed > 0:
				self.shape = self.posShieldShape
			elif self.firespeed < 0:
				self.shape = self.negShieldShape
		else:
			if self.firespeed > 0:
				self.shape = self.posShape
			elif self.firespeed < 0:
				self.shape = self.negShape

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect((self.x,self.y),(self.width, self.height))

		surface.blit(self.shape, (self.rect[0], self.rect[1]))

		if self.shieldForce > 0:
			self.shieldForce = self.shieldForce - 10


	def Move(self, speed_x, speed_y, time):
		distance_x = speed_x * time
		distance_y = speed_y * time

		self.rect.move_ip(distance_x, distance_y)

		# update fire direction
		if self.speed_x != 0:
			self.firespeed = (copysign(1,self.speed_x)) * abs(self.firespeed)

		for i in (0,1):
			if self.rect[i] < self.min_coord[i]:
				self.rect[i] = self.min_coord[i]
			if self.rect[i] > self.max_coord[i]:
				self.rect[i] = self.max_coord[i]

		self.x = self.rect[0]
		self.y = self.rect[1]


