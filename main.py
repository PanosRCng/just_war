import pygame
from sys import exit
from random import randint

from pygame.locals import *

from justwar.data.Background import Background
from justwar.data.Warrior import Warrior
from justwar.data.EnemyGhost import EnemyGhost
from justwar.data.WarriorGhost import WarriorGhost

# Import the android module. If we can't import it, set it to None - this
# lets us test it, and check to see if we want android-specific behavior.
try:
    import android
except ImportError:
    android = None



# main program

def main():

	pygame.init()

	# game parameters
	gameName = "Just War"
	NUMBER_OF_ENEMIES = 3
	screenWidth,screenHeight = (800,600)
	framerate = 60

	screen = pygame.display.set_mode((screenWidth, screenHeight))
	#screen = pygame.display.set_mode( (screenWidth,screenHeight), DOUBLEBUF, 32)
	pygame.display.set_caption(gameName)
	pygame.key.set_repeat(1,1)

	Field = Background("field.jpg", (0,0))

	# mapping between the android and the pygame keys.
	if android:
	        android.init()
	        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
	        android.map_key(android.KEYCODE_K, pygame.K_k)
	        android.map_key(android.KEYCODE_L, pygame.K_l)
	        android.map_key(android.KEYCODE_A, pygame.K_a)
	        android.map_key(android.KEYCODE_D, pygame.K_d)
	        android.map_key(android.KEYCODE_W, pygame.K_w)
	        android.map_key(android.KEYCODE_S, pygame.K_s)

	warriorGhost1_pos = (screenWidth/4,screenHeight/2)
	warrior_low = (0,0)
	warrior_high = (screenWidth, screenHeight)
	WarriorGhost1 = WarriorGhost("warrior1", warriorGhost1_pos, warrior_low, warrior_high)

	clock = pygame.time.Clock()

	firelist = []

	enemies = []

	enemyFirelist = []

	while True:
		time = clock.tick(framerate)/1000.0


		# Android-specific:
        	if android:
            		if android.check_pause():
                		android.wait_for_resume()


		# enemy recreation - revolution
		
		if not enemies:
			for i in range(0, NUMBER_OF_ENEMIES):
				enemies.append( EnemyGhost("warrior2", [randint(screenWidth-100,screenWidth), 
									randint(0,screenHeight)],
									warrior_low,
									warrior_high,
									randint(0,300),
									randint(0,300)) )			


		warriorGhostSpeed_x = 0
		warriorGhostSpeed_y = 0


		# handle input events

		for event in pygame.event.get():
			if event.type == QUIT:
				#pygame.quit()
				#exit()
				return

			if event.type == KEYDOWN:
				key = pygame.key.get_pressed()

				# quit the game if escape is pressed
				if key[K_ESCAPE]:
					#pygame.quit()
					#exit()
					return
				if key[K_a]:
					warriorGhostSpeed_x = -300
				if key[K_d]:
					warriorGhostSpeed_x = +300
				if key[K_w]:
					warriorGhostSpeed_y = -300
				if key[K_s]:
					warriorGhostSpeed_y = +300
				if key[K_k]:
					if len(firelist) < 1:
						firelist.append( WarriorGhost1.Fire() )
				if key[K_l]:
					WarriorGhost1.shieldForce = 100

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

			if shot.GoneOut(screenWidth):
				firelist.remove(shot)
			else:
				for enemy in enemies:
					if enemy.rect.collidepoint(shot.GetXY()):
						shot.Boom()
						enemies.remove(enemy)

		for shot in enemyFirelist:
			shot.Move(time)
			shot.Show(screen)

			if shot.GoneOut(screenWidth):
				enemyFirelist.remove(shot)
			else:
				if WarriorGhost1.rect.collidepoint(shot.GetXY()):
					shot.Boom()
					if WarriorGhost1.shieldForce == 0:
						return

		pygame.display.update()

if __name__ == "__main__":
	main()



