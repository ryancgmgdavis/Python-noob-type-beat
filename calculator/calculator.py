import pygame
from settings import *

# rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
#pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60), 2, 3)

pygame.init()

class Calculator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.SysFont("comicsansms", F_SIZE)
        self.font_small = pygame.font.SysFont
        self.clock = pygame.time.Clock()

    def new_button(self, x, y , width, height, hover, color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, hover, (x, y, width, height), 50, 5)
            if click[0] == 1:
                return True

    def button(self, column, row, text):
        pygame.draw.rect(self.screen, GRAY, pygame.Rect(column, row, BUTTON, BUTTON), 50, 5)
        button = self.new_button(column, row, BUTTON, BUTTON, LIGHTGRAY, GRAY)
        text = self.font.render(text, True, BLACK)
        self.screen.blit(text, (column + 15, row))

    def menu(self):
        self.button(COL4, ROW1, "7")
        self.button(COL3, ROW1, "8")
        self.button(COL2, ROW1, "9")
        self.button(COL1, ROW1, "-")

        self.button(COL4, ROW2, "4")
        self.button(COL3, ROW2, "5")
        self.button(COL2, ROW2, "6")
        self.button(COL1, ROW2, "+")

        self.button(COL4, ROW3, "1")
        self.button(COL3, ROW3, "2")
        self.button(COL2, ROW3, "3")
        self.button(COL1, ROW3, "*")

        self.button(COL4, ROW4, "C")
        self.button(COL3, ROW4, "0")
        self.button(COL2, ROW4, "A")
        self.button(COL1, ROW4, "÷")
        
        
        

        


running = True
c = Calculator()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    c.screen.fill(WHITE)
    c.menu()
    pygame.display.flip()
    pygame.display.update()
    c.clock.tick(15)