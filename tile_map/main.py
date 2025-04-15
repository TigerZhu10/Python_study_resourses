import pygame

pygame.init()

WINDOW_WIDTH = 320
WINDOW_HEIGHT = 160
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game")

grass = pygame.image.load("./tile_map/grass.png")
dirt = pygame.image.load("./tile_map/dirt.png")
water = pygame.image.load("./tile_map/water.png")
tile_size = 32

tilemap = [
    [4,4,4,4,4,4,4,4,4,4],
    [4,4,4,4,4,4,4,4,4,4],
    [1,1,4,1,1,1,4,4,1,1],
    [0,0,2,0,0,0,2,2,0,0],
    [0,0,2,0,0,0,2,2,0,0],
]


def draw_tilemap():
    for y, row in enumerate(tilemap):
        for x, tile in enumerate(row):
            if tile == 0:
                screen.blit(dirt, (x * tile_size, y * tile_size))
            elif tile == 1:
                screen.blit(grass, (x * tile_size, y * tile_size))
            elif tile == 2:
                screen.blit(water, (x * tile_size, y * tile_size))



game_running = True
while game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_running = False

    draw_tilemap()

    pygame.display.update()
pygame.quit

