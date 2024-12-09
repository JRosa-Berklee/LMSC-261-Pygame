import pygame

from pygame.locals import *

pygame.init()

screen_width = 1600
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define variables
tile_size = 50
#load images
bg_img = pygame.image.load('background-2.jpeg')

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

screen.fill((0,0,0))
run = True 
while run:


    screen.blit(bg_img,bg_img.get_rect())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        pygame.display.update()
pygame.quit()


