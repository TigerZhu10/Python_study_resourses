import pygame, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Group Collide!")

FPS = 60
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, mg):
        super().__init__()
        self.image = pygame.image.load("Knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.velocity = 5

        self.mg = mg

    def update(self):
        self.move()
        self.check_collisions()

    def move(self):  
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def check_collisions(self):
        if pygame.sprite.spritecollide(self, self.mg, True):
            print(len(self.mg))

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.velocity = random.randint(1,10)

    def update(self):
        self.rect.y += self.velocity 

monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    monster_group.add(monster)

player_group = pygame.sprite.Group()
player = Player(500, 500, monster_group)
player_group.add(player) 

game_running = True
while game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_running = False

    display_surface.fill((0,0,0))

    player_group.update()
    player_group.draw(display_surface)

    monster_group.update()
    monster_group.draw(display_surface)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit