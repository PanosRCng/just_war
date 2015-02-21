import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from math import copysign
from justwar.data.Room import stoneList

class Fire(GameElement):

	def __init__(self, imagefile, coord, speed, direction):

		GameElement.__init__(self)

		self.direction = direction
		self.speed = speed
		self.imagefile = imagefile
		self.moveCounter = 0
		self.boomCounter = 0

		# initially load all shapes -- fewer disk I/O during the game
		if self.direction == "x":
			if self.speed < 0:
				self.shape = self.load_image(imagefile + "_neg.png")
			elif self.speed > 0:
				self.shape = self.load_image(imagefile + ".png")
		else:
			if self.speed < 0:
				self.shape = self.load_image(imagefile + "_up.png")
			elif self.speed > 0:
				self.shape = self.load_image(imagefile + "_down.png")

	        self.boomShape = self.load_image(self.imagefile + "_boom.png")

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(coord,(self.width, self.height))

	def Show(self, surface):
		surface.blit(self.shape, (self.rect[0], self.rect[1]))

	def Move(self, time):

		self.moveCounter = self.moveCounter + 1

		if self.boomCounter > 0:
			self.boomCounter = self.boomCounter + 1

		distance = self.speed * time

		if self.direction == "x":
			self.rect.move_ip(distance, 0)
		elif self.direction == "y":
			self.rect.move_ip(0, distance)

		if (self.rect[0] >= Config.screenWidth-70) or (self.rect[0] <= 70) or (self.rect[1] >= Config.screenHeight-70) or (self.rect[1] <= 0):
			self.Boom()

		for stone in stoneList:
			if stone.rect.collidepoint(self.GetXY()):
				self.Boom()


	def FadeOut(self):
		if self.moveCounter > 10:
			return True
		elif self.boomCounter > 3:
			return True
		else:
			return False

	def GetXY(self):
		return (self.rect[0], self.rect[1])

	def Boom(self):

		self.boomCounter = 1
		self.speed = (copysign(1,self.speed)) * 500

	        self.shape = self.boomShape
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(self.GetXY(),(self.width, self.height))


