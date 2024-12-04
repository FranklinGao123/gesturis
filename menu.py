import pygame
import sys
import settings 
from utils import renderTitle, drawButtonWithText

# This method will return a menu action
# def displayMenu(curr_state):
#     # Menu specific setup
#     menu_running = True
#     is_settings_active = False
#     sound_fx_volume = settings.SOUND_FX_VOLUME
#     music_volume = settings.MUSIC_VOLUME
#     colour_blind_mode = settings.COLOUR_BLIND_MODE

#     BUTTON_WIDTH = 236
#     BUTTON_HEIGHT = 66

#     ICON_DIM = BUTTON_HEIGHT * .75
#     BUTTON_X = (settings.WINDOW_WIDTH - BUTTON_WIDTH) // 2
#     SINGLE_BUTTON_Y = 290
#     SPACE_BW_BUTTONS = (114 * .75)
#     MULTI_BUTTON_Y = SINGLE_BUTTON_Y + SPACE_BW_BUTTONS
#     ICON_Y = MULTI_BUTTON_Y + SPACE_BW_BUTTONS

#     SETTINGS_X = (settings.WINDOW_WIDTH - ICON_DIM) // 2
#     INSTR_X =  SETTINGS_X - SPACE_BW_BUTTONS
#     SOUND_X = SETTINGS_X + SPACE_BW_BUTTONS

#     NORMAL_SCALE = 1.00
#     HOVER_SCALE = 1.1

#     # Buttons
#     single_player_button = pygame.Rect(BUTTON_X, SINGLE_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
#     multi_player_button = pygame.Rect(BUTTON_X, MULTI_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
#     quit_button = pygame.Rect(300, 600, 200, 50)

#     # Load icons + setup rects for them
#     peace_icon = pygame.image.load("images/peace_inverted.png")
#     scaled_peace_icon = pygame.transform.scale(peace_icon, (3*ICON_DIM, 3*ICON_DIM))

#     instructions_icon = pygame.image.load("images/question_inverted.png")
#     scaled_instructions_icon = pygame.transform.scale(instructions_icon, (ICON_DIM, ICON_DIM))
#     instr_button = pygame.Rect(INSTR_X, ICON_Y, ICON_DIM, ICON_DIM)

#     settings_icon = pygame.image.load("images/settings_inverted.png")
#     scaled_settings_icon = pygame.transform.scale(settings_icon, (ICON_DIM, ICON_DIM))
#     settings_button = pygame.Rect(SETTINGS_X, ICON_Y, ICON_DIM, ICON_DIM)

#     sound_icon = pygame.image.load("images/sound_inverted.png")
#     scaled_sound_icon = pygame.transform.scale(sound_icon, (ICON_DIM, ICON_DIM))
#     sound_button = pygame.Rect(SOUND_X, ICON_Y, ICON_DIM, ICON_DIM)

#     while menu_running:
#         # Event loop
#         mouse_x, mouse_y = pygame.mouse.get_pos()

#         # Check for hover on icons
#         instr_scale = HOVER_SCALE if not is_settings_active and instr_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE
#         settings_scale = HOVER_SCALE if not is_settings_active and settings_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE
#         sound_scale = HOVER_SCALE if not is_settings_active and sound_button.collidepoint(mouse_x, mouse_y) else NORMAL_SCALE

#         hover_scaled_instr_icon = pygame.transform.scale(scaled_instructions_icon, (int(ICON_DIM * instr_scale), int(ICON_DIM * instr_scale)))
#         hover_scaled_settings_icon = pygame.transform.scale(scaled_settings_icon, (int(ICON_DIM * settings_scale), int(ICON_DIM * settings_scale)))
#         hover_scaled_sound_icon = pygame.transform.scale(scaled_sound_icon, (int(ICON_DIM * sound_scale), int(ICON_DIM * sound_scale)))
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             # Handle settings modal displayal
#             if is_settings_active:

#                 mouse_pos = pygame.mouse.get_pos()
#                 mouse_down = pygame.mouse.get_pressed()[0]  # Left mouse button

#                 cancel_button, save_button, toggle_button, sound_fx_volume, music_volume, colour_blind_mode = displaySettings(
#                     is_settings_active,
#                     scaled_peace_icon,
#                     single_player_button,
#                     multi_player_button,
#                     hover_scaled_instr_icon,
#                     hover_scaled_settings_icon,
#                     hover_scaled_sound_icon,
#                     mouse_pos,
#                     mouse_down
#                 )

