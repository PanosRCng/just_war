import pygame
from justwar.data.GameElement import GameElement


class HealthDrop(GameElement):


	def __init__(self, coord):

		GameElement.__init__(self)

		self.coord = coord

		self.shape = self.load_image("health_drop.png")

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(self.coord,(self.width, self.height))


	def Show(self, surface):
		surface.blit(self.shape, self.coord)


	def GetXY(self):
		return (self.rect.centerx, self.rect.centery)



class ForceDrop(GameElement):


	def __init__(self, coord):

		GameElement.__init__(self)

		self.coord = coord

		self.shape = self.load_image("force_drop.png")

		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(self.coord,(self.width, self.height))


	def Show(self, surface):
		surface.blit(self.shape, self.coord)


	def GetXY(self):
		return (self.rect.centerx, self.rect.centery)



