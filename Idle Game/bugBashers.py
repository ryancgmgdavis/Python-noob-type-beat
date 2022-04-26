'''

'''

import random
import pygame 
from bashersTac import *

pygame.init()

class Game():
    loaded = False
    def __init__(self, points):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.monsters = [ALIEN, CAT, CROC, DEMON, DOG, FLAME, MAGMA, SANDMAN, STONE, WIZARD, MONKEY, ZOMBIE1, MINOTAUR, PIG, SPIDER, WEREWOLF, ZOMBIE2, ZOMBIE3, SPHINX, TREE, OGRE, LIZARD]
        self.monster = random.choice(self.monsters)
        self.font = pygame.font.SysFont("comicsansms", FONT_SIZE)
        self.score = 0 + self.tempScore
        self.scoreboard = self.font.render(f"Score: {self.score}", True, BLACK)

    def load(self):
        self.enemy = self.monster
        self.enemyRect = self.enemy.get_rect()
        self.screen.blit(BGIMG, (0, 0))
        self.screen.blit(self.enemy, (200, 100))
        self.screen.blit(self.scoreboard, (10, 0))
        
    def newEnemy(self):
        self.enemy = random.choice(self.monsters) 
    
    def display(self):
        #for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #x, y = event.pos
                #if self.enemy.get_rect().collidepoint(x, y):
        self.enemy = self.monster
        self.enemyRect = self.enemy.get_rect()
        self.screen.blit(BGIMG, (0, 0))
        self.screen.blit(self.enemy, (200, 100))
        self.screen.blit(self.scoreboard, (10, 0))

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS) / 1000
            if self.loaded == False:
                self.load()
                self.loaded = True
            self.events()
            pygame.display.update()


    def events(self):
        for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if self.enemyRect.collidepoint(x, y):
                    self.score += 1
                    Game().display()

while True:
    Game().run()