import enum
import pygame

# shared
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # screen size
SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 # screen center
C_BLACK,         C_WHITE,         C_RED,           C_GREEN,         C_BLUE,          C_YELLOW,        C_PURPLE,        C_CYAN = \
(000, 000, 000), (255, 255, 255), (255, 000, 000), (000, 255, 000), (000, 000, 255), (255, 255, 000), (255, 000, 255), (000, 255, 255)
# colors

# main.py
FPS = 60 # frames per second
K_UP, K_LEFT, K_DOWN, K_RIGHT = pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d # player controls
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # main output surface

# player.py
PLAYER_MAX_VELOCITY = 30 # the maximum velocity the player can reach
PLAYER_SPEEDUP = 20 # the rate at which the player's velocity increases
PLAYER_SLOWDOWN = 40 # the rate at which the player's velocity decreases
PLAYER_SCORE_FILE = "score.json" # the file to save the player's score

# background.py
STAR_MAX_DEPTH = 20 # the maximum depth (3D) of a star
STAR_COUNT = 400 # ~the number of stars in the background at any given time
STAR_SPEED = 0.5 # the speed at which the stars move
STAR_SIZE = 2 # the maximum size of a star (also the number of possible sizes)
STAR_COLOURS = [(255, 255, 255, 255), (170, 170, 0, 150), (255, 255, 255, 170), (150, 225, 225, 255)]

# enemy.py
ENEMIES = [pygame.image.load(f'assets/sprites/enemy{i}.png').convert_alpha() for i in [1, 2, 3]]
ENEMY_WIDTH, ENEMY_HEIGHT = 16, 8
ENEMY_SCALE = 5
ENEMY_FPS = 2
ENEMY_FRAMECOUNT = 2
ENEMY_COLOURKEY = (0, 255, 0)
ENEMY_SPEED = 1
ENEMY_COUNT = 1