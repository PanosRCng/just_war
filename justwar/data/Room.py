import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from justwar.data.Background import Background
from justwar.data.Gate import Gate
from justwar.data.Stone import Stone

gateList = []
stoneList = []

class Room(GameElement):

	def __init__(self):

		GameElement.__init__(self)

		stoneList[:] = []
		gateList[:] = []

		self.Field = Background("field.png", (0,0))

		for i in range(0, Config.NUMBER_OF_GATES):
			gateList.append( Gate(i) ) 

		for i in range(0, Config.NUMBER_OF_STONES):
			stoneList.append( Stone() )


	def Show(self, surface):

		self.Field.Show(surface)

		for gate in gateList:
			gate.Show(surface)

		for stone in stoneList:
			stone.Show(surface)


