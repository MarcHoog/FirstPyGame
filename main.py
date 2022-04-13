import pygame
from sys import exit

# Youtube video, Great turtorial if you never did anything with pygame
# It's pretty easy
# https://www.youtube.com/watch?v=AY9MnQ4x3zk 

# initiate pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner Clone')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Background variables
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/Ground.png').convert()
text_surf = font.render('hoi',False,'Black').convert()

# snail variables
snail_default_pos = 800
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (snail_default_pos,300))

# player variables
player_default_pas = 80
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (player_default_pas,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # blit = block image transfer
    # They render in that order so you can overlap 
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    screen.blit(text_surf,(300,50))
    
   
    # snail movement code
    snail_rect.left += -4
    if snail_rect.right <= 0:
        snail_rect.left = snail_default_pos    
        
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)
    
    if player_rect.colliderect(snail_rect):
        print('collision!')
  
    pygame.display.update()
    clock.tick(60)
    
    