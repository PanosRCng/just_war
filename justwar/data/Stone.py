import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from random import randint

class Stone(GameElement):

	def __init__(self):

		GameElement.__init__(self)

		# determines the stone size
		size_offset = randint(0,30)

	        self.shape = pygame.transform.scale( self.load_image("stone.png"), (68-size_offset, 64-size_offset))
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		
		self.coord = ( randint(Config.screenWidth-800, Config.screenWidth-300), randint(Config.screenHeight-450,Config.screenHeight-210) )

		self.rect = pygame.Rect(self.coord,(self.width, self.height))


	def Show(self, surface):
		surface.blit(self.shape, self.coord)
