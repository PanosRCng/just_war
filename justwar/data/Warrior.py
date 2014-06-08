import pygame
from justwar.data.GameElement import GameElement
from justwar.data.Fire import Fire
from math import copysign

class Warrior(GameElement):

	def __init__ (self, imagefile, coord, min_coord, max_coord):

		GameElement.__init__(self)

	        self.shape = self.load_image(imagefile+".png")
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(coord,(self.width, self.height))

		self.min_coord = min_coord
		self.max_coord = (max_coord[0]-self.width, max_coord[1]-self.height)
		self.midheight = self.height/2

		self.firespeed = 800

		self.imagefile = imagefile

		self.speed_x = 0
		self.x = 0
		self.y = 0

	def Show(self, surface):

		if self.speed_x < 0:
			self.shape = self.load_image(self.imagefile+"_neg.png")
		elif self.speed_x > 0:
			self.shape = self.load_image(self.imagefile+".png")
			
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect((self.x,self.y),(self.width, self.height))

		surface.blit(self.shape, (self.rect[0], self.rect[1]))

	def Move(self, speed_x, speed_y, time):
		distance_x = speed_x * time
		distance_y = speed_y * time

		self.rect.move_ip(distance_x, distance_y)

		self.speed_x = speed_x

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

	def Fire(self):
		shot = Fire("fire_red", (self.rect[0], self.rect[1]+self.midheight), self.firespeed)
		return shot

