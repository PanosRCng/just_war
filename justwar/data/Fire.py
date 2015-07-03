import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from math import copysign
from justwar.data.Room import stoneList


class Fire(GameElement):


	def __init__(self, imagefile, warrior_rect, speed, direction):

		GameElement.__init__(self)

		self.direction = direction
		self.speed = speed
		self.imagefile = imagefile
		self.moveCounter = 0
		self.boomCounter = 0

		# initially load all shapes -- fewer disk I/O during the game
		self.shapes = { 2 : self.load_image(self.imagefile + '.png') }
	        self.boomShape = self.load_image(self.imagefile + "_boom.png")

		# rotate what can be rotated -- fewer disk I/O
		self.shapes[4] =  pygame.transform.rotate(self.shapes[2], -90)
		self.shapes[1] =  pygame.transform.rotate(self.shapes[2], 180)
		self.shapes[3] =  pygame.transform.rotate(self.shapes[2], 90)

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
				self.Boom()


	def FadeOut(self):
		if self.moveCounter > 20:
			return True
		elif self.boomCounter > 10:
			return True
		else:
			return False


	def GetXY(self):
		return (self.rect.centerx, self.rect.centery)


	def Boom(self):

		self.boomCounter = 1
		self.speed = (copysign(1,self.speed)) * 100

		self.__Shaping( self.boomShape, (self.GetXY()) )


	def __Shaping(self, new_shape, coord):

	        self.shape = new_shape

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect( (coord[0]-(self.width/2), coord[1]-(self.height/2)), (self.width, self.height) )
		self.min_coord = (Config.terrain_min_width, 20)
		self.max_coord = (Config.terrain_max_width, Config.terrain_max_height)


