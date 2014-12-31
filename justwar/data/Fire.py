import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from math import copysign

class Fire(GameElement):

	def __init__(self, imagefile, coord, speed):

		GameElement.__init__(self)

		self.speed = speed
		self.imagefile = imagefile
		self.moveCounter = 0
		self.boomCounter = 0

		# initially load all shapes -- fewer disk I/O during the game
		if self.speed < 0:
			self.fireShape = self.load_image(imagefile + "_neg.png")
		elif self.speed > 0:
			self.fireShape = self.load_image(imagefile + ".png")

	        self.boomShape = self.load_image(self.imagefile + "_boom.png")

	        self.shape = self.fireShape
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
		self.rect.move_ip(distance, 0)

		if (self.rect[0] >= Config.screenWidth-70) or (self.rect[0] <= 70):
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


