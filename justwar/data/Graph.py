########################
# a simple graph module
########################


# graph class
class Graph():


	def __init__(self):

		self.graph = {}	

	
	# returns a list with all the edges of a given node
	def getEdges(self, node): 

		edges = []

		for pair_node in self.getNodes(node):
			edges.append( Edge(node, pair_node) )	

		return edges

	
	# returns a list with all the 1-hop away, reachable nodes, for a given node
	def getNodes(self, node):

		nodes = []

		nodes_labels = self.graph[ node.getLabel() ]

		for node_label in nodes_labels:
			nodes.append( self.label2node(node_label) )
		
		return nodes


	# returns a list with all the nodes in the graph
	def getAllNodes(self):

		nodesList = []		

		nodeLabels = self.graph.keys()

		for nodeLabel in nodeLabels:

			nodesList.append( self.label2node(nodeLabel) )

		return nodesList


	# checks if a node is in the graph
	def findNode(self, node):

		if node.getLabel() in self.graph:
			return True
		else:
			return False


	# adds a node to the graph
	def addNode(self, node):
		self.graph[node.getLabel()] = []
		return True


	# adds an edge to the graph, between node1 and node2
	def addEdge(self, edge):

		if (self.findNode( edge.getLeftNode() )) and (self.findNode( edge.getRightNode() )):
			self.graph[ edge.getLeftNode().getLabel() ].append( edge.getRightNode().getLabel() )
			self.graph[ edge.getRightNode().getLabel() ].append( edge.getLeftNode().getLabel() )

			return True
		else:
			return False


	def label2node(self, node_label):
		pos_strs = node_label.split("_")
		return Node(( int(pos_strs[0]), int(pos_strs[1]) ))


# node class
class Node():

	def __init__(self, pos):

		self.pos = pos

	def getLabel(self):
		return str(self.pos[0]) + "_" + str(self.pos[1])

	def getPos(self):
		return (self.pos[0], self.pos[1])


# edge class (bi-directional)
class Edge():

	def __init__(self, leftNode, rightNode):

		self.leftNode = leftNode
		self.rightNode = rightNode

	def getLabel(self):
		return self.leftNode.getLabel() + "<-->" + self.rightNode.getLabel()		

	def getLeftNode(self):
		return self.leftNode

	def getRightNode(self):
		return self.rightNode



