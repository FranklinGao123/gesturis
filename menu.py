import pygame
import sys
import settings 
from utils import renderTitle, drawButtonWithText

# This method will return a menu action
def displayMenu(curr_state):
    # Menu specific setup
    menu_running = True
    is_settings_active = False
    sound_fx_volume = settings.SOUND_FX_VOLUME
    music_volume = settings.MUSIC_VOLUME
    colour_blind_mode = settings.COLOUR_BLIND_MODE

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

    while menu_running:
        # Event loop
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check for hover on icons
        instr_scale = HOVER_SCALE if not is_settings_active and instr_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE
        settings_scale = HOVER_SCALE if not is_settings_active and settings_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE
        sound_scale = HOVER_SCALE if not is_settings_active and sound_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE

        hover_scaled_instr_icon = pygame.transform.scale(scaled_instructions_icon, (int(ICON_DIM * instr_scale), int(ICON_DIM * instr_scale)))
        hover_scaled_settings_icon = pygame.transform.scale(scaled_settings_icon, (int(ICON_DIM * settings_scale), int(ICON_DIM * settings_scale)))
        hover_scaled_sound_icon = pygame.transform.scale(scaled_sound_icon, (int(ICON_DIM * sound_scale), int(ICON_DIM * sound_scale)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle settings modal displayal
            if is_settings_active:
                cancel_button, save_button, toggle_button = displaySettings(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check for setting events
                    if cancel_button.collidepoint(mouse_x, mouse_y):
                        is_settings_active = False
                    elif save_button.collidepoint(mouse_x, mouse_y):
                        saveSettings(sound_fx_volume, music_volume, colour_blind_mode)
                        is_settings_active = False
                    elif toggle_button.collidepoint(mouse_x, mouse_y):
                        colour_blind_mode = not colour_blind_mode
                        # update visuals for toggle
                        print("toggled colour blind mode")

                    # TODO: Volume settings
            else:
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
                    if settings_button.collidepoint(mouse_x, mouse_y):
                        is_settings_active = True

                    if quit_button.collidepoint(mouse_x, mouse_y):
                        pygame.quit()
                        sys.exit()

        # Fill screen with menu background color
        settings.display_surface.fill(settings.MENU_BG_COLOR)

        if not is_settings_active:
            displayBaseMenu(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon)

        # Render the settings modal if active
        if is_settings_active:
            displaySettings(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon)
        
        # Update the display
        pygame.display.update()
        
    return curr_state


def displayBaseMenu(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, 
                   hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon):
    
    # Fonts
    title_font = pygame.font.Font(settings.FONT_PATH, 150)
    button_font = pygame.font.Font(settings.FONT_PATH, 23)

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

    # Text
    single_player_text = button_font.render("1 PLAYER", True, settings.BUTTON_TEXT_COLOR)
    multi_player_text = button_font.render("2 PLAYERS", True, settings.BUTTON_TEXT_COLOR)
    quit_text = button_font.render("Quit", True, settings.BUTTON_TEXT_COLOR)

    renderTitle(title_font, "GESTURIS", settings.GAME_PIXEL_SIZE * 10, SINGLE_BUTTON_Y - 3*BUTTON_HEIGHT)
    settings.display_surface.blit(scaled_peace_icon, (settings.GAME_PIXEL_SIZE * 36.5, SINGLE_BUTTON_Y - 3*BUTTON_HEIGHT + settings.GAME_PIXEL_SIZE))

    # Draw buttons with hover effect
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if not is_settings_active and single_player_button.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, single_player_button, 0, settings.BUTTON_CORNER_RADIUS)
    else:
        pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, single_player_button)
    pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, single_player_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

    if not is_settings_active and multi_player_button.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, multi_player_button, 0, settings.BUTTON_CORNER_RADIUS)
    else:
        pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, multi_player_button)
    pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, multi_player_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

    # Draw button text
    settings.display_surface.blit(single_player_text, (BUTTON_X + (settings.GAME_PIXEL_SIZE * 2.8), SINGLE_BUTTON_Y + (settings.GAME_PIXEL_SIZE * .7)))
    settings.display_surface.blit(multi_player_text, (BUTTON_X + (settings.GAME_PIXEL_SIZE * 2.35), MULTI_BUTTON_Y + (settings.GAME_PIXEL_SIZE * .7)))
    # settings.display_surface.blit(quit_text, (quit_button.x + 70, quit_button.y + 10))

    # Draw icons
    settings.display_surface.blit(hover_scaled_instr_icon, (INSTR_X, ICON_Y))
    settings.display_surface.blit(hover_scaled_settings_icon, (SETTINGS_X, ICON_Y))
    settings.display_surface.blit(hover_scaled_sound_icon, (SOUND_X, ICON_Y))


