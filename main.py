import pygame
import sys
from random import randint


#initializing setting
def obstacle_movement(obstacle_list):
    global obstacle_rect_list
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=5
            if obstacle_rect.bottom ==300: screen.blit(snail_surface,obstacle_rect)
            else: screen.blit(fly_surface,obstacle_rect)

        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x> -50]
        return obstacle_list
    
    else:return[] 

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
    fly_index+=0.1
    if fly_index >= len(fly_flying):fly_index=0
    fly_surface=fly_flying[int(fly_index)]
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):return False
    return True
def score_get():
    global score
    global score_surface, start_time
    # score is time survived in seconds
    score = (pygame.time.get_ticks() - start_time) // 1000 
    score_surface = score_font.render(f"Your score is   {score}", False,("black"))
    return score

pygame.init()
game_active=True
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Pixel Runner")
clock = pygame.time.Clock()

score =0
#text=on the display
score_font=pygame.font.Font("font/Pixeltype.ttf",50)
end_text=pygame.font.Font("font/Pixeltype.ttf",50)
end_surface=end_text.render(f"DEAD !   Press  'SPACE'  to  try  again !",False,("black"))

score_surface=score_font.render(f"Your score is   {score}",False,("black"))
sky_surface=pygame.image.load('graphics/Sky.png')


#player
player_walk1=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk2=pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walking=[player_walk1,player_walk2]
player_index =0
player_jumping=pygame.image.load('graphics/player/jump.png').convert_alpha()
#sounds
jump_sound=pygame.mixer.Sound('audio/jump.mp3')
jump_sound.set_volume(0.5)
bgsound=pygame.mixer.Sound('audio/music.wav')
bgsound.set_volume(0.3)
bgsound.play(loops= -1)

# start time for score (milliseconds)
start_time = pygame.time.get_ticks()

player_surf=player_walking[player_index]
player_rect= player_surf.get_rect(bottomleft=(20,300))
player_gravity=0

ground_surface=pygame.image.load('graphics/ground.png').convert_alpha()
ground_rect=ground_surface.get_rect(topleft=(0,300))

#bugs
snail_1=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_2=pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_walking=[snail_1,snail_2]
snail_index=0
snail_surface=snail_walking[snail_index]
snail_rect=snail_surface.get_rect(bottomright=(800,300))

fly_1=pygame.image.load("graphics/fly/fly1.png").convert_alpha()
fly_2=pygame.image.load("graphics/fly/fly2.png").convert_alpha()
fly_index=0
fly_flying=[fly_1,fly_2]
fly_surface=fly_flying[fly_index]
fly_rect=fly_surface.get_rect(bottomright=(800,300))

# obstacle_rect_list=[fly_rect,snail_rect]
obstacle_rect_list = []
#timer
obstacle_clock=pygame.USEREVENT +1
pygame.time.set_timer(obstacle_clock,1400)


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
                    jump_sound.play()
        else:
            if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active=True
                snail_rect.x=800
                # reset scoring and timers
                start_time = pygame.time.get_ticks()
                score = 0
                obstacle_rect_list.clear()
                player_rect.bottom = 300
        if event.type == obstacle_clock and game_active==True:
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900,1100),300)))
                
            else:
                obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900,1100),200)))
    score_get()
    if game_active:
    #blit

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,ground_rect)
        
        #animation
        fly_animation()
        snail_animation()
        screen.blit(score_surface,(260,20))
        
        
        #obstile spwaning
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #player
        player_gravity+=0.85
        player_rect.y +=player_gravity
        if player_rect.bottom >= 300:player_rect.bottom =300
        player_animation()
        screen.blit(player_surf,player_rect)

        #collision
        game_active=collisions(player_rect,obstacle_rect_list)
        
    else:
        screen.fill('red')
        screen.blit(end_surface,(150,170))
        obstacle_rect_list.clear()
        player_rect.y = 300
        if event.type == pygame.KEYDOWN :
            if event.key ==pygame.K_SPACE:
                game_active=True
                start_time = pygame.time.get_ticks()
                score = 0
                obstacle_rect_list.clear()
                player_rect.bottom = 300
                

    #Updating 
    pygame.display.update()
    clock.tick(60)
    