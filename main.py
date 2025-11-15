import pygame
import sys

#initisializing setting
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption="The Runner.pygame"
clock = pygame.time.Clock()

score_font=pygame.font.Font("font/pixeltype.ttf",50)
score_surface=score_font.render("Welcome to My Pygame",False,("white"))
score_rect=score_surface.get_rect(center=(400,100))
sky_surface=pygame.image.load('graphics/Sky.png')
player_surface=pygame.image.load('graphics/player/player_walk_2.png')
player_rect= player_surface.get_rect(bottomleft=(20,300))
player_gravity=0

ground_surface=pygame.image.load('graphics/ground.png')
ground_rect=ground_surface.get_rect(topleft=(0,300))

#bugs
snail_surface=pygame.image.load('graphics/snail/snail1.png')
snail_rect=snail_surface.get_rect(bottomright=(800,300))
fly_surface=pygame.image.load("graphics/Fly/fly1.png")
fly_rect=fly_surface.get_rect(bottomright=(700,300))


while True:
    #exiting
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
        if event.type ==pygame.MOUSEBUTTONDOWN :
            if player_rect.collidepoint(event.pos):
                player_gravity=-20

        if event.type == pygame.KEYDOWN  and player_rect.bottom ==300:
            if event.key == pygame.K_SPACE :
                player_gravity=-20
            
    #blit
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,ground_rect)
    screen.blit(snail_surface,snail_rect)
    snail_rect.x -=2
    if snail_rect.x <-50:
        snail_rect.x =800

    #player
    player_gravity+=1
    player_rect.y +=player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom =300
    screen.blit(player_surface,player_rect)
    

    #Updating 
    pygame.display.update()
    clock.tick(60)