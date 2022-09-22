from ast import keyword
import pygame, sys
import menu


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 512
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Seed of the Wild')

player_surf = pygame.image.load('./Assets/Player/player_idle.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (500, 443))
player_gravity = 0

florest_surf = pygame.image.load('./Assets/Scenery/florest_1.png').convert()
florest_surf = pygame.transform.rotozoom(florest_surf, 0, 2)

ground_surf = pygame.image.load('./Assets/Scenery/ground_2.png').convert_alpha()
ground_surf = pygame.transform.rotozoom(ground_surf, 0, 2)
ground_rect = ground_surf.get_rect(midbottom = (500, 550))

game_font = pygame.font.Font('./Font/Pixeltype.ttf', 60)

text_1_surf = game_font.render('Seed of the Wild', True, (0,0,0))
text_1_rect = text_1_surf.get_rect(midbottom = (500, 100))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 430:
                player_gravity = -20

            if event.key == pygame.K_d:
                player_x = +1

    screen.blit(florest_surf, (0,0))
    screen.blit(ground_surf, (ground_rect))
    screen.blit(player_surf, (player_rect))

    screen.blit(text_1_surf, text_1_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 430:
        player_rect.bottom = 430
        
    clock.tick(60)

    pygame.display.update()