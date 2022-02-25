from numpy import average, sign
import pygame
import random
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
	def __init__(self, x, y):
		super().__init__()
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
	def __init__(self):
		self.stars = []

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
			pygame.draw.rect(screen, WHITE, (x, y, size, size))

def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	alphaSurf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
	clock = pygame.time.Clock()
	player = Player(HALFWIDTH, HEIGHT)
	background = Background()

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

		screen.blit(player.image, player.rect)

		background.update(player.rect.centerx)

		pygame.display.update()

if __name__ == '__main__':
	main()
	pygame.quit()
	quit()

class Player(pg.sprite.Sprite):

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        pg.draw.circle(self.image, pg.Color('dodgerblue'), (25, 25), 25)
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos


def main():
    alpha_surf = pg.Surface(screen.get_size(), pg.SRCALPHA)
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    player = Player((150, 150), all_sprites)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    player.vel.x = 5
                elif event.key == pg.K_a:
                    player.vel.x = -5
                elif event.key == pg.K_w:
                    player.vel.y = -5
                elif event.key == pg.K_s:
                    player.vel.y = 5
            elif event.type == pg.KEYUP:
                if event.key == pg.K_d and player.vel.x > 0:
                    player.vel.x = 0
                elif event.key == pg.K_a and player.vel.x < 0:
                    player.vel.x = 0
                elif event.key == pg.K_w:
                    player.vel.y = 0
                elif event.key == pg.K_s:
                    player.vel.y = 0

        # Reduce the alpha of all pixels on this surface each frame.
        # Control the fade speed with the alpha value.
        alpha_surf.fill((255, 255, 255, 220), special_flags=pg.BLEND_RGBA_MULT)

        all_sprites.update()
        screen.fill((20, 50, 80))  # Clear the screen.
        all_sprites.draw(alpha_surf)  # Draw the objects onto the alpha_surf.
        screen.blit(alpha_surf, (0, 0))  # Blit the alpha_surf onto the screen.
        pg.display.flip()
        clock.tick(60)
