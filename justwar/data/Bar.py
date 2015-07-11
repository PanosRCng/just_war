import pygame
from justwar.data.GameElement import GameElement


class Bar(GameElement):

	def __init__(self, x, y):

		GameElement.__init__(self)

		self.x = x
		self.y = y

		self.barShape = self.load_image_scaled("bar.png", 1.0)
		self.barRect = pygame.Rect( (x,y), (self.barShape.get_width(), self.barShape.get_height()) )

	def Show(self, surface):

		surface.blit(self.barShape, (self.barRect[0], self.barRect[1]))	

		for i in range((self.value/10)):

			beatRect = pygame.Rect( (self.x+5 + (i)*self.beat_width, self.y+3), (self.beat_width, self.beat_height) )
			surface.blit(self.beatShape, (beatRect[0], beatRect[1]))


class HealthBar(Bar):

	def __init__(self, x, y):
		super(HealthBar, self).__init__(x, y)

		self.value = 200

		self.beatShape = self.load_image_scaled("health_beat.png", 1.0)
		self.beat_width = self.beatShape.get_width()
		self.beat_height = self.beatShape.get_height()


class ForceBar(Bar):

	def __init__(self, x, y):
		super(ForceBar, self).__init__(x, y)

		self.value = 200

		self.beatShape = self.load_image_scaled("force_beat.png", 1.0)
		self.beat_width = self.beatShape.get_width()
		self.beat_height = self.beatShape.get_height()



