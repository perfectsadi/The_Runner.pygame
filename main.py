import pygame
import sys
import random

#initisializing setting
def player_animation():
    global player_surf ,player_index
    if player_rect.bottom<300:
        player_surf=player_jumping
    
    else:
        player_index += 0.1
        if player_index >= len(player_walking):player_index =0
        player_surf=player_walking[int(player_index)]

def snail_animation():
    global snail_surface ,snail_index
    snail_index+=0.1
    if snail_index >= len(snail_walking):snail_index=0
    snail_surface=snail_walking[int(snail_index)]
def fly_animation():
    global fly_index,fly_surface
    if snail_index >= len(snail_walking):fly_index=0





pygame.init()
game_active=True
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption="The Runner.pygame"
clock = pygame.time.Clock()

score =0
#text=on the display
score_font=pygame.font.Font("font/pixeltype.ttf",50)
end_text=pygame.font.Font("font/pixeltype.ttf",50)
end_surface=end_text.render(f"DEAD !   Press  'SPACE'  to  try  again !",False,("black"))

score_surface=score_font.render(f"Your score is   {score}",False,("black"))
sky_surface=pygame.image.load('graphics/Sky.png')


#player
player_walk1=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk2=pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walking=[player_walk1,player_walk2]
player_index =0
player_jumping=pygame.image.load('graphics/player/jump.png').convert_alpha()
player_surf=player_walking[player_index]
player_rect= player_surf.get_rect(bottomleft=(20,300))
player_gravity=0

ground_surface=pygame.image.load('graphics/ground.png')
ground_rect=ground_surface.get_rect(topleft=(0,300))

#bugs
snail_1=pygame.image.load('graphics/snail/snail1.png')
snail_2=pygame.image.load('graphics/snail/snail2.png')
snail_walking=[snail_1,snail_2]
snail_index=0
snail_surface=snail_walking[snail_index]
snail_rect=snail_surface.get_rect(bottomright=(800,300))

fly_1=pygame.image.load("graphics/Fly/fly1.png")
fly_2=pygame.image.load("graphics/Fly/fly2.png")
fly_index=0
fly_flying=[fly_1,fly_2]
fly_surface=fly_flying[fly_index]
fly_rect=fly_surface.get_rect(bottomright=(800,300))

obsatcle_list=[fly_rect,snail_rect]
#timer
obsatcle_clock=pygame.USEREVENT + 1
pygame.time.set_timer(obsatcle_clock,950)


while True:
    #exiting
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type ==pygame.MOUSEBUTTONDOWN :
                if player_rect.collidepoint(event.pos):
                    player_gravity=-20

            if event.type == pygame.KEYDOWN  and player_rect.bottom ==300:
                if event.key == pygame.K_SPACE :
                    player_gravity=-20
        else:
            if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active=True
                snail_rect.x=800
        if event.type == obsatcle_clock and game_active==True:
            obsatcle_list.append(snail_rect(bottomright=(randint(900,1100),300)))
    if game_active:
    #blit
    
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,ground_rect)
        screen.blit(snail_surface,snail_rect)
        screen.blit(score_surface,(260,20))
        screen.blit(fly_surface,fly_rect)
        
        #obstile

        
    
        

        #player
        player_gravity+=1
        player_rect.y +=player_gravity
        if player_rect.bottom >= 300:player_rect.bottom =300
        player_animation()
        screen.blit(player_surf,player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active=False
            
    else:
        screen.fill('red')
        screen.blit(end_surface,(150,170))
        if event.type == pygame.KEYDOWN :
            if event.key ==pygame.K_SPACE:
                game_active=True

    #Updating 
    pygame.display.update()
    clock.tick(60)
    