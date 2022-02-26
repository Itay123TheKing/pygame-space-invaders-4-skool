import enum
import pygame

# main.py, background.py, player.py, enemy.py
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # screen size
SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 # screen center

# main.py
FPS = 60 # frames per second
K_UP, K_LEFT, K_DOWN, K_RIGHT = pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d # player controls
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # main output surface

# player.py
PLAYER_MAX_VELOCITY = 30 # the maximum velocity the player can reach
PLAYER_SPEEDUP = 20 # the rate at which the player's velocity increases
PLAYER_SLOWDOWN = 40 # the rate at which the player's velocity decreases

# background.py
C_BLACK, C_WHITE = (0, 0, 0), (255, 255, 255) # colors
STAR_MAX_DEPTH = 20 # the maximum depth (3D) of a star
STARCOUNT = 150 # ~the number of stars in the background at any given time
STAR_SPEED = 0.5 # the speed at which the stars move
STAR_SIZE = 2 # the maximum size of a star (also the number of possible sizes)

# enemy.py
VALID_ENEMIES = {1, 2, 3}
ENEMY_SPRITESHEET = pygame.image.load('Sprites\Enemies.png').convert_alpha()
ENEMY_WIDTH, ENEMY_HEIGHT = 16, 8
ENEMY_SCALE = 5
ENEMY_FPS = 2
ENEMY_FRAMECOUNT = 2
ENEMY_COLOURKEY = (0, 255, 0)