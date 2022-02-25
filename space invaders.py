from numpy import average, sign
import pygame
import random
import colorsys
pygame.init()

WIDTH, HEIGHT = 800, 600
HALFWIDTH, HALFHEIGHT = WIDTH // 2, HEIGHT // 2

FPS   = 60
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
UP, LEFT, DOWN, RIGHT, ESCAPE = pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_ESCAPE

MAX_VELOCITY = 30
SPEEDUP = 20
SLOWDOWN = 30
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

MAXDEPTH = 20
STARCOUNT = 150
STARSPEED = 0.5
class Background:
	def __init__(self, screen):
		self.stars = []
		self.screen = screen

		for i in range(STARCOUNT):
			self.stars.append({
				'x': random.randint(-HALFWIDTH, HALFWIDTH), 
				'y': random.randint(0, HEIGHT), 
				'depth': random.randint(1, MAXDEPTH)
			})

	def update(self, playerpos):
		playerpos -= HALFWIDTH
		for star in self.stars:
			size = 2 if star['depth'] < MAXDEPTH // 2 else 3
			x = (star['x'] + playerpos * (star['depth'] / MAXDEPTH) * 0.1) + HALFWIDTH
			y = star['y']
			star['y'] += (star['depth'] / MAXDEPTH) * STARSPEED
			if star['y'] > HEIGHT:
				star['y'] = random.randint(-HALFHEIGHT, 0)
				star['x'] = random.randint(-HALFWIDTH, HALFWIDTH)
				star['depth'] = random.randint(1, MAXDEPTH)
			pygame.draw.rect(self.screen, WHITE, (x, y, size, size))

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
		dt = clock.tick(FPS) / 1000.0
		keys = pygame.key.get_pressed()
		screen.fill(BLACK)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT: return
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
	pygame.quit()
	quit()