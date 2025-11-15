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


ground_surface=pygame.image.load('graphics/ground.png')
ground_rect=ground_surface.get_rect(topleft=(0,300))












while True:
    #exiting
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
        if event.type == pygame.K_SPACE :
            player_rect.y-=10
    #blit
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,ground_rect)
    screen.blit(player_surface,player_rect)

    while player_rect.y >300:player_rect.y+=1


    #Updating 
    pygame.display.update()
    clock.tick(60)