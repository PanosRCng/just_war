import pygame
from sys import exit
from random import randint

from pygame.locals import *

from justwar.data.Config import Config
from justwar.data.Maze import Maze
from justwar.data.Room import Room 
from justwar.data.Room import gates
from justwar.data.Bar import HealthBar
from justwar.data.Bar import ForceBar
from justwar.data.Warrior import Warrior
from justwar.data.EnemyGhost import EnemyGhost
from justwar.data.WarriorGhost import WarriorGhost
from justwar.data.Drop import HealthDrop
from justwar.data.Drop import ForceDrop
from justwar.data.Room import stoneList

# put this in if android
from justwar.data.MoveKeyPad import MoveKeyPad
from justwar.data.PowerKeyPad import PowerKeyPad

# easy porting to android using the pygame subset for android
# import the android module, if can't import it, set it to none
try:
	import android
except ImportError:
	android = None



# main program

def main():

	pygame.init()

	screen = pygame.display.set_mode((Config.screenWidth, Config.screenHeight))
	#screen = pygame.display.set_mode( (screenWidth,screenHeight), DOUBLEBUF, 32)
	pygame.display.set_caption(Config.gameName)
	pygame.key.set_repeat(1,1)

	Map = Maze()

	CurrentRoom = Room(Map.getPathWays())

	# mapping Android keycodes to Pygame keysyms
	if android:
	        android.init()
	        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
	        android.map_key(android.KEYCODE_K, pygame.K_k)
	        android.map_key(android.KEYCODE_L, pygame.K_l)
	        android.map_key(android.KEYCODE_A, pygame.K_a)
	        android.map_key(android.KEYCODE_D, pygame.K_d)
	        android.map_key(android.KEYCODE_W, pygame.K_w)
	        android.map_key(android.KEYCODE_S, pygame.K_s)

	# put this in if android
	if android:
		MoveKeyPad1 = MoveKeyPad(10, 400)
		PowerKeyPad1 = PowerKeyPad(800, 400)

	WarriorGhost1 = WarriorGhost()

	HealthBar1 = HealthBar(10, 10)
	ForceBar1 = ForceBar(10, 27)

	clock = pygame.time.Clock()

	firelist = []

	enemies = []

	enemyFirelist = []

	drops = []

	if android:
		touchedKeys = []


	while True:
		time = clock.tick(Config.framerate)/1000.0

		# Android-specific:
        	if android:
            		if android.check_pause():
                		android.wait_for_resume()


		# enemy recreation - revolution
		
		if not enemies:
			for i in range(0, Config.NUMBER_OF_ENEMIES):
				enemies.append( EnemyGhost() )			



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
					WarriorGhost1.speed_x = -300
				if key[K_d]:
					WarriorGhost1.speed_x = +300
				if key[K_w]:
					WarriorGhost1.speed_y = -300
				if key[K_s]:
					WarriorGhost1.speed_y = +300
				if key[K_k]:
					if WarriorGhost1.fireForce > 0:
						firelist.append( WarriorGhost1.Fire() )
				if key[K_l]:
					WarriorGhost1.shieldForce = 100

			if android:
				if event.type == pygame.MOUSEBUTTONDOWN:

         				for i in MoveKeyPad1.keyArray:
           					if i[1].collidepoint(event.pos):

							touchedKeys.append(i[2])

         				for j in PowerKeyPad1.keyArray:
           					if j[1].collidepoint(event.pos):

							touchedKeys.append(j[2])

				if event.type==pygame.MOUSEBUTTONUP:

					touchedKeys = []


		if android:

			for i in touchedKeys:
				if i == 'w':
					WarriorGhost1.speed_y = -400
				elif i == 's':
					WarriorGhost1.speed_y = +400
				elif i == 'a':
					WarriorGhost1.speed_x = -400
				elif i == 'd':
					WarriorGhost1.speed_x = +400
				elif i == 'k':
					if WarriorGhost1.fireForce > 0:
						firelist.append( WarriorGhost1.Fire() )
				elif i == 'l':
					WarriorGhost1.shieldForce = 100

		# move

		WarriorGhost1.Move(time)			

		if WarriorGhost1.throughGate != -1:

			Map.throughPathWay(WarriorGhost1.throughGate)

			CurrentRoom = Room(Map.getPathWays())

			firelist[:] = []
			enemies[:] = []
			enemyFirelist[:] = []
			drops[:] = []

			if WarriorGhost1.throughGate == 0:
					WarriorGhost1.x = gates[2].rect[0]+WarriorGhost1.width
					WarriorGhost1.y = gates[2].rect[1]-WarriorGhost1.height-10
			elif WarriorGhost1.throughGate == 1:
					WarriorGhost1.x = gates[3].rect[0]+gates[3].rect[2] + 10
					WarriorGhost1.y = gates[3].rect[1]+WarriorGhost1.height
			elif WarriorGhost1.throughGate == 2:
					WarriorGhost1.x = gates[0].rect[0]+WarriorGhost1.width
					WarriorGhost1.y = gates[0].rect[1]+WarriorGhost1.height+10
			elif WarriorGhost1.throughGate == 3:
					WarriorGhost1.x = gates[1].rect[0]-WarriorGhost1.width-10
					WarriorGhost1.y = gates[1].rect[1]+WarriorGhost1.height

			WarriorGhost1.throughGate = -1

		# show		

		CurrentRoom.Show(screen)

		if android:
			MoveKeyPad1.Show(screen)
			PowerKeyPad1.Show(screen)

		HealthBar1.value = WarriorGhost1.life
		HealthBar1.Show(screen)

		ForceBar1.value = WarriorGhost1.life
		ForceBar1.Show(screen)

		WarriorGhost1.Show(screen)

		for enemy in enemies:

			enemy.checkArea(WarriorGhost1.x, WarriorGhost1.y)
			enemy.Move(time)
			enemy.Show(screen)

			if enemy.inDanger:

				if enemy.personality == 1:
					# do some probability math here
					if randint(0,10) == 9:
						if enemy.fireForce > 0:
							enemyFirelist.append( enemy.Fire() )
				elif enemy.personality == 0:
					enemy.shieldForce = 100

		for stone in stoneList:
			if (stone.broken) and not (stone.wastedDrop):
				drops.append( ForceDrop( stone.GetXY() ) )
				stone.wastedDrop = True

		for drop in drops:

			drop.Show(screen)

			if WarriorGhost1.rect.collidepoint( drop.GetXY() ):

				WarriorGhost1.life = 200
				drops.remove(drop)


		# fast moving objects -- collisions

		for shot in firelist:
			shot.Move(time)
			shot.Show(screen)

			if shot.FadeOut():
				firelist.remove(shot)
			else:
				for enemy in enemies:
					if enemy.rect.collidepoint(shot.GetXY()):
						shot.Boom()
						if enemy.shieldForce == 0:
							enemy.life -= 10

						if enemy.life < 0:
							drops.append( HealthDrop( (enemy.x, enemy.y) ) )
							enemies.remove(enemy)

		for shot in enemyFirelist:
			shot.Move(time)
			shot.Show(screen)

			if shot.FadeOut():
				enemyFirelist.remove(shot)
			else:
				if WarriorGhost1.rect.collidepoint(shot.GetXY()):
					shot.Boom()
					if WarriorGhost1.shieldForce == 0:
						WarriorGhost1.life -= 10

					if WarriorGhost1.life <= 0: 
						#return
						WarriorGhost1 = WarriorGhost()

		pygame.display.update()

if __name__ == "__main__":

	main()



