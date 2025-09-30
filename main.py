import pygame

pygame.init()
clock = pygame.time.Clock()
class button(pygame.sprite.Sprite):
    def __init__(self, key, width, height, coordinates):
        super().__init__()
        self.key = key
        self.coordinates = coordinates
        self.rect= pygame.Rect(self.coordinates[0], self.coordinates[1], width, height)
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

screen = pygame.display.set_mode((13*scale, 6*scale))

button_list=pygame.sprite.Group()

characters= ["~1234567890-=" , "qwertyuiop[]\\", "asdfghjkl;'" , "zxcvbnm,./","", "made by osiris"]


spacing = 1/8 #easily adjustable button settings
button_size = .5

offsets={ #adds value to the x coordinate to move individual rows a specific amount to account for special keys
    0 : (0),
    1 : (1 - 1/8),
    2 : (1 + 1/8),
    3 : (1.5),
    4 : (0),
    5 : 0
}

special_keys={ # text, dimensions(width, height), position
    0 : [
        "tab",
         ((2 - 4/8) * (scale * button_size), (button_size * scale)),
         ((1 + spacing) * scale, ((1.5 * scale) + 1 * (spacing * scale)) + spacing * scale)
    ],

    1 : [
        "del", ((1 + 4/8) * (scale * button_size), (button_size * scale)), ((((((13/2)+1) * scale) + 0) + 13 * (spacing * scale)) + spacing * scale,
        ((1 * scale) + 0 * (spacing * scale)) + spacing * scale)
    ],
    2 : [
        "caps",
         ((2 + 1/8) * (scale * button_size), (button_size * scale)),
        ((1 + spacing) * scale, ((2 * scale) + 2 * (spacing * scale)) + spacing * scale)
    ]
    # 3 :
    # 4 :
    # 5 :
    # 6 :
    # 7 :
    # 8 :
    # 9 :
}


# creating button classes
for y in range(len(characters)):
    for i in range(len(characters[y])):


        x_coord_base= (((i/2)+1) * scale) + offsets[y] * scale #variables for readability while finding the x coord
        x_coordinate = (x_coord_base + i *( spacing * scale)) + spacing*scale

        y_coord_base = (((y / 2) + 1) * scale)  # variables for readability while finding the x coord
        y_coordinate = (y_coord_base + y * (spacing * scale)) + spacing * scale

        button_list.add(button(characters[y][i], button_size * scale, button_size * scale, (x_coordinate, y_coordinate)))

for key in special_keys:
    button_list.add(button(special_keys[key][0], special_keys[key][1][0], special_keys[key][1][1], special_keys[key][2]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), exit()

        if event.type == pygame.KEYDOWN:
            print(event.key)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, 'white', pygame.Rect(1*scale, 1*scale, 11*scale, 4*scale), 4)

    fps_text = font.render(f"fps: {round(clock.get_fps())}", False, "white")
    fps_text_rect = fps_text.get_rect(topleft=(0,0))
    screen.blit(fps_text, fps_text_rect)

    for b in button_list:
        b.draw(screen)
    pygame.display.update()

    clock.tick(30)
    # print(clock.get_fps())
