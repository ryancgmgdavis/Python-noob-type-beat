'''

'''

import pygame 
from bashersTac import *

pygame.init()

class Game():
    loaded = False
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", FONT_SIZE)
        self.score = 0
        self.scoreboard = self.font.render(f"Score: {self.score}", True, WHITE)
    
    def display(self):
        self.screen.blit(self.scoreboard, (10, 0))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.score += 1
                Game().display()

while True:
    Game().display()
    
    