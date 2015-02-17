import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from random import randint

class Gate(GameElement):

	def __init__(self, direction):

		GameElement.__init__(self)

		self.direction = direction

		self.shape = self.load_image("gate.png")
		self.coord = ( randint(Config.screenWidth-700, Config.screenWidth-300), 0 ) 

		if direction == 1:
			self.shape = pygame.transform.rotate(self.shape, -90)
			self.coord = ( Config.screenWidth-self.shape.get_width()-10, randint(Config.screenHeight-440, Config.screenHeight-300) )

		if direction == 2:
			self.shape = pygame.transform.rotate(self.shape, -180)
			self.coord = ( randint(Config.screenWidth-700, Config.screenWidth-300), Config.screenHeight-self.shape.get_height() )

		if direction == 3:
			self.shape = pygame.transform.rotate(self.shape, 90)
			self.coord = ( 0+10, randint(Config.screenHeight-440, Config.screenHeight-300) )

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()

		self.rect = pygame.Rect(self.coord,(self.width, self.height))


	def Show(self, surface):
		surface.blit(self.shape, self.coord)
