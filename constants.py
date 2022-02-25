import pygame

# main.py, background.py, player.py
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # screen size
SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 # screen center

# main.py
FPS = 60 # frames per second
K_UP, K_LEFT, K_DOWN, K_RIGHT = pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d # player controls

# background.py
C_BLACK, C_WHITE = (0, 0, 0), (255, 255, 255) # colors

# player.py
PLAYER_MAX_VELOCITY = 30 # the maximum velocity the player can reach
PLAYER_SPEEDUP = 20 # the rate at which the player's velocity increases
PLAYER_SLOWDOWN = 40 # the rate at which the player's velocity decreases

# background.py
STAR_MAX_DEPTH = 20
STARCOUNT = 150
STAR_SPEED = 0.5
STAR_SIZE = 2