import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from justwar.data.Drop import ForceDrop
from random import randint

class Stone(GameElement):

	def __init__(self):

		GameElement.__init__(self)

		# determines the stone size
		size_offset = randint(0,30)

		self.coord = ( randint(Config.screenWidth-800, Config.screenWidth-300), randint(Config.screenHeight-450,Config.screenHeight-210) )

		# initially load all shapes -- fewer disk I/O during the game
	        self.shape = pygame.transform.scale( self.load_image("stone.png"), (68-size_offset, 64-size_offset))
		self.shape_hit = pygame.transform.scale( self.load_image("stone_hit.png"), (68-size_offset, 64-size_offset))
		self.shape_broken = pygame.transform.scale( self.load_image("stone_broken.png"), (68-size_offset, 64-size_offset))

		self.hits = 0
		self.broken = False
		self.wastedDrop = False

		self.__Shaping(self.shape)


	def Show(self, surface):
		surface.blit(self.shape, self.coord)

	
	def Hit(self):

		self.hits += 1

		if self.hits > 500:
			self.__Shaping(self.shape_broken)
			self.broken = True	
		elif self.hits > 50:
			self.__Shaping(self.shape_hit)	


	def GetXY(self):
		return (self.rect.centerx, self.rect.centery)


	def __Shaping(self, new_shape):

	        self.shape = new_shape

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(self.coord,(self.width, self.height))


