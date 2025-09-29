import pygame
pygame.init()

class button(pygame.sprite.Sprite):
    def __init__(self, key, dimensions, coordinates):
        super().__init__()
        self.key = key
        self.coordinates = coordinates
        self.rect= pygame.Rect(self.coordinates[0], self.coordinates[1], dimensions[0], dimensions[1])
        self.color = "white"

    def pressed(self, bool):
        if bool:
            self.color = 'white'
        else: self.color = 'black'

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        print("drawn")

scale=50

screen = pygame.display.set_mode((13*scale, 6*scale))

test=button("Q",(1*scale, 1*scale), (3*scale, 6*scale))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), exit()

        if event.type == pygame.KEYDOWN:
            print(event.key)

    pygame.draw.rect(screen, 'white', pygame.Rect(1*scale, 1*scale, 11*scale, 4*scale), 4)

    test.draw(screen)
    pygame.display.update()