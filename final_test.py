import pygame, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Group Collide!")

FPS = 60
clock = pygame.time.Clock()

class Game():
    def __init__(self, monster_group, knight_group):
        self.monster_group = monster_group
        self.knight_group = knight_group

    def update(self):
        self.check_collisions()

    def check_collisions(self):
        pygame.sprite.groupcollide(self.monster_group, self.knight_group, False , True)

class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1,5)

    def update(self):
        self.rect.y -= self.velocity

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

my_knight_group = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i*64, WINDOW_HEIGHT - 64)
    my_knight_group.add(knight)

my_game = Game(monster_group, my_knight_group)

game_running = True
while game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_running = False

    display_surface.fill((0,0,0))

    monster_group.update()
    monster_group.draw(display_surface)

    my_knight_group.update()
    my_knight_group.draw(display_surface)

    my_game.update()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit

