from constants import *
import math
import random
import pygame
from typing import Dict, List

class Background:
	def __init__(self, screen: pygame.Surface) -> None:
		self.stars: List[Dict] = []
		self.screen = screen

		for _ in range(STARCOUNT):
			self.stars.append({
				'x': random.randint(-SCREEN_HALF_WIDTH, SCREEN_HALF_WIDTH), 
				'y': random.randint(0, SCREEN_HEIGHT), 
				'depth': random.randint(1, STAR_MAX_DEPTH)
			})

	def update(self, playerpos: int) -> None:
		playerpos = -playerpos + SCREEN_HALF_WIDTH
		self.screen.fill(C_BLACK)
		for star in self.stars:
			radius = math.ceil((star['depth'] / STAR_MAX_DEPTH) * STAR_SIZE)
			x = (star['x'] + playerpos * (star['depth'] / STAR_MAX_DEPTH) * 0.1) + SCREEN_HALF_WIDTH
			y = star['y']
			star['y'] += (star['depth'] / STAR_MAX_DEPTH) * STAR_SPEED
			if star['y'] - radius > SCREEN_HEIGHT:
				star['y'] = random.randint(-SCREEN_HALF_HEIGHT, 0)
				star['x'] = random.randint(-SCREEN_HALF_WIDTH, SCREEN_HALF_WIDTH)
				star['depth'] = random.randint(1, STAR_MAX_DEPTH)
			pygame.draw.rect(self.screen, C_WHITE, (x, y, radius, radius))