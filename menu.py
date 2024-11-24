import pygame
import sys
import settings 
from utils import renderTitle, drawButtonWithText

# This method will return a menu action
def displayMenu(curr_state):
    # Menu specific setup
    menu_running = True

    BUTTON_WIDTH = 236
    BUTTON_HEIGHT = 66

    ICON_DIM = BUTTON_HEIGHT * .75
    BUTTON_X = (settings.WINDOW_WIDTH - BUTTON_WIDTH) // 2
    SINGLE_BUTTON_Y = 290
    SPACE_BW_BUTTONS = (114 * .75)
    MULTI_BUTTON_Y = SINGLE_BUTTON_Y + SPACE_BW_BUTTONS
    ICON_Y = MULTI_BUTTON_Y + SPACE_BW_BUTTONS

    SETTINGS_X = (settings.WINDOW_WIDTH - ICON_DIM) // 2
    INSTR_X =  SETTINGS_X - SPACE_BW_BUTTONS
    SOUND_X = SETTINGS_X + SPACE_BW_BUTTONS

    NORMAL_SCALE = 1.00
    HOVER_SCALE = 1.1

    # Fonts
    title_font = pygame.font.Font(settings.FONT_PATH, 150)
    button_font = pygame.font.Font(settings.FONT_PATH, 23)

    # Text
    single_player_text = button_font.render("1 PLAYER", True, settings.BUTTON_TEXT_COLOR)
    multi_player_text = button_font.render("2 PLAYERS", True, settings.BUTTON_TEXT_COLOR)
    quit_text = button_font.render("Quit", True, settings.BUTTON_TEXT_COLOR)

    # Buttons
    single_player_button = pygame.Rect(BUTTON_X, SINGLE_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    multi_player_button = pygame.Rect(BUTTON_X, MULTI_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    quit_button = pygame.Rect(300, 600, 200, 50)

    # Load icons + setup rects for them
    peace_icon = pygame.image.load("images/peace_inverted.png")
    scaled_peace_icon = pygame.transform.scale(peace_icon, (3*ICON_DIM, 3*ICON_DIM))

    instructions_icon = pygame.image.load("images/question_inverted.png")
    scaled_instructions_icon = pygame.transform.scale(instructions_icon, (ICON_DIM, ICON_DIM))
    instr_button = pygame.Rect(INSTR_X, ICON_Y, ICON_DIM, ICON_DIM)

    settings_icon = pygame.image.load("images/settings_inverted.png")
    scaled_settings_icon = pygame.transform.scale(settings_icon, (ICON_DIM, ICON_DIM))
    settings_button = pygame.Rect(SETTINGS_X, ICON_Y, ICON_DIM, ICON_DIM)

    sound_icon = pygame.image.load("images/sound_inverted.png")
    scaled_sound_icon = pygame.transform.scale(sound_icon, (ICON_DIM, ICON_DIM))
    sound_button = pygame.Rect(SOUND_X, ICON_Y, ICON_DIM, ICON_DIM)

    # instructions button
    # settings button
    # volume button

    while menu_running:
        # Event loop
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check for hover on icons
        instr_scale = HOVER_SCALE if instr_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE
        settings_scale = HOVER_SCALE if settings_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE
        sound_scale = HOVER_SCALE if sound_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE

        hover_scaled_instr_icon = pygame.transform.scale(scaled_instructions_icon, (int(ICON_DIM * instr_scale), int(ICON_DIM * instr_scale)))
        hover_scaled_settings_icon = pygame.transform.scale(scaled_settings_icon, (int(ICON_DIM * settings_scale), int(ICON_DIM * settings_scale)))
        hover_scaled_sound_icon = pygame.transform.scale(scaled_sound_icon, (int(ICON_DIM * sound_scale), int(ICON_DIM * sound_scale)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # mouse_x, mouse_y = pygame.mouse.get_pos()

            # # Check for hover on icons
            # instr_scale = HOVER_SCALE if instr_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE
            # settings_scale = HOVER_SCALE if settings_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE
            # sound_scale = HOVER_SCALE if sound_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE

            # hover_scaled_instr_icon = pygame.transform.scale(scaled_instructions_icon, (int(ICON_DIM * instr_scale), int(ICON_DIM * instr_scale)))
            # hover_scaled_settings_icon = pygame.transform.scale(scaled_settings_icon, (int(ICON_DIM * settings_scale), int(ICON_DIM * settings_scale)))
            # hover_scaled_sound_icon = pygame.transform.scale(scaled_sound_icon, (int(ICON_DIM * sound_scale), int(ICON_DIM * sound_scale)))

            # Check for button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if single_player_button.collidepoint(mouse_x, mouse_y):
                    curr_state = settings.GameState.SINGLEPLAYER
                    menu_running = False

                if multi_player_button.collidepoint(mouse_x, mouse_y):
                    curr_state = settings.GameState.MULTIPLAYER
                    menu_running = False

                if instr_button.collidepoint(mouse_x, mouse_y):
                    curr_state = settings.GameState.INSTRUCTIONS_1
                    menu_running = False
                
                # TODO: If settings button is clicked, load settings overlay

                if quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        # Fill screen with menu background color
        settings.display_surface.fill(settings.MENU_BG_COLOR)
        renderTitle(title_font, "GESTURIS", settings.GAME_PIXEL_SIZE * 10, SINGLE_BUTTON_Y - 3*BUTTON_HEIGHT)
        settings.display_surface.blit(scaled_peace_icon, (settings.GAME_PIXEL_SIZE * 36.5, SINGLE_BUTTON_Y - 3*BUTTON_HEIGHT + settings.GAME_PIXEL_SIZE))

        # Draw buttons with hover effect
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if single_player_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, single_player_button, 0, settings.BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, single_player_button)
        pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, single_player_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

        if multi_player_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, multi_player_button, 0, settings.BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, multi_player_button)
        pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, multi_player_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

        # if quit_button.collidepoint(mouse_x, mouse_y):
        #     pygame.draw.rect(settings.display_surface, BUTTON_HOVER_COLOR, quit_button)
        # else:
        #     pygame.draw.rect(settings.display_surface, BUTTON_COLOR, quit_button)

        # Draw button text
        settings.display_surface.blit(single_player_text, (BUTTON_X + (settings.GAME_PIXEL_SIZE * 2.8), SINGLE_BUTTON_Y + (settings.GAME_PIXEL_SIZE * .7)))
        settings.display_surface.blit(multi_player_text, (BUTTON_X + (settings.GAME_PIXEL_SIZE * 2.35), MULTI_BUTTON_Y + (settings.GAME_PIXEL_SIZE * .7)))
        # settings.display_surface.blit(quit_text, (quit_button.x + 70, quit_button.y + 10))

        # Draw icons
        settings.display_surface.blit(hover_scaled_instr_icon, (INSTR_X, ICON_Y))
        settings.display_surface.blit(hover_scaled_settings_icon, (SETTINGS_X, ICON_Y))
        settings.display_surface.blit(hover_scaled_sound_icon, (SOUND_X, ICON_Y))

        # Update the display
        pygame.display.update()
        
    return curr_state


# TODO: deal with settings in here? It's an overlay so it's not a new page

def displaySettings(curr_state):
    pass