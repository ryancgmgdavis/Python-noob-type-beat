'''

'''
import random
import pygame 
from settings import *

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS) / 1000
            Particle().new()
            self.events()
            pygame.display.update()
            pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

class Particle:
    def new(self):
        self.x = random.randint(1, WIDTH)
        self.y = random.randint(1, HEIGHT)
        self.particle = pygame.draw.circle(Game().screen, BLUE, (self.x, self.y), 5, 5)

        

while True:
    Game().run()