import pygame
from justwar.data.GameElement import GameElement

class MoveKeyPad(GameElement):

	def __init__(self, x, y):

		GameElement.__init__(self)

		self.keyArray = []

		letters = ['w','s','a','d']
		x_move = 0
		y_move = 0

		self.MakeKey( (x+60, y+0), 'w', 'keyUp.png')
		self.MakeKey( (x+0, y+55), 'a', 'keyLeft.png')
		self.MakeKey( (x+104, y+55), 'd', 'keyRight.png')
		self.MakeKey( (x+60, y+100), 's', 'keyDown.png')

	def MakeKey(self, coord, letter, imagefile):

		shape = self.load_image(imagefile)
		width = shape.get_width()
		height = shape.get_height()
		rect = pygame.Rect(coord,(width, height))		

		self.keyArray.append((shape, rect, letter))


	def Show(self, surface):

		for i in self.keyArray:
			surface.blit(i[0],i[1])


