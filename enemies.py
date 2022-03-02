import pygame
from constants import *
from linked_list import LinkedList

class Enemies:
	"""
	- [ ] Enem*ies* class:
		- [ ] Linked list of enemies
		- [ ] Move all enemies (also check for collision with the edge)
		- [ ] Shoot
		- [ ] Cool effects with new alpha layer 
	"""
	def __init__(self):
		self.enemies = LinkedList()

	def add(self, enemy):
		self.enemies.push_back(enemy)
	
	def update(self):
		for enemy in self.enemies:
			enemy.move(enemy.x_dir, enemy.y_dir)
			if enemy.x < 0 or enemy.x + enemy.image.get_width() > SCREEN_WIDTH:
				enemy.x_dir *= -1
			if enemy.y < 0 or enemy.y + enemy.image.get_height() > SCREEN_HEIGHT:
				enemy.y_dir *= -1

	def draw(self, surface: pygame.Surface) -> None:
		for enemy in self.enemies:
			enemy.draw(surface)