#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     # Check for setting events
#                     if cancel_button.collidepoint(mouse_x, mouse_y):
#                         is_settings_active = False
#                     elif save_button.collidepoint(mouse_x, mouse_y):
#                         saveSettings(sound_fx_volume, music_volume, colour_blind_mode)
#                         is_settings_active = False
#                     # elif toggle_button.collidepoint(mouse_x, mouse_y):
#                     #     colour_blind_mode = not colour_blind_mode
#                     #     # update visuals for toggle
#                     #     print("toggled colour blind mode")

#                     # TODO: Volume settings
#             else:
#                 # Check for button clicks
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if single_player_button.collidepoint(mouse_x, mouse_y):
#                         curr_state = settings.GameState.SINGLEPLAYER
#                         menu_running = False

#                     if multi_player_button.collidepoint(mouse_x, mouse_y):
#                         curr_state = settings.GameState.MULTIPLAYER
#                         menu_running = False

#                     if instr_button.collidepoint(mouse_x, mouse_y):
#                         curr_state = settings.GameState.INSTRUCTIONS_1
#                         menu_running = False
                    
#                     # TODO: If settings button is clicked, load settings overlay
#                     if settings_button.collidepoint(mouse_x, mouse_y):
#                         is_settings_active = True

#                     if quit_button.collidepoint(mouse_x, mouse_y):
#                         pygame.quit()
#                         sys.exit()

#         # Fill screen with menu background colour
#         settings.display_surface.fill(settings.MENU_BG_COLOUR)

#         if not is_settings_active:
#             displayBaseMenu(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon)

#         # Render the settings modal if active
#         if is_settings_active:
#             displaySettings(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon)
        
#         # Update the display
#         pygame.display.update()
        
#     return curr_state

def displayMenu(curr_state):
    # Menu specific setup
    menu_running = True
    is_settings_active = False

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
        mouse_down = pygame.mouse.get_pressed()[0]  # Check if left mouse button is pressed

        # Hover effects for icons
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

            # Handle settings modal interactions
            if is_settings_active:
                cancel_button, save_button, new_settings_state = displaySettings(
                    is_settings_active,
                    scaled_peace_icon,
                    single_player_button,
                    multi_player_button,
                    hover_scaled_instr_icon,
                    hover_scaled_settings_icon,
                    hover_scaled_sound_icon,
                    (mouse_x, mouse_y),
                    mouse_down
                )

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cancel_button.collidepoint(mouse_x, mouse_y):
                        is_settings_active = False  # Close modal without saving
                    elif save_button.collidepoint(mouse_x, mouse_y):
                        saveSettings(new_settings_state)  # Save the shared state
                        is_settings_active = False  # Close modal
            else:
                # Handle main menu interactions
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

                    if settings_button.collidepoint(mouse_x, mouse_y):
                        is_settings_active = True

                    if quit_button.collidepoint(mouse_x, mouse_y):
                        pygame.quit()
                        sys.exit()

        # Fill screen with background colour
        settings.display_surface.fill(settings.MENU_BG_COLOUR)

        # Render base menu or settings modal
        if not is_settings_active:
            displayBaseMenu(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon)
        else:
            displaySettings(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon, (mouse_x, mouse_y), mouse_down)

        # Update display
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
    single_player_text = button_font.render("1 PLAYER", True, settings.BUTTON_TEXT_COLOUR)
    multi_player_text = button_font.render("2 PLAYERS", True, settings.BUTTON_TEXT_COLOUR)
    quit_text = button_font.render("Quit", True, settings.BUTTON_TEXT_COLOUR)

    renderTitle(title_font, "GESTURIS", settings.GAME_PIXEL_SIZE * 10, SINGLE_BUTTON_Y - 3*BUTTON_HEIGHT)
    settings.display_surface.blit(scaled_peace_icon, (settings.GAME_PIXEL_SIZE * 36.5, SINGLE_BUTTON_Y - 3*BUTTON_HEIGHT + settings.GAME_PIXEL_SIZE))

    # Draw buttons with hover effect
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if not is_settings_active and single_player_button.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOUR, single_player_button, 0, settings.BUTTON_CORNER_RADIUS)
    else:
        pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOUR, single_player_button)
    pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOUR, single_player_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

    if not is_settings_active and multi_player_button.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOUR, multi_player_button, 0, settings.BUTTON_CORNER_RADIUS)
    else:
        pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOUR, multi_player_button)
    pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOUR, multi_player_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

    # Draw button text
    settings.display_surface.blit(single_player_text, (BUTTON_X + (settings.GAME_PIXEL_SIZE * 2.8), SINGLE_BUTTON_Y + (settings.GAME_PIXEL_SIZE * .7)))
    settings.display_surface.blit(multi_player_text, (BUTTON_X + (settings.GAME_PIXEL_SIZE * 2.35), MULTI_BUTTON_Y + (settings.GAME_PIXEL_SIZE * .7)))
    # settings.display_surface.blit(quit_text, (quit_button.x + 70, quit_button.y + 10))

    # Draw icons
    settings.display_surface.blit(hover_scaled_instr_icon, (INSTR_X, ICON_Y))
    settings.display_surface.blit(hover_scaled_settings_icon, (SETTINGS_X, ICON_Y))
    settings.display_surface.blit(hover_scaled_sound_icon, (SOUND_X, ICON_Y))


