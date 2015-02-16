from random import randint
from justwar.data.Config import Config
from justwar.data.Graph import Graph
from justwar.data.Graph import Node
from justwar.data.Graph import Edge


class Maze():

	def __init__(self):

		self.N = Config.mapSize

		self.mazeMatrix = [[0 for x in range(self.N)] for x in range(self.N)] 	
		for i in range(0, self.N):
			for j in range(0, self.N):			
				self.mazeMatrix[i][j] = "__"

		self.mazeGraph = Graph()

		self.getMaze(self.N)

		self.printMatrix(self.N)

		#for node in self.mazeGraph.getAllNodes():
		#	print node.getLabel()
		#	
		#	for edge in self.mazeGraph.getEdges(node):
		#		print edge.getLabel()
		#print "\n"


		self.startNode = Node( (0,0) )
		self.endNode = Node( (self.N-1, self.N-1) )
		self.currentNode = self.startNode
		self.gate2edgeMap = self.mapEdges2Gates()


	# do one hop through a gate-edge
	def throughPathWay(self, gate):
		edge = self.gate2edgeMap[gate]

		self.currentNode = edge.getRightNode()
		self.gate2edgeMap = self.mapEdges2Gates()

		if self.currentNode.getLabel() == self.endNode.getLabel() :
			print "THIS IS THE END"


	# generates a maze using depth-first search on a NxN matrix
	def getMaze(self, N):

		currentNode = Node( (0,0) )

		testCounter = 0

		while True:

			if self.mazeGraph.findNode(currentNode) == False:
				self.mazeGraph.addNode(currentNode)

			testCounter+=1
			self.mazeMatrix[currentNode.getPos()[0]][currentNode.getPos()[1]] = str(testCounter)

			unvisited_neighbors = self.getNeighbors(currentNode)
	
			# dead end -- jump to a node with unvisited neighbors -- i you can not find, return
			if len(unvisited_neighbors) == 0:
			
				visited_nodes = self.mazeGraph.getAllNodes()
			
				for node in visited_nodes:

					unvisited_neighbors = self.getNeighbors(node)

					if len(unvisited_neighbors) > 0:
						currentNode = node
						testCounter+=100
						break

				if len(unvisited_neighbors) == 0:
					return

			nextNode = unvisited_neighbors[randint(0,len(unvisited_neighbors)-1)]

			self.mazeGraph.addNode(nextNode)	
			self.mazeGraph.addEdge( Edge(currentNode, nextNode) )

			currentNode = nextNode

		return


	# get a list with the unvisited neighbors nodes for a given node
	def getNeighbors(self, node):

		unvisited_neighbors = []

		row = node.getPos()[0]
		column = node.getPos()[1]

		possible_neighbors =  [(row-1, column), 
				      	   (row+1, column), 
				      	   (row, column-1), 
				      	   (row, column+1)]

		for neighbor in possible_neighbors:
			if (neighbor[0]>=0) and (neighbor[0]<self.N) and (neighbor[1]>=0) and (neighbor[1]<self.N):

				neighbor_node = Node(neighbor)

				if self.mazeGraph.findNode(neighbor_node) == False: 				
					unvisited_neighbors.append(neighbor_node)

		return unvisited_neighbors


	def getCurrentNode(self):
		return self.currentNode


	def getPathWays(self):
		return self.gate2edgeMap.keys()


	# returns a dictionary that maps the room's gates to graph's edges
	def mapEdges2Gates(self):

		gate2edgeMap = {}

		edges = self.mazeGraph.getEdges(self.currentNode)

		for edge in edges:

			pair_node = edge.getRightNode()

			# gate mapping: 0->up, 1->right, 2->down, 3->left
			if pair_node.getPos()[0] - self.currentNode.getPos()[0] > 0:
				gate2edgeMap[2] = edge
			elif pair_node.getPos()[0] - self.currentNode.getPos()[0] < 0:
				gate2edgeMap[0] = edge
			elif pair_node.getPos()[1] - self.currentNode.getPos()[1] > 0:
				gate2edgeMap[1] = edge
			elif pair_node.getPos()[1] - self.currentNode.getPos()[1] < 0:
				gate2edgeMap[3] = edge 

		return gate2edgeMap


	def printMatrix(self, N):

		print "\n"
		for i in range(0,N):
			str_row = ""
			for j in range(0,N):
				str_row += self.mazeMatrix[i][j] + "  "
			print str_row
		print "\n"


