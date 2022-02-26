from constants import *
from numpy import sign
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, *groups):
		super().__init__(*groups)
		self.image = pygame.Surface((32, 32))
		self.image.fill(C_WHITE)
		self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
		self.rect.bottom = y
		self.rect.centerx = x
		self.velocity = 0
		self.direction = 0		

	def update(self, dt):
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
	
	def move(self, keys):
		if keys[K_LEFT] and keys[K_RIGHT]:
			pass
		elif keys[K_LEFT]:
			self.direction = -1
		elif keys[K_RIGHT]:
			self.direction = 1
		else:
			self.direction = 0