from constants import *
import math
import random
import pygame
import player
from typing import List, Tuple

class Background:
	class Star:
		def __init__(self) -> None:
			self.x = random.randint(-SCREEN_HALF_WIDTH, SCREEN_HALF_WIDTH)
			self.y = random.randint(-SCREEN_HALF_HEIGHT, SCREEN_HEIGHT)
			self.depth = random.randint(1, STAR_MAX_DEPTH)
			self.size = math.ceil((self.depth / STAR_MAX_DEPTH) * STAR_SIZE)
			self.colour = random.choice(STAR_COLOURS)



		def to_screen_coords(self, player_x: int) -> Tuple[int, int]:
			return ((self.x + player_x * (self.depth / STAR_MAX_DEPTH) * .1) + SCREEN_HALF_WIDTH, self.y)

		def move(self) -> None:
			self.y += (self.depth / STAR_MAX_DEPTH) * STAR_SPEED

	def __init__(self, screen: pygame.Surface, player: player.Player) -> None:
		self.stars: List[self.Star] = [self.Star() for _ in range(STAR_COUNT)]
		self.screen = screen
		self.player = player

	def update(self) -> None:
		player_x = -self.player.rect.centerx + SCREEN_HALF_WIDTH
		self.screen.fill(C_BLACK)
		for star in self.stars:
			x, y = star.to_screen_coords(player_x)
			star.move()
			if star.y - star.size > SCREEN_HEIGHT:
				star = self.Star()
			pygame.draw.rect(self.screen, star.colour, (x, y, star.size, star.size))