# Remove pygame "Hello from the pygame community." message
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "something"

from constants import *
import pygame
import json
import pygame.locals as locals
import pygame.font as font
import colorsys
from background import Background
from player import Player
from enemy import Enemy, EnemyType
from alpha_layer import AlphaLayer
from typing import Dict, List

pygame.init()
font.init()

def main():
	highScores: List[Dict] = []
	# load previous scores

	fixJson = lambda: json.dump({"scores": []}, open(PLAYER_SCORE_FILE, "w"), indent="\t")
	
	if os.path.exists(PLAYER_SCORE_FILE):
		with open(PLAYER_SCORE_FILE, "r") as file:
			try:
				jsonObject: dict = json.load(file)
				if jsonObject.get('scores'):
					highScores = jsonObject['scores']
				else:
					# If scores isn't in the json, fix the file
					with open(PLAYER_SCORE_FILE, "w") as writeFile:
						json.dump({"scores": []}, writeFile, indent="\t")
			except json.JSONDecodeError:
				# If file is empty for some reason, fix the file
				with open(PLAYER_SCORE_FILE, "w") as writeFile:
					json.dump({"scores": []}, writeFile, indent="\t")
	else:
		# if file does not exist, create it and write empty scores
		with open(PLAYER_SCORE_FILE, "w") as writeFile:
			json.dump({"scores": []}, writeFile, indent="\t")

	pygame.display.set_caption("Space Invaders")
	pygame.display.set_icon(pygame.image.load("assets/icon.png"))

	alpha_surf = AlphaLayer(SCREEN)

	retro_font = font.Font("assets/font/prstart.ttf", 16)

	clock = pygame.time.Clock()
	player = Player(SCREEN_HALF_WIDTH, SCREEN_HEIGHT - 10)
	alpha_surf.bind(player, C_RED)

	enemies = []
	enemy_group = pygame.sprite.Group()

	enemies.append(Enemy(EnemyType.SMALL, SCREEN_HALF_WIDTH - 100, SCREEN_HALF_HEIGHT, enemy_group))
	enemies.append(Enemy(EnemyType.MEDIUM, SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT, enemy_group))
	enemies.append(Enemy(EnemyType.LARGE, SCREEN_HALF_WIDTH + 100, SCREEN_HALF_HEIGHT, enemy_group))
	
	alpha_surf.bind(enemy_group, C_GREEN)

	background = Background(SCREEN, player)

	while True:
		for event in pygame.event.get():
			if event.type == locals.QUIT:
				# Save the player's score
				with open(PLAYER_SCORE_FILE, "w") as file:
					highScores.append({
						"name": hex(id(player)),
						"score": player.score
					})

					json.dump({
						"scores": highScores
					}, file, indent="\t")
				return		

		dt = clock.tick(60) / 1000.0
		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE]: return
		player.move(keys)
		player.update(dt)
		
		background.update()

		alpha_surf.render_all_binded()
		alpha_surf.draw()

		player.draw(SCREEN)

		for enemy in enemies:
			enemy.update()
			enemy.draw(SCREEN)

		SCREEN.blit(retro_font.render(f"SCORE: {player.score}", True, C_WHITE), (10, 10))

		if pygame.time.get_ticks() % FPS == 0:
			player.addScore(1)

		SCREEN.blit(retro_font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255)), (10, 30))

		pygame.display.flip()

		pygame.display.update()

if __name__ == "__main__":
	main()
	pygame.quit()
	font.quit()
				
	
			
	quit()