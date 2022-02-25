from numpy import sign
import pygame as pg
import random
pg.init()

WIDTH, HEIGHT = 800, 600
HALFWIDTH, HALFHEIGHT = WIDTH // 2, HEIGHT // 2

FPS   = 60
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
UP, LEFT, DOWN, RIGHT, ESCAPE = pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_ESCAPE

MAX_VELOCITY = 30
SPEEDUP = 20
SLOWDOWN = 30
class Player(pg.sprite.Sprite):
	def __init__(self, x, y, screen):
		super().__init__()
		self.image = pg.Surface((32, 32))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
		self.rect.bottom = y
		self.rect.centerx = x
		self.velocity = 0
		self.screen = screen
		

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
	def __init__(self):
		self.stars = []

		for i in range(STARCOUNT):
			self.stars.append({
				'x': random.randint(-HALFWIDTH, HALFWIDTH), 
				'y': random.randint(0, HEIGHT), 
				'depth': random.randint(1, MAXDEPTH)
			})

	def update(self, playerpos, screen):
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
			pg.draw.rect(screen, WHITE, (x, y, size, size))

def main():
	screen = pg.display.set_mode((WIDTH, HEIGHT))
	alphaSurf = pg.Surface(screen.get_size(), pg.SRCALPHA)
	clock = pg.time.Clock()
	player = Player(HALFWIDTH, HEIGHT, screen)
	background = Background()

	while True:
		dt = clock.tick(FPS) / 1000.0
		keys = pg.key.get_pressed()
		screen.fill(BLACK)
		
		for event in pg.event.get():
			if event.type == pg.QUIT: return
		if keys[ESCAPE]: return
		if keys[LEFT]:
			player.update(LEFT, dt)
		elif keys[RIGHT]:
			player.update(RIGHT, dt)
		else:
			player.update(None, dt)

		screen.blit(player.image, player.rect)

		background.update(player.rect.centerx)

		pg.display.update()

if __name__ == '__main__':
	main()
	pg.quit()
	quit()