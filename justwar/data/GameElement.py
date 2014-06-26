import os
import pygame

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
