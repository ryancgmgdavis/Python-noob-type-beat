import pygame
from settings import *
        
startbutton = True
running = True


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.SysFont("comicsansms", F_SIZE)
        self.font_small = pygame.font.SysFont("comicsansms", 14)
        self.clock = pygame.time.Clock()


    def display(self):
        self.background = pygame.image.load("images/background.png")
        self.screen.blit(self.background, (0, 0))
        self.opponent = pygame.image.load("images/danny.png")
        self.screen.blit(self.opponent, (350, 21))
        self.player = pygame.image.load("images/GunkBama.png")
        self.screen.blit(self.player, (100, 112))

    def show_text(self, message1, message2):
        text1 = self.font.render(message2, True, F_COLOR)
        self.screen.blit(text1, (T_SPACE, T1_HEIGHT))
        text2 = self.font.render(message1, True, F_COLOR)
        self.screen.blit(text2, (T_SPACE, T2_HEIGHT))

    def button(self, x, y , width, height, hover, color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, hover, (x, y, width, height))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.screen, color, (x, y, width, height))

    def start_menu(self):
        global startbutton
        while startbutton:
            start_button = self.button(WIDTH - 130, 7, 125, 26, LIGHTGRAY, GRAY)
            start_text = self.font_small.render("Start the Game!", True, WHITE)
            self.screen.blit(start_text, (WIDTH - 120, 9))
            if start_button:
                self.display()
                self.show_text("Trash Man attacks!", "What will Gunk MissBama do?")
                startbutton = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            pygame.display.update()
            self.clock.tick(15)
            return True

    def events(self):
        pass

    
g = Game()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    g.start_menu()
    pygame.display.update()
    g.clock.tick(15)
    

