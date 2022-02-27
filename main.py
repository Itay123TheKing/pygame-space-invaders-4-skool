# Remove pygame "Hello from the pygame community." message
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "something"

from constants import *
import pygame
import pygame.locals as locals
import colorsys
from typing import Tuple
from background import Background
from player import Player
from enemy import Enemy

pygame.init()

def hsv2rgb(h: float, s: float = 1.0, v: float = 1.0) -> Tuple[int, int, int]:
	return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def main() -> None:
	pygame.display.set_caption("Space Invaders")
	pygame.display.set_icon(pygame.image.load("assets/icon.png"))
	alphaSurf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
	# surface for adding alpha visual effect, still needs work
  
	clock = pygame.time.Clock()
	allSprites = pygame.sprite.Group()
	player = Player(SCREEN_HALF_WIDTH, SCREEN_HEIGHT - 10, allSprites)
	background = Background(SCREEN, player)
	enemy = Enemy(1, 0, 0)

	h = 0

	while True:
		for event in pygame.event.get():
			if event.type == locals.QUIT:
				pygame.quit()
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

		enemy.update()
		enemy.draw(SCREEN)

		pygame.display.update()

if __name__ == "__main__":
	main()