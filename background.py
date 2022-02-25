from constants import *
import random
import pygame

class Background:
	def __init__(self, screen):
		self.stars = []
		self.screen = screen

		for i in range(STARCOUNT):
			self.stars.append({
				'x': random.randint(-SCREEN_HALF_WIDTH, SCREEN_HALF_WIDTH), 
				'y': random.randint(0, SCREEN_HEIGHT), 
				'depth': random.randint(1, STAR_MAX_DEPTH)
			})

	def update(self, playerpos):
		playerpos = -playerpos + SCREEN_HALF_WIDTH
		self.screen.fill(C_BLACK)
		for star in self.stars:
			radius = max(1, (star['depth'] / STAR_MAX_DEPTH) * STAR_SIZE)
			x = (star['x'] + playerpos * (star['depth'] / STAR_MAX_DEPTH) * 0.1) + SCREEN_HALF_WIDTH
			y = star['y']
			star['y'] += (star['depth'] / STAR_MAX_DEPTH) * STAR_SPEED
			if star['y'] - radius > SCREEN_HEIGHT:
				star['y'] = random.randint(-SCREEN_HALF_HEIGHT, 0)
				star['x'] = random.randint(-SCREEN_HALF_WIDTH, SCREEN_HALF_WIDTH)
				star['depth'] = random.randint(1, STAR_MAX_DEPTH)
			pygame.draw.circle(self.screen, C_WHITE, (x, y), radius)