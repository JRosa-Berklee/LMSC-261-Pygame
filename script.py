import pygame

from pygame.locals import *

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define variables
tile_size = 25
#load images
bg_img = pygame.image.load('img/background-2.jpeg')

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

class Player():
    def __init__(self, x, y):
         img = pygame.image.load('img/guy-1.jpeg')
         self.image = pygame.transform.scale(img, (20, 40))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.velocity = 50

    def update(self, dt):
         dx = 0
         dy = 0
         #get inputs
         key = pygame.key.get_pressed()
         if key[pygame.K_LEFT]:
              dx -= self.velocity * dt
         if key[pygame.K_RIGHT]:
              dx += self.velocity * dt
        
         #check for collision here

         #update player coordinates
         self.rect.x += dx
         self.rect.y += dy
         
         #draw player onto screen
         screen.blit(self.image, self.rect)
         
         

class World():
      def __init__(self, data):
        self.tile_list = []  
        #load images
        dirt_img = pygame.image.load('img/dirt-block.png')
        grass_img = pygame.image.load('img/grass-block.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                 if tile == 1:
                      img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                      img_rect = img.get_rect()
                      img_rect.x = col_count * tile_size
                      img_rect.y = row_count * tile_size
                      tile = (img, img_rect)
                      self.tile_list.append(tile)
                 if tile == 2:
                      img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                      img_rect = img.get_rect()
                      img_rect.x = col_count * tile_size
                      img_rect.y = row_count * tile_size
                      tile = (img, img_rect)
                      self.tile_list.append(tile)
                 col_count += 1
            row_count += 1
      def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])    

world_data =[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
player = Player(50, screen_height - 65)
world = World(world_data)

clock = pygame.time.Clock()
run = True 
while run:
    dt = clock.tick(60) / 1000.0

    
    screen.blit(bg_img,bg_img.get_rect())
    world.draw()
    player.__init__
    player.update(dt)
    print(world.tile_list)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        pygame.display.update()
pygame.quit()


