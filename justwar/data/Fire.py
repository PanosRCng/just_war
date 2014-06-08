import pygame
from justwar.data.GameElement import GameElement
from math import copysign

class Fire(GameElement):

	def __init__(self, imagefile, coord, speed):

		GameElement.__init__(self)

		self.speed = speed
		self.imagefile = imagefile
		self.boomCounter = 0

		if self.speed < 0:
			imagefile = imagefile + "_neg.png"
		elif self.speed > 0:
			imagefile = imagefile + ".png"

	        self.shape = self.load_image(imagefile)
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(coord,(self.width, self.height))

	def Show(self, surface):
		surface.blit(self.shape, (self.rect[0], self.rect[1]))

	def Move(self, time):

		if self.boomCounter > 0:
			self.boomCounter = self.boomCounter + 1

		distance = self.speed * time	
		self.rect.move_ip(distance, 0)

	def GoneOut(self,x):
		if self.rect[0] >= x:
			return True
		elif self.rect[0] <= 0:
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

		imagefile = self.imagefile + "_boom.png"

	        self.shape = self.load_image(imagefile)
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(self.GetXY(),(self.width, self.height))


