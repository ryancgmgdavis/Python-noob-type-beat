import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 576  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "SOOPAH BARIO GORLD: Waluigi's Taco Truck Adventure"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 400
GRAVITY = 300
PLAYER_WIDTH = TILESIZE // 1.2
PLAYER_HEIGHT = TILESIZE * 1.4

BGIMG = pg.transform.scale(pg.image.load("images/background.png"), (WIDTH, HEIGHT))
BLOCK = pg.transform.scale(pg.image.load("images/block.png"), (TILESIZE, TILESIZE))
PLAYER = pg.transform.scale(pg.image.load("images/player.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))