# def displaySettings(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, 
#                    hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon):
#     colour_blind_mode = False
#     sound_fx_volume = 0.5  # Range: 0.0 to 1.0
#     music_volume = 0.5

#     # Render base background menu
#     displayBaseMenu(is_settings_active, scaled_peace_icon, single_player_button, multi_player_button, hover_scaled_instr_icon, hover_scaled_settings_icon, hover_scaled_sound_icon)
    
#     # Semi-transparent background
#     overlay = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
#     overlay.set_alpha(128)
#     overlay.fill((0, 0, 0))
#     settings.display_surface.blit(overlay, (0, 0))

#     # Modal box
#     modal_width, modal_height = 400, 300
#     modal_x = (settings.WINDOW_WIDTH - modal_width) // 2
#     modal_y = (settings.WINDOW_HEIGHT - modal_height) // 2
#     modal_rect = pygame.Rect(modal_x, modal_y, modal_width, modal_height)
#     pygame.draw.rect(settings.display_surface, (255, 255, 255), modal_rect, 0, border_radius=15)

#     # Title
#     title_font = pygame.font.Font(settings.FONT_PATH, 40)
#     title_text = title_font.render("SETTINGS", True, (0, 0, 0))
#     settings.display_surface.blit(title_text, (modal_rect.centerx - title_text.get_width() // 2, modal_rect.y + 20))

#     # Sound FX Slider
#     slider_font = pygame.font.Font(settings.FONT_PATH, 20)
#     sound_text = slider_font.render("SOUND FX:", True, (0, 0, 0))
#     settings.display_surface.blit(sound_text, (modal_x + 30, modal_y + 80))

#     sound_slider_x = modal_x + 150
#     sound_slider_y = modal_y + 90
#     sound_slider_width = 200
#     sound_handle_radius = 8

#     sound_handle_pos = int(sound_slider_x + sound_fx_volume * sound_slider_width)
#     draw_slider(settings.display_surface, sound_slider_x, sound_slider_y, sound_slider_width, 20, sound_handle_pos, sound_handle_radius, (0, 0, 0), (200, 200, 200))

#     # Music Slider
#     music_text = slider_font.render("MUSIC:", True, (0, 0, 0))
#     settings.display_surface.blit(music_text, (modal_x + 30, modal_y + 140))

#     music_slider_x = modal_x + 150
#     music_slider_y = modal_y + 150

#     music_handle_pos = int(music_slider_x + music_volume * sound_slider_width)
#     draw_slider(settings.display_surface, music_slider_x, music_slider_y, sound_slider_width, 20, music_handle_pos, sound_handle_radius, (0, 0, 0), (200, 200, 200))

#     # Handle user interaction
#     mouse_down = pygame.mouse.get_pressed()[0]
#     mouse_pos = pygame.mouse.get_pos()

#     sound_handle_pos = handle_slider_drag(mouse_pos, mouse_down, sound_slider_x, sound_slider_y, sound_slider_width, sound_handle_pos, sound_handle_radius)
#     music_handle_pos = handle_slider_drag(mouse_pos, mouse_down, music_slider_x, music_slider_y, sound_slider_width, music_handle_pos, sound_handle_radius)

#     sound_fx_volume = (sound_handle_pos - sound_slider_x) / sound_slider_width
#     music_volume = (music_handle_pos - music_slider_x) / sound_slider_width

#     # Color-Blind Mode Toggle
#     cb_text = slider_font.render("COLOUR-BLIND MODE:", True, (0, 0, 0))
#     settings.display_surface.blit(cb_text, (modal_x + 30, modal_y + 200))
    
