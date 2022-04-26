import pygame     
        

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("TITLE")

font = pygame.font.SysFont(None, 32)

def show_text(message):
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, (10, 370))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    show_text("hoss")
    pygame.display.update()
    

