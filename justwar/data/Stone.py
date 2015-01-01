import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from random import randint

class Stone(GameElement):

	def __init__(self):

		GameElement.__init__(self)

		self.shape = self.load_image("stone.png")
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		
		self.coord = ( randint(Config.screenWidth-900, Config.screenWidth-200), randint(Config.screenHeight-550,Config.screenHeight-110) )

		self.rect = pygame.Rect(self.coord,(self.width, self.height))


	def Show(self, surface):
		surface.blit(self.shape, self.coord)
