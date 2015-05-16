import pygame


class Utils:

	@staticmethod
	def scale(shape, ratio):

		width,height = shape.get_size()

		scaled_width = ratio * width
		scaled_height = ratio * height

		return pygame.transform.scale(shape, (int(scaled_width), int(scaled_height)))



