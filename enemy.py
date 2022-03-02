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
			ENEMY_FRAMECOUNT, ENEMY_FPS, ENEMY_SCALE, *groups)

		self.type = type
		self.x_vel = random.randint(5, 10) * random.choice([-1, 1])
		self.y_vel = random.randint(5, 10) * random.choice([-1, 1])
		self.rect.x = x
		self.rect.y = y

	def move(self, x: int, y: int) -> None:
		self.rect.centerx += x
		self.rect.centery += y

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, (self.rect.topleft))
	
	def update(self):
		super().update()
		self.move(self.x_vel, self.y_vel)
		if self.rect.left < 0:
			self.rect.left = 0
			self.x_vel *= -1
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
			self.x_vel *= -1
		if self.rect.top < 0:
			self.rect.top = 0
			self.y_vel *= -1
		if self.rect.bottom > SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT
			self.y_vel *= -1
