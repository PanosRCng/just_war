import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from justwar.data.Fire import Fire
from math import copysign

class Warrior(GameElement):


	def __init__ (self, imagefile, coord):

		GameElement.__init__(self)

		# initially load all shapes -- fewer disk I/O during the game
	        self.posShape = pygame.transform.scale( self.load_image(imagefile+".png"), (33, 80))
	        self.negShape = pygame.transform.scale( self.load_image(imagefile+"_neg"+".png"), (33, 80) )
		self.posShieldShape = pygame.transform.scale( self.load_image(imagefile+"_shield"+".png"), (87, 100) )
		self.negShieldShape = pygame.transform.scale( self.load_image(imagefile+"_shield"+"_neg"+".png"), (87, 100) )

	        self.shape = self.posShape
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(coord,(self.width, self.height))

		self.min_coord = (Config.screenWidth-960, 0)
		self.max_coord = (Config.screenWidth-self.width-60, Config.screenHeight-self.height-70)
		self.midheight = self.height/2

		self.x = 0
		self.y = 0
		self.firespeed = 800
		self.fireForce = 100
		self.shieldForce = 0
		self.life = 200


	def Show(self, surface):

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

		if self.fireForce <= 0:
			self.fireForce += 10


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


