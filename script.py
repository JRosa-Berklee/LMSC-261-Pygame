import pygame

from pygame.locals import *

pygame.init()

screen_width = 612
screen_height = 382

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#load images
bg_img = pygame.image.load('img/background.jpeg')

screen.fill((0,0,0))
run = True 
while run:


    screen.blit(bg_img,bg_img.get_rect())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()