def displaySettings(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, 
                   hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon):
    color_blind_mode = False

    # Render the base background menu first
    displayBaseMenu(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon)
    
    # Semi-transparent background
    overlay = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    overlay.set_alpha(128)  # Set opacity (0 is fully transparent, 255 is fully opaque)
    overlay.fill((0, 0, 0))  # Black background
    settings.display_surface.blit(overlay, (0, 0))

    # Modal box
    modal_width, modal_height = 400, 300
    modal_x = (settings.WINDOW_WIDTH - modal_width) // 2
    modal_y = (settings.WINDOW_HEIGHT - modal_height) // 2
    modal_rect = pygame.Rect(modal_x, modal_y, modal_width, modal_height)
    pygame.draw.rect(settings.display_surface, (255, 255, 255), modal_rect, 0, border_radius=15)

    # Title
    title_font = pygame.font.Font(settings.FONT_PATH, 40)
    title_text = title_font.render("SETTINGS", True, (0, 0, 0))
    title_x = modal_rect.centerx - title_text.get_width() // 2
    title_y = modal_rect.y + 20
    settings.display_surface.blit(title_text, (title_x, title_y))

    # Sound FX Slider
    slider_font = pygame.font.Font(settings.FONT_PATH, 20)
    sound_text = slider_font.render("SOUND FX:", True, (0, 0, 0))
    settings.display_surface.blit(sound_text, (modal_x + 30, modal_y + 80))

    # Music Slider
    music_text = slider_font.render("MUSIC:", True, (0, 0, 0))
    settings.display_surface.blit(music_text, (modal_x + 30, modal_y + 140))

    # Color-Blind Mode
    cb_text = slider_font.render("COLOUR-BLIND MODE:", True, (0, 0, 0))
    settings.display_surface.blit(cb_text, (modal_x + 30, modal_y + 200))
    
    # Toggle Button
    toggle_button_rect = pygame.Rect(modal_x + 300, modal_y + 200, 50, 25)
    pygame.draw.rect(settings.display_surface, (0, 128, 0) if color_blind_mode else (128, 128, 128), toggle_button_rect)

    # Cancel and Save Buttons
    cancel_button = pygame.Rect(modal_x + 50, modal_y + 250, 100, 40)
    save_button = pygame.Rect(modal_x + 250, modal_y + 250, 100, 40)

    pygame.draw.rect(settings.display_surface, (200, 200, 200), cancel_button, border_radius=10)
    pygame.draw.rect(settings.display_surface, (200, 200, 200), save_button, border_radius=10)

    cancel_text = slider_font.render("CANCEL", True, (0, 0, 0))
    save_text = slider_font.render("SAVE", True, (0, 0, 0))

    settings.display_surface.blit(cancel_text, (cancel_button.centerx - cancel_text.get_width() // 2, cancel_button.centery - cancel_text.get_height() // 2))
    settings.display_surface.blit(save_text, (save_button.centerx - save_text.get_width() // 2, save_button.centery - save_text.get_height() // 2))

    return cancel_button, save_button, toggle_button_rect


def saveSettings(sound_fx_volume, music_volume, colour_blind_mode):
    settings.SOUND_FX_VOLUME = sound_fx_volume
    settings.MUSIC_VOLUME = music_volume
    settings.COLOUR_BLIND_MODE = colour_blind_mode