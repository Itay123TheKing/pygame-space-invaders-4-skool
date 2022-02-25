# Remove pygame "Hello from the pygame community." message
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "something"

from constants import *
import pygame
import pygame.locals as locals
import colorsys
from player import Player
from background import Background

pygame.init()

def hsv2rgb(h, s=1.0, v=1):
	return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	alphaSurf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
	clock = pygame.time.Clock()
	allSprites = pygame.sprite.Group()
	player = Player(HALFWIDTH, HEIGHT - 10, allSprites)
	background = Background(screen)

	h = 0

	while True:
		for event in pygame.event.get():
			if event.type == locals.QUIT:
				pygame.quit()
				quit()

		dt = clock.tick(FPS) / 1000.0
		keys = pygame.key.get_pressed()
		screen.fill(BLACK)
		
		if keys[ESCAPE]: return
		if keys[LEFT]:
			player.update(LEFT, dt)
		elif keys[RIGHT]:
			player.update(RIGHT, dt)
		else:
			player.update(None, dt)

		alphaSurf.fill((*hsv2rgb(h / 64), 220), special_flags=pygame.BLEND_RGBA_MULT)
		h += 1
		h %= 64

		background.update(player.rect.centerx)

		allSprites.draw(alphaSurf)

		screen.blit(alphaSurf, (0, 0))

		pygame.display.update()

if __name__ == '__main__':
	main()