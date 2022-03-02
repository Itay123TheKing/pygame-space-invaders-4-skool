from enum import Enum
import random
from constants import *
import pygame
import animated_sprite
import random

class EnemyType(Enum):
	SQUID   = SMALL  = TYPE1 = 1
	CRAB    = MEDIUM = TYPE2 = 2
	OCTOPUS = LARGE  = TYPE3 = 3

class Enemy(animated_sprite.AnimatedSprite):
	def __init__(self, type: EnemyType, x: int, y: int, *groups: pygame.sprite.Group) -> None:
		super().__init__(ENEMIES[type.value - 1], ENEMY_COLOURKEY,
			ENEMY_WIDTH, ENEMY_HEIGHT,
			ENEMY_FRAMECOUNT, ENEMY_FPS, ENEMY_SCALE, *groups)

		self.type = type
		self.x = x
		self.y = y
		x_sign = random.choice([-1, 1])
		y_sign = random.choice([-1, 1])
		self.x_dir = x_sign * random.randint(5, 10)
		self.y_dir = y_sign * random.randint(5, 10)

	def move(self, x: int, y: int) -> None:
		self.x += x
		self.y += y
		self.rect.topleft = (self.x, self.y)

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, (self.x, self.y))

	def update(self) -> None:
		super().update()
		self.move(self.x_dir, self.y_dir)
		if self.x < 0 or self.x + self.image.get_width() > SCREEN_WIDTH:
			self.x_dir *= -1
		if self.y < 0 or self.y + self.image.get_height() > SCREEN_HEIGHT:
			self.y_dir *= -1