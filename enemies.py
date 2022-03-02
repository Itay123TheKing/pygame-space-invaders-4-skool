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
			enemy.update()

	def draw(self, surface: pygame.Surface) -> None:
		for enemy in self.enemies:
			enemy.draw(surface)