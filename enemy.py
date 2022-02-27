from typing import Literal
from constants import *
import pygame
import animated_sprite

class Enemy(animated_sprite.AnimatedSprite):
	def __init__(self, type: Literal[1, 2, 3], x: int, y: int, *groups: pygame.sprite.Group) -> None:
		if type not in VALID_ENEMIES:
			raise ValueError(f"Enemy type must be one of {VALID_ENEMIES}.")
		super().__init__(pygame.image.load(f'assets/sprites/enemy{type}.png').convert_alpha(), 
			ENEMY_COLOURKEY, ENEMY_WIDTH, ENEMY_HEIGHT, 
			ENEMY_FRAMECOUNT, ENEMY_FPS, ENEMY_SCALE, *groups)

		self.type = type
		self.x = x
		self.y = y

	def draw(self, surface: pygame.Surface) -> None:
		surface.blit(super().image, self.x, self.y)