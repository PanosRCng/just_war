import pygame
from justwar.data.Config import Config
from justwar.data.GameElement import GameElement
from justwar.data.Background import Background
from justwar.data.Maze import Maze
from justwar.data.Gate import Gate
from justwar.data.Stone import Stone

gates = {}
stoneList = []


class Room(GameElement):


	def __init__(self, pathWays):

		GameElement.__init__(self)

		self.Field = Background("field.png", (0,0))

		stoneList[:] = []
		gates.clear()

		# gate mapping: 0->up, 1->right, 2->down, 3->left
		for pathWay in pathWays:
			gates[pathWay] = Gate(pathWay)  

		for i in range(0, Config.NUMBER_OF_STONES):
			stoneList.append( Stone() )


	def Show(self, surface):

		self.Field.Show(surface)

		for gate in gates:
			gates[gate].Show(surface)

		for stone in stoneList:
			stone.Show(surface)


