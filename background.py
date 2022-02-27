from constants import *
import math
import random
import pygame
from typing import Dict, List

class Background:
	class Star:
		def __init__(self) -> None:
			self.x = random.randint(-SCREEN_HALF_WIDTH, SCREEN_HALF_WIDTH)
			self.y = random.randint(0, SCREEN_HEIGHT)
			self.depth = random.randint(1, STAR_MAX_DEPTH)
			self.size = math.ceil((self.depth / STAR_MAX_DEPTH) * STAR_SIZE)

	def __init__(self, screen: pygame.Surface) -> None:
		self.stars: List[Dict] = []
		self.screen = screen

		for _ in range(STARCOUNT):
			self.stars.append(self.Star())

	def update(self, playerpos: int) -> None:
		playerpos = -playerpos + SCREEN_HALF_WIDTH
		self.screen.fill(C_BLACK)
		for star in self.stars:
			x = (star.x + playerpos * (star.depth / STAR_MAX_DEPTH) * 0.1) + SCREEN_HALF_WIDTH
			y = star.y
			star.y += (star.depth / STAR_MAX_DEPTH) * STAR_SPEED
			if star.y - star.size > SCREEN_HEIGHT:
				star.y = random.randint(-SCREEN_HALF_HEIGHT, 0)
				star.x = random.randint(-SCREEN_HALF_WIDTH, SCREEN_HALF_WIDTH)
				star.depth = random.randint(1, STAR_MAX_DEPTH)
			pygame.draw.rect(self.screen, C_WHITE, (x, y, star.size, star.size))