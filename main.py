import pygame
pygame.init()

class button(pygame.sprite.Sprite):
    def __init__(self, button, coordinates):
        super().__init__()
        self.button = button
        self.coordinates = coordinates



screen = pygame.display.set_mode((13*50, 6*50), pygame.SCALED, vsync=1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), exit()

        if event.type == pygame.KEYDOWN:
            pass

    pygame.draw.rect(screen, 'white', pygame.Rect(1*50, 1*50, 11*50, 4*50))

    pygame.display.update()