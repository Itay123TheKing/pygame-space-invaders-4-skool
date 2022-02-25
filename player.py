from constants import *
from numpy import sign
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, *groups):
		super().__init__(*groups)
		self.image = pygame.Surface((32, 32))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
		self.rect.bottom = y
		self.rect.centerx = x
		self.velocity = 0
		

	def update(self, dir, dt):
		if dir == LEFT:
			self.velocity -= SPEEDUP * dt
		elif dir == RIGHT:
			self.velocity += SPEEDUP * dt
		else:
			self.velocity += -sign(self.velocity) * SLOWDOWN * dt
			if abs(self.velocity) < SLOWDOWN * dt:
				self.velocity = 0
	
		if self.velocity > MAX_VELOCITY:
			self.velocity = MAX_VELOCITY
		if self.velocity < -MAX_VELOCITY:
			self.velocity = -MAX_VELOCITY
		
		self.rect.move_ip(self.velocity, 0)
		if self.rect.left < 0:
			self.rect.left = 0
			self.velocity = 0
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
			self.velocity = 0