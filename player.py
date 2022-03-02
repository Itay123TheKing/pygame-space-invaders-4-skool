from constants import *
from numpy import sign
import pygame
from animated_sprite import AnimatedSprite

class Player(AnimatedSprite):
	def __init__(self, x: int, y: int, *groups: pygame.sprite.Group) -> None:
		#super().__init__(pygame.image.load('assets/sprites/nyan_cat.png'),
		#(0, 255, 255), 50, 22, 5, 5, 1, *groups)
		super().__init__(ENEMIES[0], ENEMY_COLOURKEY,
			ENEMY_FRAMECOUNT, ENEMY_FPS, ENEMY_SCALE, *groups)
		self.rect.bottom = y
		self.rect.centerx = x
		self.velocity = 0
		self.direction = 0
		self.score = 0
		self.facing = 1

	def update(self, dt: float) -> None:
		super().update()
		if self.direction == 0:
			self.velocity += -sign(self.velocity) * PLAYER_SLOWDOWN * dt
			if abs(self.velocity) < PLAYER_SLOWDOWN * dt:
				self.velocity = 0
		else:
			self.velocity += self.direction * PLAYER_SPEEDUP * dt
	
		if self.velocity > PLAYER_MAX_VELOCITY:
			self.velocity = PLAYER_MAX_VELOCITY
		if self.velocity < -PLAYER_MAX_VELOCITY:
			self.velocity = -PLAYER_MAX_VELOCITY
		
		self.rect.move_ip(self.velocity, 0)
		if self.rect.left < 0:
			self.rect.left = 0
			self.velocity = 0
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
			self.velocity = 0
	
	def move(self, keys: dict) -> None:
		if keys[K_LEFT] and keys[K_RIGHT]:
			pass
		elif keys[K_LEFT]:
			self.direction = -1
			if self.direction != self.facing:
				self.flip(True, False)
				self.facing = self.direction
		elif keys[K_RIGHT]:
			self.direction = 1
			if self.direction != self.facing:
				self.flip(True, False)
				self.facing = self.direction
		else:
			self.direction = 0



	def addScore(self, score: int) -> None:
		self.score += score