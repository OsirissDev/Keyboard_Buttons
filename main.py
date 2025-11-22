import pygame

pygame.init()
clock = pygame.time.Clock()
class button(pygame.sprite.Sprite):
    def __init__(self, key, width, height, coordinates):
        super().__init__()
        self.key = key
        self.coordinates = coordinates
        self.rect= pygame.Rect(self.coordinates[0], self.coordinates[1], width, height)
        self.box_filled = False
        self.text_color = "white"


    def pressed(self, bool):
        self.box_filled = bool
        if bool:
            self.text_color = 'dark grey'
        else: self.text_color = 'white'


    def draw(self, screen):
        if self.box_filled: pygame.draw.rect(screen, "white", self.rect)
        else: pygame.draw.rect(screen, "white", self.rect,2 )
        if self.key in tiny_keys:
            key_text = tiny_font.render(self.key, False, self.text_color)
        else:
            key_text = font.render(self.key, False, self.text_color)
        key_text_rect = key_text.get_rect(center = self.rect.center)
        screen.blit(key_text, key_text_rect)

    def yell(self):
        print("YELLOW")

scale=150
font = pygame.font.SysFont("Sans-serif", 1*scale//2)
tiny_font = pygame.font.SysFont("Sans-serif", 1*scale//4)

screen = pygame.display.set_mode((11*scale, 6*scale))
pygame.display.set_icon(pygame.image.load('Pygame_Icon.png').convert())

button_list=pygame.sprite.Group()




spacing = 1/8 #easily adjustable button settings
button_size = .5

offsets={ #adds value to the x coordinate to move individual rows a specific amount to account for special keys
    0 : (0),
    1 : (1 - 1/8),
    2 : (1 + 1/8),
    3 : (1.5),
    4 : (0),
    5 : 0,
    6 : 0,
    7 : 0
}

special_keys={ # text, dimensions(width, height), column, row, offset
    0 : [
        "tab",
         ((2 - 4/8) * (scale * button_size), (button_size * scale)),
         (0,1),
        0
    ],

    1 : [
        "del",
        ((1 + 4/8) * (scale * button_size), (button_size * scale)),
        (13,0),
        0
    ],
    2 : [
        "caps",
        ((2) * (scale * button_size), (button_size * scale)) ,
         (0,2),
        0
    ],
     3 : [
         "L shift",
        ((2 + 7/9) * (scale * button_size), (button_size * scale)),
         (0,3),
         0
     ],
    4 : [
        "R shift",
     ((2 + 3/8) * (scale * button_size), (button_size * scale)),
        (10,3),
        1.5,
    ],
    5 : [
        "enter",
        ((2) * (scale * button_size), (button_size * scale)),
         (11,2),
         1 + 1/8,
    ],
    6 : [ #the bottom row sucks so its better to just do it through manually defining sizes and coords
        "fn",
        ((.99) * (scale * button_size), (button_size * scale)),
         (0,4),
         0,
    ],
    7 : [
        "ctrl",
        ((.99) * (scale * button_size), (button_size * scale)),
         (1,4),
         0,
    ],
    8 : [
        "Lalt",
        ((.99) * (scale * button_size), (button_size * scale)),
         (2,4),
         0,
    ],
     9 : [
        "Lcmd",
        ((1) * (scale * button_size), (button_size * scale)),
         (3,4),
         0,
    ],
    10 : [
        " ",
        ((6.5) * (scale * button_size), (button_size * scale)),
         (4,4),
         0,
    ],
    11 : [
        "Rcmd",
        ((1.25) * (scale * button_size), (button_size * scale)),
         (5,4),
         2.75,
    ],
    12 : [
        "Ralt",
        ((.99) * (scale * button_size), (button_size * scale)),
         (6,4),
         2.9,
    ],
    13 : [
        "up",
        ((1) * (scale * button_size), ((.5)* button_size * scale)),
        (8,4),
         2.9,
    ],
    14 : [
        "down",
        ((1) * (scale * button_size), ((.5)* button_size * scale)),
        (8,4.4),
         2.9,
    ],
    15 : [
        "left",
        ((1) * (scale * button_size), ((.5)* button_size * scale)),
        (7.19,4.4),
         2.9,
    ],
    16 : [
        "right",
        ((1) * (scale * button_size), ((.5)* button_size * scale)),
        (8.81,4.4),
         2.9,
    ],
}

#keys that need to use the tiny font
tiny_keys=["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","Lalt","Ralt","Lcmd","Rcmd","ctrl","up","down","left","right"]

for i in special_keys.keys():
    col, row = special_keys[i][2]  # column and row of the special key

    # X calculation based on column
    x_coord_base = ((((col / 2) + 1) + special_keys[i][3]) * scale)
    x_coordinate = x_coord_base + col * spacing * scale + spacing * scale

    # Y calculation based on row
    y_coord_base = (((row / 2) + 1) * scale)
    y_coordinate = y_coord_base + row * spacing * scale + spacing * scale

    # Use the actual width and height from the special_keys definition
    width, height = special_keys[i][1]

    button_list.add(button(special_keys[i][0], width, height, (x_coordinate, y_coordinate)))

#keys that are different on pygame than on the keyboard
alt_key_names={
    "left ctrl" : "ctrl",
    "left alt" : "Lalt",
    "left meta" : "Lcmd",
    "space" : " ",
    "right meta" : "Rcmd",
    "right alt" : "Ralt",
    "return" : "enter",
    "right shift" : "R shift",
    "left shift" : "L shift",
    "caps lock" : "caps",
    "backspace" : "del",
}

characters= ["`1234567890-=" , "qwertyuiop[]\\", "asdfghjkl;'" , "zxcvbnm,./","","","", "made by osiris"]
# creating button classes
for y in range(len(characters)):
    for i in range(len(characters[y])):


        x_coord_base= (((i/2)+1) * scale) + offsets[y] * scale #variables for readability while finding the x coord
        x_coordinate = (x_coord_base + i *( spacing * scale)) + spacing*scale

        y_coord_base = (((y / 2) + 1) * scale)  # variables for readability while finding the x coord
        y_coordinate = (y_coord_base + y * (spacing * scale)) + spacing * scale

        button_list.add(button(characters[y][i], button_size * scale, button_size * scale, (x_coordinate, y_coordinate)))

#Half keys
# creating button classes
for i in range(12):

        x_coord_base= (((i/2)+1) * scale) * scale #variables for readability while finding the x coord
        x_coordinate = (x_coord_base + i *( spacing * scale)) + spacing*scale

        y_coord_base = (((y / 2) + 1) * scale)  # variables for readability while finding the x coord
        y_coordinate = spacing * scale

        button_list.add(button(f"f{i}", button_size * scale, button_size * scale, (x_coordinate, y_coordinate)))

# Test: call yell() on first button in the group


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), exit()

        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) in alt_key_names.keys(): target = alt_key_names[pygame.key.name(event.key)]
            else: target = pygame.key.name(event.key)
            for button in button_list:
                if button.key == target:
                    button.pressed(True)
        if event.type == pygame.KEYUP:
            if pygame.key.name(event.key) in alt_key_names.keys(): target = alt_key_names[pygame.key.name(event.key)]
            else: target = pygame.key.name(event.key)
            for button in button_list:
                if button.key == target:
                    button.pressed(False)



    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, 'white', pygame.Rect(1*scale, 1*scale, 9.3*scale, 4*scale), 4)

    fps_text = font.render(f"fps: {round(clock.get_fps())}", False, "white")
    fps_text_rect = fps_text.get_rect(topleft=(0,0))
    screen.blit(fps_text, fps_text_rect)

    for b in button_list:
        b.draw(screen)
    pygame.display.update()

    clock.tick(30)
    # print(clock.get_fps())