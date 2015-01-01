import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from justwar.data.Background import Background
from justwar.data.Stone import Stone

stoneList = []

class Room(GameElement):

	def __init__(self):

		GameElement.__init__(self)

		self.Field = Background("field.png", (0,0))

		for i in range(0, Config.NUMBER_OF_STONES):
			stoneList.append(Stone())


	def Show(self, surface):

		self.Field.Show(surface)

		for stone in stoneList:
			stone.Show(surface)