#     toggle_button = pygame.Rect(modal_x + 300, modal_y + 200, 50, 25)
#     pygame.draw.rect(settings.display_surface, (0, 128, 0) if colour_blind_mode else (128, 128, 128), toggle_button)

#     # Cancel and Save Buttons
#     cancel_button = pygame.Rect(modal_x + 50, modal_y + 250, 100, 40)
#     save_button = pygame.Rect(modal_x + 250, modal_y + 250, 100, 40)

#     pygame.draw.rect(settings.display_surface, (200, 200, 200), cancel_button, border_radius=10)
#     pygame.draw.rect(settings.display_surface, (200, 200, 200), save_button, border_radius=10)

#     cancel_text = slider_font.render("CANCEL", True, (0, 0, 0))
#     save_text = slider_font.render("SAVE", True, (0, 0, 0))

#     settings.display_surface.blit(cancel_text, (cancel_button.centerx - cancel_text.get_width() // 2, cancel_button.centery - cancel_text.get_height() // 2))
#     settings.display_surface.blit(save_text, (save_button.centerx - save_text.get_width() // 2, save_button.centery - save_text.get_height() // 2))

#     return cancel_button, save_button, toggle_button, sound_fx_volume, music_volume

def displaySettings(
    is_settings_active,
    scaled_peace_icon,
    single_player_button,
    multi_player_button,
    hover_scaled_instr_icon,
    hover_scaled_settings_icon,
    hover_scaled_sound_icon,
    mouse_pos,
    mouse_down
):
    # State variables
    sound_volume = settings.SETTINGS_STATE["sound_fx_volume"]
    music_volume = settings.SETTINGS_STATE["music_volume"]
    colour_blind_mode = settings.SETTINGS_STATE["colour_blind_mode"]

    new_settings_state = {
        "sound_fx_volume": settings.SETTINGS_STATE["sound_fx_volume"],
        "music_volume": settings.SETTINGS_STATE["music_volume"],
        "colour_blind_mode": settings.SETTINGS_STATE["colour_blind_mode"]
    }

    # Render base background menu
    displayBaseMenu(
        is_settings_active,
        scaled_peace_icon,
        single_player_button,
        multi_player_button,
        hover_scaled_instr_icon,
        hover_scaled_settings_icon,
        hover_scaled_sound_icon,
    )

    # Semi-transparent background
    overlay = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
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
    settings.display_surface.blit(title_text, (modal_rect.centerx - title_text.get_width() // 2, modal_rect.y + 20))

    # Slider configuration
    slider_font = pygame.font.Font(settings.FONT_PATH, 20)
    slider_width = 200
    slider_height = 20
    handle_radius = 10

    # SOUND FX Slider
    sound_text = slider_font.render("SOUND FX:", True, (0, 0, 0))
    settings.display_surface.blit(sound_text, (modal_x + 30, modal_y + 80))

    sound_slider_x = modal_x + 150
    sound_slider_y = modal_y + 90
    sound_handle_x = int(sound_slider_x + sound_volume * slider_width)

    pygame.draw.rect(settings.display_surface, (200, 200, 200), (sound_slider_x, sound_slider_y + slider_height // 2 - 2, slider_width, 4), border_radius=handle_radius)
    pygame.draw.rect(settings.display_surface, (0, 0, 0), (sound_slider_x, sound_slider_y + slider_height // 2 - 2, sound_handle_x - sound_slider_x, 4), border_radius=handle_radius)
    pygame.draw.circle(settings.display_surface, (0, 0, 0), (sound_handle_x, sound_slider_y + slider_height // 2), handle_radius)

    # MUSIC Slider
    music_text = slider_font.render("MUSIC:", True, (0, 0, 0))
    settings.display_surface.blit(music_text, (modal_x + 30, modal_y + 140))

    music_slider_x = modal_x + 150
    music_slider_y = modal_y + 150
    music_handle_x = int(music_slider_x + music_volume * slider_width)

    pygame.draw.rect(settings.display_surface, (200, 200, 200), (music_slider_x, music_slider_y + slider_height // 2 - 2, slider_width, 4), border_radius=handle_radius)
    pygame.draw.rect(settings.display_surface, (0, 0, 0), (music_slider_x, music_slider_y + slider_height // 2 - 2, music_handle_x - music_slider_x, 4), border_radius=handle_radius)
    pygame.draw.circle(settings.display_surface, (0, 0, 0), (music_handle_x, music_slider_y + slider_height // 2), handle_radius)

    # COLOUR-BLIND MODE Toggle
    cb_text = slider_font.render("COLOUR-BLIND MODE:", True, (0, 0, 0))
    settings.display_surface.blit(cb_text, (modal_x + 30, modal_y + 200))

    toggle_button_width, toggle_button_height = 50, 25
    toggle_button_x = modal_x + 300
    toggle_button_y = modal_y + 200
    toggle_button_rect = pygame.Rect(toggle_button_x, toggle_button_y, toggle_button_width, toggle_button_height)
    toggle_handle_x = toggle_button_x + (toggle_button_width - toggle_button_height) # + (toggle_button_width - toggle_button_height if colour_blind_mode else 0)

    pygame.draw.rect(settings.display_surface, (128, 128, 128), toggle_button_rect, border_radius=toggle_button_height // 2 - 2)
    pygame.draw.rect(settings.display_surface, (0, 128, 0) if colour_blind_mode else (1, 158, 115), toggle_button_rect.inflate(-2, -2), border_radius=toggle_button_height // 2 - 2)
    pygame.draw.circle(settings.display_surface, (255, 255, 255), (toggle_handle_x + toggle_button_height // 2, toggle_button_y + toggle_button_height // 2), toggle_button_height // 2 - 2)

    # Cancel and Save Buttons
    cancel_button = pygame.Rect(modal_x + 50, modal_y + 250, 100, 40)
    save_button = pygame.Rect(modal_x + 250, modal_y + 250, 100, 40)

    pygame.draw.rect(settings.display_surface, (200, 200, 200), cancel_button, border_radius=10)
    pygame.draw.rect(settings.display_surface, (200, 200, 200), save_button, border_radius=10)

    cancel_text = slider_font.render("CANCEL", True, (0, 0, 0))
    save_text = slider_font.render("SAVE", True, (0, 0, 0))

    settings.display_surface.blit(cancel_text, (cancel_button.centerx - cancel_text.get_width() // 2, cancel_button.centery - cancel_text.get_height() // 2))
    settings.display_surface.blit(save_text, (save_button.centerx - save_text.get_width() // 2, save_button.centery - save_text.get_height() // 2))

    # Handle slider dragging (updates state directly)
    if mouse_down:
        if sound_slider_x <= mouse_pos[0] <= sound_slider_x + slider_width and abs(mouse_pos[1] - (sound_slider_y + slider_height // 2)) <= handle_radius:
            sound_volume = (mouse_pos[0] - sound_slider_x) / slider_width
            new_settings_state["sound_fx_volume"] = max(0.0, min(1.0, sound_volume))  # Clamping

        if music_slider_x <= mouse_pos[0] <= music_slider_x + slider_width and abs(mouse_pos[1] - (music_slider_y + slider_height // 2)) <= handle_radius:
            music_volume = (mouse_pos[0] - music_slider_x) / slider_width
            new_settings_state["music_volume"] = max(0.0, min(1.0, music_volume))  # Clamping

    # Handle toggle button (updates state directly)
    if mouse_down and toggle_button_rect.collidepoint(mouse_pos):
        colour_blind_mode = not colour_blind_mode
        new_settings_state["colour_blind_mode"] = colour_blind_mode

    return cancel_button, save_button, new_settings_state



def saveSettings(new_settings_state):
    settings.SOUND_FX_VOLUME = new_settings_state["sound_fx_volume"]
    settings.MUSIC_VOLUME = new_settings_state["music_volume"]
    settings.COLOUR_BLIND_MODE = new_settings_state["colour_blind_mode"]


# SLIDER HELPERS:

def draw_slider(surface, x, y, width, height, handle_pos, handle_radius, active_colour, inactive_colour):
    """Draws a slider with the given parameters."""
    # Draw the slider bar
    pygame.draw.rect(surface, inactive_colour, (x, y + height // 2 - 2, width, 4))  # Full slider
    pygame.draw.rect(surface, active_colour, (x, y + height // 2 - 2, handle_pos - x, 4))  # Active portion

    # Draw the draggable handle
    pygame.draw.circle(surface, active_colour, (handle_pos, y + height // 2), handle_radius)

def handle_slider_drag(mouse_pos, mouse_down, x, y, width, handle_pos, handle_radius):
    """Handles slider drag interaction."""
    if mouse_down and abs(mouse_pos[0] - handle_pos) <= handle_radius and abs(mouse_pos[1] - (y + 10)) <= handle_radius:
        handle_pos = min(max(x, mouse_pos[0]), x + width)  # Clamp position between slider bounds
    return handle_pos
