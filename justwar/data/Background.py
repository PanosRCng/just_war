import pygame
from justwar.data.GameElement import GameElement

class Background(GameElement):

	def __init__(self, imagefile, coord):

		GameElement.__init__(self)

		self.shape = self.load_image(imagefile)
		self.coord = coord

	def Show(self, surface):
		surface.blit(self.shape, self.coord)

