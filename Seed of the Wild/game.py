from ast import keyword
import pygame, sys

  
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 512
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Seed of the Wild')

player_surf = pygame.image.load('./Assets/Player/player_idle.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (500, 443))

player_gravity_y = 0
player_velocity = 3


# looking_left = False # Vamos usar isso pra direcionar o dash

oilbee_x_4_pos = 250
oilbee_y_4_pos = 100
oilbee_surf_4 = pygame.image.load('./Assets/oilbee/oilbee_1.png').convert_alpha()
oilbee_rect_4 = oilbee_surf_4.get_rect(midbottom = (oilbee_x_4_pos, oilbee_y_4_pos))
oilbee_surf_2 = pygame.image.load('./Assets/oilbee/oilbee_2.png').convert_alpha()
oilbee_rect_2 = oilbee_surf_2.get_rect(midbottom = (500, 90))
oilbee_surf_3 = pygame.image.load('./Assets/oilbee/oilbee_2.png').convert_alpha()
oilbee_rect_3 = oilbee_surf_3.get_rect(midbottom = (100, 440))

oilbee_collider = (oilbee_rect_4, oilbee_rect_2, oilbee_rect_3)

florest_surf = pygame.image.load('./Assets/Scenery/florest_1.png').convert()
florest_surf = pygame.transform.rotozoom(florest_surf, 0, 2)

ground_surf = pygame.image.load('./Assets/Scenery/ground_2.png').convert_alpha()
ground_surf = pygame.transform.rotozoom(ground_surf, 0, 2)
ground_rect = ground_surf.get_rect(midbottom = (500, 550))

game_font = pygame.font.Font('./Font/Pixeltype.ttf', 60)

text_1_surf = game_font.render('Seed of the Wild', True, (0,0,0))
text_1_rect = text_1_surf.get_rect(midbottom = (500, 100))

menu_surf = pygame.image.load('./Assets/menu_esc/menu_screen.png').convert_alpha()
menu_rect = menu_surf.get_rect(midbottom = (500, 256))

clock = pygame.time.Clock()

game_active = False

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        key = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 430:
                player_gravity_y= -20 #Tem que fazer no gravity(y) / velocity (x) porque esses vão adicionar exponencialmente, sendo o velocity limitado.
            
            #if key[pygame.K_q] and looking_left == False:
                #player_rect.x += 50  # Faz direto no Rect pra pular tudo

           # elif[pygame.K_q] and looking_left == True:
               # player_rect.x -= 50

            #else:
                #ooking_left = False
                #dash_velocity = 0

        if key[pygame.K_d]:
                looking_left = False
                player_velocity += 3
            
        elif key[pygame.K_a]:
            looking_left = True
            player_velocity -= 3

        else:
            player_velocity = 0

        if player_velocity >= 3:
            player_velocity = 3
        
        if player_velocity <= -3:
            player_velocity = -3

    screen.blit(florest_surf, (0,0))

    screen.blit(ground_surf, (ground_rect))
    
    screen.blit(player_surf, (player_rect))

    screen.blit(oilbee_surf_4, (oilbee_rect_4))
    screen.blit(oilbee_surf_2, (oilbee_rect_2))
    screen.blit(oilbee_surf_3, (oilbee_rect_3))

    screen.blit(text_1_surf, text_1_rect)

    player_rect.x += player_velocity
    
    player_gravity_y += 1
    player_rect.y += player_gravity_y

    if player_rect.bottom >= 430:
        player_rect.bottom = 430
    
    oilbee_rect_4.x += 4
    oilbee_rect_4.y += 4
    
    oilbee_rect_2.x -= 6
    oilbee_rect_2.y += 6

    oilbee_rect_3.x += 5


    if oilbee_y_4_pos < 100:
        oilbee_x_4_pos = 700

    if oilbee_rect_3.colliderect(player_rect):
        pygame.quit()
        sys.exit()

    clock.tick(60)

    pygame.display.update()