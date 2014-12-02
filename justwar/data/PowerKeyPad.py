import pygame
from justwar.data.GameElement import GameElement

class PowerKeyPad(GameElement):

	def __init__(self, x, y):

		GameElement.__init__(self)

		self.keyArray = []

		letters = ['k','l']
		x_move = 0
		y_move = 0

		self.MakeKey( (x+0, y+50), 'k', 'keyFire.png')
		self.MakeKey( (x+120, y+50), 'l', 'keyShield.png')

	def MakeKey(self, coord, letter, imagefile):

		shape = self.load_image(imagefile)
		width = shape.get_width()
		height = shape.get_height()
		rect = pygame.Rect(coord,(width, height))		

		self.keyArray.append((shape, rect, letter))


	def Show(self, surface):

		for i in self.keyArray:
			surface.blit(i[0],i[1])

