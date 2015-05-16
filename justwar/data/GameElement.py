import os
import pygame
from justwar.data.Utils import Utils

class GameElement(pygame.sprite.Sprite):


	def __init__(self):

		#constructor

		pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        

	def load_image(self, name):

		fullname = os.path.join('./data', name)

        	try:
        		shape = pygame.image.load(fullname)

        	except pygame.error, message:
            		print 'Cannot load image:', fullname
            		raise SystemExit, message

        	return shape


	def load_image_scaled(self, name, ratio):

		fullname = os.path.join('./data', name)

        	try:
        		shape = pygame.image.load(fullname)

			scaled_shape = Utils.scale(shape, ratio)

        	except pygame.error, message:
            		print 'Cannot load image:', fullname
            		raise SystemExit, message

        	return scaled_shape


		
