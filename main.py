import pygame

pygame.init()
clock = pygame.time.Clock()
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
        pygame.draw.rect(screen, self.color, self.rect, 2)
        key_text = font.render(self.key, False, "white")
        key_text_rect = key_text.get_rect(center = self.rect.center)
        screen.blit(key_text, key_text_rect)


scale=150
font = pygame.font.SysFont("Sans-serif", 1*scale//2)

screen = pygame.display.set_mode((13*scale, 6*scale), pygame.SCALED, vsync=1)

button_list=pygame.sprite.Group()

characters= ["~1234567890-=" , "qwertyuiop[]\\", "asdfghjkl;'" , "zxcvbnm,./"]

# creating button classes
for y in range(len(characters)):
    for i in range(len(characters[y])):
        x_coord_base= (((i/2)+1) * scale) #variables for readability while finding the x coord
        x_coordinate = (x_coord_base + i *( .25 * scale)) + .25*scale

        y_coord_base = (((y / 2) + 1) * scale)  # variables for readability while finding the x coord
        y_coordinate = (y_coord_base + y * (.25 * scale)) + .25 * scale

        button_list.add(button(characters[y][i], (.5 * scale, .5 * scale), (x_coordinate, y_coordinate)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), exit()

        if event.type == pygame.KEYDOWN:
            print(event.key)

    pygame.draw.rect(screen, 'white', pygame.Rect(1*scale, 1*scale, 11*scale, 4*scale), 4)

    for b in button_list:
        b.draw(screen)
    pygame.display.update()

    clock.tick(30)
    # print(clock.get_fps())
