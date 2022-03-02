# Remove pygame "Hello from the pygame community." message
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "something"

from enemies import Enemies
from constants import *
import pygame
import json
import pygame.locals as locals
import pygame.font as font
import colorsys
from background import Background
from player import Player
from enemy import Enemy, EnemyType
from typing import Dict, List

pygame.init()
font.init()

def hsv2rgb(h, s=1.0, v=1):
	return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

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

	# surface for adding alpha visual effect, still needs work
	alphaSurf = pygame.Surface(SCREEN.get_size(), pygame.SRCALPHA)

	retroFont = font.Font("assets/font/prstart.ttf", 16)

	clock = pygame.time.Clock()
	allSprites = pygame.sprite.Group()
	player = Player(SCREEN_HALF_WIDTH, SCREEN_HEIGHT - 10, allSprites)

	enemies = Enemies()

	enemies.add(Enemy(EnemyType.SMALL, SCREEN_HALF_WIDTH - 100, SCREEN_HALF_HEIGHT))
	enemies.add(Enemy(EnemyType.MEDIUM, SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT))
	enemies.add(Enemy(EnemyType.LARGE, SCREEN_HALF_WIDTH + 100, SCREEN_HALF_HEIGHT))

	background = Background(SCREEN, player)

	h = 0

	while True:
		for event in pygame.event.get():
			if event.type == locals.QUIT:
				pygame.quit()
				font.quit()
				
				# Save the player's score
				with open(PLAYER_SCORE_FILE, "w") as file:
					highScores.append({
						"name": hex(id(player)),
						"score": player.score
					})

					json.dump({
						"scores": highScores
					}, file, indent="\t")
				
				quit()

		dt = clock.tick(FPS) / 1000.0
		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE]: return
		player.move(keys)
		player.update(dt)
		
		alphaSurf.fill((*hsv2rgb(h / 64), 220), special_flags=pygame.BLEND_RGBA_MULT)
		h += 1
		h %= 64
		
		background.update()

		allSprites.draw(alphaSurf)

		SCREEN.blit(alphaSurf, (0, 0))

		enemies.update()
		enemies.draw(SCREEN)

		SCREEN.blit(retroFont.render(f"SCORE: {player.score}", True, C_WHITE), (10, 10))

		if pygame.time.get_ticks() % FPS == 0:
			player.addScore(1)

		SCREEN.blit(retroFont.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255)), (10, 30))

		pygame.display.flip()

		pygame.display.update()

if __name__ == "__main__":
	main()