
import pygame

#colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (25, 25, 25)
LIGHTGRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

#screen stuff
TITLE = "Soopah Bario Gorld"
#1280 or 1024 for best results
WIDTH = 1024
HEIGHT = WIDTH // 1.777
TILESIZE = WIDTH // 32
TILEWIDTH = TILESIZE
TILEHEIGHT = TILESIZE
P_HEIGHT = TILESIZE * 1.8
P_WIDTH = P_HEIGHT // 1.3
P_SPEED = TILESIZE // 6
FPS = 40

#images
BGIMG = pygame.transform.scale(pygame.image.load("images/background.png"), (WIDTH, HEIGHT))
BLOCK = pygame.transform.scale(pygame.image.load("images/block.png"), (TILESIZE, TILESIZE))
