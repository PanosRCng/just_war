import pygame
from justwar.data.GameElement import GameElement

class HealthBar(GameElement):

	def __init__(self, x, y):

		GameElement.__init__(self)

		self.health_value = 200

		self.x = x
		self.y = y

		self.barShape = self.load_image("health_bar.png")
		self.barRect = pygame.Rect( (x,y), (self.barShape.get_width(), self.barShape.get_height()) )

		self.beatShape = self.load_image("health_beat.png")
		self.beat_width = self.beatShape.get_width()
		self.beat_height = self.beatShape.get_height()


	def Show(self, surface):

		surface.blit(self.barShape, (self.barRect[0], self.barRect[1]))	

		for i in range((self.health_value/10)):

			beatRect = pygame.Rect( (self.x+5 + (i)*self.beat_width, self.y+3), (self.beat_width, self.beat_height) )
			surface.blit(self.beatShape, (beatRect[0], beatRect[1]))
