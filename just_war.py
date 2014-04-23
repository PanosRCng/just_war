import pygame
from pygame.locals import *
from sys import exit
from random import randint

# classes

class Warrior(object):
	def __init__ (self, imagefile, coord, min_coord, max_coord):
		self.shape = pygame.image.load(imagefile)
		self.width = self.shape.get_width()
		self.height = self.shape.get_height()
		self.rect = pygame.Rect(coord,(self.width, self.height))
		self.min_coord = min_coord
		self.max_coord = (max_coord[0]-self.width, max_coord[1]-self.height)
		self.midheight = self.height / 2
		self.firecolor = (255,0,0)
		self.firespeed = 800
		self.shotlength = 10

	def Show(self, surface):
		surface.blit(self.shape, (self.rect[0], self.rect[1]))

	def Move(self, speed_x, speed_y, time):
		distance_x = speed_x * time
		distance_y = speed_y * time

		self.rect.move_ip(distance_x, distance_y)

		for i in (0,1):
			if self.rect[i] < self.min_coord[i]:
				self.rect[i] = self.min_coord[i]
			if self.rect[i] > self.max_coord[i]:
				self.rect[i] = self.max_coord[i]

	def Fire(self):
		shot = Fire((self.rect[0], self.rect[1]+self.midheight), self.firecolor, self.shotlength, self.firespeed)
		return shot


class WarriorGhost(Warrior):
	pass


class EnemyGhost(Warrior):
	def __init__(self, imagefile, coord, min_coord, max_coord, speed_x, speed_y):
		super(EnemyGhost, self).__init__(imagefile, coord, min_coord, max_coord)

		self.speed_x = speed_x
		self.speed_y = speed_y
		
		self.firespeed = -800
		self.firecolor = (0,0,255)
		
	def Move(self, time):
		super(EnemyGhost, self).Move(self.speed_x, self.speed_y, time)

		if self.rect[0] >= self.max_coord[0] or self.rect[0] <= self.min_coord[0]:
			self.speed_x = -self.speed_x
		if self.rect[1] >= self.max_coord[1] or self.rect[1] <= self.min_coord[1]:
			self.speed_y = -self.speed_y

	def Fire(self):
		shot = Fire((self.rect[0], self.rect[1]+self.midheight), self.firecolor, self.shotlength, self.firespeed)
		return shot


class Fire:
	def __init__(self, coord, color, size, speed):
		self.x1 = coord[0]
		self.y1 = coord[1]
		self.size = size
		self.color = color
		self.speed = speed

	def Show(self, surface):
		pygame.draw.line(surface, self.color, (self.x1,self.y1), (self.x1-self.size,self.y1),2)

	def Move(self, time):
		distance = self.speed * time
		self.x1 += distance	

	def GoneAbove(self,x):
		if self.x1 <= x:
			return True
		else:
			return False

	def GetXY(self):
		return (self.x1, self.y1)

class Background(object):
	def __init__(self, imagefile, coord):
		self.shape = pygame.image.load(imagefile)
		self.coord = coord

	def Show(self, surface):
		surface.blit(self.shape, self.coord)


# main program

def main():
	pygame.init()

	NUMBER_OF_ENEMIES = 2

	screenWidth,screenHeight = (800,500)

	screen = pygame.display.set_mode( (screenWidth,screenHeight), DOUBLEBUF, 32)
	pygame.display.set_caption("Just War")
	pygame.key.set_repeat(1,1)

	Field = Background("field.jpg", (0,0))

	warriorGhost1_pos = (100,250)
	warrior_low = (0,0)
	warrior_high = (screenWidth, screenHeight)
	WarriorGhost1 = WarriorGhost("warrior1.png", warriorGhost1_pos, warrior_low, warrior_high)

	clock = pygame.time.Clock()
	framerate = 60

	firelist = []

	enemies = []

	enemyFirelist = []

	while True:
		time = clock.tick(framerate)/1000.0


		# enemy recreation - revolution
		
		if not enemies:
			for i in range(0, NUMBER_OF_ENEMIES):
				enemies.append( EnemyGhost("warrior2.png", [randint(screenWidth-100,screenWidth), 
									randint(0,screenHeight)],
									warrior_low,
									warrior_high,
									randint(0,300),
									randint(0,300)) )			


		warriorGhostSpeed_x = 0
		warriorGhostSpeed_y = 0


		# check events

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()

			if event.type == KEYDOWN:
				key = pygame.key.get_pressed()

				if key[K_q]:
					pygame.quit()
					exit()
				if key[K_LEFT]:
					warriorGhostSpeed_x = -300
				if key[K_RIGHT]:
					warriorGhostSpeed_x = +300
				if key[K_UP]:
					warriorGhostSpeed_y = -300
				if key[K_DOWN]:
					warriorGhostSpeed_y = +300
				if key[K_SPACE]:
					firelist.append( WarriorGhost1.Fire() )


		# move

		WarriorGhost1.Move(warriorGhostSpeed_x, warriorGhostSpeed_y, time)			


		# show		

		Field.Show(screen)
		WarriorGhost1.Show(screen)

		for enemy in enemies:
			enemy.Move(time)
			enemy.Show(screen)

			# do some probability math here
			if randint(0,100) == 9:
				enemyFirelist.append( enemy.Fire() )


		# fast moving objects -- collisions

		for shot in firelist:
			shot.Move(time)
			shot.Show(screen)

			if shot.GoneAbove(0):
				firelist.remove(shot)
			else:
				for enemy in enemies:
					if enemy.rect.collidepoint(shot.GetXY()):
						firelist.remove(shot)
						enemies.remove(enemy)

		for shot in enemyFirelist:
			shot.Move(time)
			shot.Show(screen)

			if shot.GoneAbove(0):
				enemyFirelist.remove(shot)
			else:
				if WarriorGhost1.rect.collidepoint(shot.GetXY()):
					enemyFirelist.remove(shot)
					exit()

		pygame.display.update()

if __name__ == "__main__":
	main()



