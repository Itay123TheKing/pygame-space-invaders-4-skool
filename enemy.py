from enum import Enum
from typing import Literal
from constants import *
import pygame
import animated_sprite

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

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(self.image, (self.x, self.y))