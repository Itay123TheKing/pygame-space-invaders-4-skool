from enum import Enum
from typing import Literal
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
		self.dirx = random.choice([-1, 1])
		self.diry = random.choice([-1, 1])

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, (self.x, self.y))
	
	def update(self) -> None:
		super().update()
		self.x += ENEMY_SPEED * self.dirx
		self.y += ENEMY_SPEED * self.diry
		self.rect.x = self.x
		self.rect.y = self.y
		if self.rect.top < 0:
			self.rect.top = 0
			self.y = self.rect.y
			self.diry = -self.diry
		if self.rect.bottom > SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT
			self.y = self.rect.y
			self.diry = -self.diry
		if self.rect.left < 0:
			self.rect.left = 0
			self.x = self.rect.x
			self.dirx = -self.dirx
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
			self.x = self.rect.x
			self.dirx = -self.dirx
		
