import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from justwar.data.Pointer import Pointer
from justwar.data.Fire import Fire
from math import copysign
from justwar.data.Room import stoneList

class Warrior(GameElement):

	ratio_map = [ 0.4, 0.5, 0.55, 0.6, 0.7, 0.75, 0.8, 0.9, 1.0, 1.1, 1.2 ]

	def __init__ (self, imagefile, coord, sizeType):

		GameElement.__init__(self)

		ratio = self.ratio_map[sizeType]

		# initially load all shapes -- fewer disk I/O during the game
		self.shapes = { 2 : self.load_image_scaled(imagefile+".png", ratio), 
				4 : self.load_image_scaled(imagefile+"_front"+".png", ratio),
				1 : self.load_image_scaled(imagefile+"_neg"+".png", ratio),
				3 : self.load_image_scaled(imagefile+"_back"+".png", ratio),
				6 : self.load_image_scaled(imagefile+"_shield"+".png", ratio),
				8 : self.load_image_scaled(imagefile+"_shield"+"_front"+".png", ratio),
				5 : self.load_image_scaled(imagefile+"_shield"+"_neg"+".png", ratio),
				7 : self.load_image_scaled(imagefile+"_shield"+"_back"+".png", ratio) }

		self.x = 0
		self.y = 0
		self.firespeed = 800
		self.fireForce = 100
		self.shieldForce = 0
		self.life = 200

		self.speed_x = 0
		self.speed_y = 0

		self.pointer = Pointer()

		self.__Shaping(self.shapes[2], coord)


	def Show(self, surface):

		if self.shieldForce > 0:
			self.__Shaping(self.shapes[ (self.pointer.direction) + 4 ], (self.x, self.y))
		else:
			self.__Shaping(self.shapes[self.pointer.direction], (self.x, self.y))

		surface.blit(self.shape, (self.rect[0], self.rect[1]))


	def Move(self, speed_x, speed_y, time):
		distance_x = speed_x * time
		distance_y = speed_y * time

		old_x = self.rect[0]
		old_y = self.rect[1]

		self.rect.move_ip(distance_x, distance_y)

		# update pointer direction
		self.pointer.update(speed_x, speed_y)

		for i in (0,1):
			if self.rect[i] < self.min_coord[i]:
				self.rect[i] = self.min_coord[i]
			if self.rect[i] > self.max_coord[i]:
				self.rect[i] = self.max_coord[i]

		for stone in stoneList:
			if stone.rect.colliderect(self.rect):
				self.rect[0] = old_x
				self.rect[1] = old_y

				# fix the "trap inside a stone"
				while stone.rect.colliderect(self.rect):
					self.rect[0] = self.rect[0] - 2
					self.rect[1] = self.rect[1] - 2

		self.x = self.rect[0]
		self.y = self.rect[1]

		if self.shieldForce > 0:
			self.shieldForce = self.shieldForce - 10

		if self.fireForce <= 0:
			self.fireForce += 10


	def __Shaping(self, new_shape, coord):

	        self.shape = new_shape

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(coord,(self.width, self.height))
		self.min_coord = (Config.terrain_min_width, Config.terrain_min_height-self.height)
		self.max_coord = (Config.terrain_max_width-self.width, Config.terrain_max_height-self.height)






