import pygame
import sys
import settings 

# This method will return a menu action
def displayMenu(curr_state):
    # Menu specific setup
    menu_running = True

    # Define menu colors
    MENU_BG_COLOR = (0, 0, 0)
    BUTTON_COLOR = (0, 0, 0)
    BUTTON_HOVER_COLOR = (69, 69, 69)
    BUTTON_TEXT_COLOR = (255, 255, 255)
    BUTTON_OUTLINE_WIDTH = 5
    BUTTON_CORNER_RADIUS = 30

    # Create font for buttons
    font = pygame.font.SysFont("monaco", 18)

    # Text
    single_player_text = font.render("1 PLAYER", True, BUTTON_TEXT_COLOR)
    multi_player_text = font.render("2 PLAYERS", True, BUTTON_TEXT_COLOR)
    quit_text = font.render("Quit", True, BUTTON_TEXT_COLOR)

    # Buttons
    single_player_button = pygame.Rect(560, 390, 315, 88)
    multi_player_button = pygame.Rect(560, 504, 315, 88)
    quit_button = pygame.Rect(300, 600, 200, 50)

    # instructions button
    # settings button
    # volume button

    while menu_running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if single_player_button.collidepoint(mouse_x, mouse_y):
                    curr_state = settings.GameState.SINGLEPLAYER
                    menu_running = False

                if multi_player_button.collidepoint(mouse_x, mouse_y):
                    curr_state = settings.GameState.MULTIPLAYER
                    menu_running = False
                
                # TODO: If settings button is clicked, load settings overlay

                if quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        # Fill screen with menu background color
        settings.display_surface.fill(MENU_BG_COLOR)

        # Draw buttons with hover effect
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if single_player_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(settings.display_surface, BUTTON_HOVER_COLOR, single_player_button, BUTTON_OUTLINE_WIDTH, BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, BUTTON_COLOR, single_player_button, BUTTON_OUTLINE_WIDTH, BUTTON_CORNER_RADIUS)

        if multi_player_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(settings.display_surface, BUTTON_HOVER_COLOR, multi_player_button, BUTTON_OUTLINE_WIDTH, BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, BUTTON_COLOR, multi_player_button, BUTTON_OUTLINE_WIDTH, BUTTON_CORNER_RADIUS)

        # if quit_button.collidepoint(mouse_x, mouse_y):
        #     pygame.draw.rect(settings.display_surface, BUTTON_HOVER_COLOR, quit_button)
        # else:
        #     pygame.draw.rect(settings.display_surface, BUTTON_COLOR, quit_button)

        # Draw button text
        settings.display_surface.blit(single_player_text, (single_player_button.x + (settings.GAME_PIXEL_SIZE * 3), single_player_button.y + (settings.GAME_PIXEL_SIZE * 2)))
        settings.display_surface.blit(multi_player_text, (multi_player_button.x + (settings.GAME_PIXEL_SIZE * 3), multi_player_button.y + (settings.GAME_PIXEL_SIZE * 2)))
        # settings.display_surface.blit(quit_text, (quit_button.x + 70, quit_button.y + 10))

        # Update the display
        pygame.display.update()
        
    return curr_state


# TODO: deal with settings in here? It's an overlay so it's not a new page

def displaySettings(curr_state):
    pass