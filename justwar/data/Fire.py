import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from math import copysign
from justwar.data.Room import stoneList


class FireGen(GameElement):

	ratio_map = [ 0.4, 0.5, 0.55, 0.6, 0.7, 0.75, 0.8, 0.9, 1.0, 1.1, 1.2 ]

	def __init__(self, imagefile, speed, sizeType):

		GameElement.__init__(self)

		self.imagefile = imagefile
		self.speed = speed

		# initially load all shapes -- fewer disk I/O during the game
		self.shapes = { 
				2 : self.load_image_scaled(self.imagefile + '.png', self.ratio_map[sizeType]), 
				'boom' : self.load_image_scaled(self.imagefile + "_boom.png", self.ratio_map[sizeType])
			      }

		# rotate what can be rotated -- fewer disk I/O
		self.shapes[4] =  pygame.transform.rotate(self.shapes[2], -90)
		self.shapes[1] =  pygame.transform.rotate(self.shapes[2], 180)
		self.shapes[3] =  pygame.transform.rotate(self.shapes[2], 90)


	def Shot(self, warrior_rect, direction):

		return FireShot(self.shapes, self.speed, warrior_rect, direction)



class FireShot():

	def __init__(self, shapes, speed, warrior_rect, direction):

		self.shapes = shapes
		self.speed = speed
		self.direction = direction
		self.moveCounter = 0
		self.boomCounter = 0

		self.__Shaping( self.shapes[direction], (warrior_rect.centerx, warrior_rect.centery) )


	def Show(self, surface):
		surface.blit(self.shape, (self.rect[0], self.rect[1]))


	def Move(self, time):

		self.moveCounter = self.moveCounter + 1

		if self.boomCounter > 0:
			self.boomCounter = self.boomCounter + 1

		distance = pow(-1, self.direction) * self.speed * time

		if (self.direction == 1) or (self.direction == 2):
			self.rect.move_ip(distance, 0)
		elif (self.direction == 3) or (self.direction == 4):
			self.rect.move_ip(0, distance)

		if (self.rect.centerx > self.max_coord[0]) or (self.rect.centerx < self.min_coord[0]) or (self.rect.centery > self.max_coord[1]) or (self.rect.centery < self.min_coord[1]):
			self.Boom()

		for stone in stoneList:
			if stone.rect.collidepoint(self.GetXY()):
				if not stone.broken:
					self.Boom()
					stone.Hit()


	def FadeOut(self):
		if self.moveCounter > 40:
			return True
		elif self.boomCounter > 20:
			return True
		else:
			return False


	def GetXY(self):
		return (self.rect.centerx, self.rect.centery)


	def Boom(self):

		self.boomCounter = 1
		self.speed = (copysign(1,self.speed)) * 100

		self.__Shaping( self.shapes['boom'], (self.GetXY()) )


	def __Shaping(self, new_shape, coord):

	        self.shape = new_shape

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect( (coord[0]-(self.width/2), coord[1]-(self.height/2)), (self.width, self.height) )
		self.min_coord = (Config.terrain_min_width, 20)
		self.max_coord = (Config.terrain_max_width, Config.terrain_max_height)


