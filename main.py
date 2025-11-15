import pygame
import sys
#setting
pygame.init()
screen = pygame.display.set_mode((865,768))
pygame.display.set_caption("My first pygame")
clock = pygame.time.Clock()
test_font=pygame.font.Font("pixeltype.ttf",50)
sky_surface=pygame.image.load("Bg.png").convert_alpha()

score_surface=test_font.render("Welcome to My Pygame",False,("white"))
score_rect=score_surface.get_rect(center=(865/2,100))

plane_surface=pygame.image.load("Plane.png").convert_alpha()
plane_rect=plane_surface.get_rect(midleft=(50,200))

obstacle_surface=pygame.image.load("Fly1.png").convert_alpha()
obstacle_rect= obstacle_surface.get_rect(midright=(865,200))

#moving


while True:
    clock.tick(60)
    pygame.display.update()
    
    #exit game
    for event in pygame.event.get():
        # if event.type ==pygame.MOUSEMOTION:
        #    print(event.pos)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type== pygame.KEYDOWN and pygame.K_SPACE:
        #     print("jump")
        # if event.type== pygame.KEYUP:
        #     print("keyup")
    
    
    #draw sky,plane and text 
    screen.blit(sky_surface,(0,0))
    #pygame.draw.line(screen,'red',(0,0),pygame.mouse.get_pos(),10)
    screen.blit(score_surface,score_rect)
    screen.blit(plane_surface,plane_rect)
    #moving obstacle
    screen.blit(obstacle_surface ,obstacle_rect)
    obstacle_rect.x-=5
    if obstacle_rect.x < -100 :
        obstacle_rect.x=865
    #if plane_rect.colliderect(obstacle_rect):
    #    print("COLLIDE")





    #key
    #keys=pygame.key.get_pressed()    
    #if keys[pygame.K_SPACE]:
        
