import pygame, sys
from button import Button
#import game

pygame.init()

SCREEN = pygame.display.set_mode((1000, 512))
pygame.display.set_caption("Seed of the Wild: Menu")

BG = pygame.image.load("Assets/screens/tela.png").convert_alpha()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Assets/screens/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(20).render("Aqui vai ficar o jogo.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(500, 256))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
       

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/screens/Play Rect.png"), pos=(520, 300), 
                            text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("Assets/screens/Quit Rect.png"), pos=(510,450), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")


        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()