# Remove pygame "Hello from the pygame community." message
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "something"

from enemies import Enemies
from hud import HUD
from constants import *
import pygame
import pygame.locals as locals
import pygame.font as font
from background import Background
from player import Player
from enemy import Enemy, EnemyType
from alpha_layer import AlphaLayer
from typing import Dict, List

pygame.init()
font.init()

def main():
	pygame.display.set_caption("Space Invaders")
	pygame.display.set_icon(pygame.image.load("assets/icon.png"))

	alpha_surf = AlphaLayer(SCREEN)

	clock = pygame.time.Clock()
	time_passed = 0
	player = Player(SCREEN_HALF_WIDTH, SCREEN_HEIGHT - 10)
	alpha_surf.bind(player, C_RED)

	# load previous HUD
	hud = HUD(PLAYER_SCORE_FILE, player, clock)
	hud.load()

	enemies = Enemies()
	for i in range(ENEMY_COUNT):
		enemies.add(Enemy(EnemyType(i % 3 + 1), SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT))
	
	alpha_surf.bind(enemies.group, C_GREEN)
	background = Background(SCREEN, player)

	while True:
		for event in pygame.event.get():
			if event.type == locals.QUIT:
				# Save the player's score
				hud.add(hex(id(player)), player.score)
				hud.save()

				return		

		dt = clock.tick(FPS) / 1000.0

		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE]: return
		player.move(keys)
		player.update(dt)
		
		background.update()

		alpha_surf.render_all_binded()
		alpha_surf.draw()


		player.draw(SCREEN)

		enemies.update()
		enemies.draw(SCREEN)

		hud.update(dt)
		hud.draw(SCREEN)

		pygame.display.flip()

		pygame.display.update()

if __name__ == "__main__":
	main()
	pygame.quit()
	font.quit()
				
	
			
	quit()