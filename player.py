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
		

	def update(self, dir, dt):
		if dir == K_LEFT:
			self.velocity -= PLAYER_SPEEDUP * dt
		elif dir == K_RIGHT:
			self.velocity += PLAYER_SPEEDUP * dt
		else:
			self.velocity += -sign(self.velocity) * PLAYER_SLOWDOWN * dt
			if abs(self.velocity) < PLAYER_SLOWDOWN * dt:
				self.velocity = 0
	
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