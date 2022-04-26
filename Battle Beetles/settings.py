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
HEIGHT = 640  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Battle Beetles"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#player settings
PLAYER_SPEED = 400
PLAYER_IMG = "F1.png"
#WALK_RIGHT = [pg.image.load("img/R1.jpg"), pg.image.load("R2.jpg"), pg.image.load("R3.jpg")]
#WALK_LEFT = [pg.image.load("L1.jpg"), pg.image.load("L2.jpg"), pg.image.load("L3.jpg")]
#WALK_FORWARD = [pg.image.load("F1.jpg"), pg.image.load("F2.jpg"), pg.image.load("F3.jpg")]
#WALK_BACK = [pg.image.load("B1.jpg"), pg.image.load("B2.jpg"), pg.image.load("B3.jpg")]