from constants import *
import random
import pygame

class Background:
	def __init__(self, screen):
		self.stars = []
		self.screen = screen

		for i in range(STARCOUNT):
			self.stars.append({
				'x': random.randint(-HALFWIDTH, HALFWIDTH), 
				'y': random.randint(0, HEIGHT), 
				'depth': random.randint(1, MAXDEPTH)
			})

	def update(self, playerpos):
		playerpos -= HALFWIDTH
		for star in self.stars:
			size = 2 if star['depth'] < MAXDEPTH // 2 else 3
			x = (star['x'] + playerpos * (star['depth'] / MAXDEPTH) * 0.1) + HALFWIDTH
			y = star['y']
			star['y'] += (star['depth'] / MAXDEPTH) * STARSPEED
			if star['y'] > HEIGHT:
				star['y'] = random.randint(-HALFHEIGHT, 0)
				star['x'] = random.randint(-HALFWIDTH, HALFWIDTH)
				star['depth'] = random.randint(1, MAXDEPTH)
			pygame.draw.rect(self.screen, WHITE, (x, y, size, size))