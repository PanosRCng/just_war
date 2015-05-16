

class Pointer():


	def __init__(self):

		self.x = 1
		self.y = 0

		self.direction = 2


	def update(self, speed_x, speed_y):

		if speed_x != 0:

			if speed_x > 0:
				self.direction = 2
			else:
				self.direction = 1

		elif speed_y != 0:

			if speed_y > 0:
				self.direction = 4
			else:
				self.direction = 3	
				
		
