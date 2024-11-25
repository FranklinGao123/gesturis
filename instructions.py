import pygame
import sys
import settings 
from menu import renderTitle

def write_text(surface, text, font, x, y):
    for line in text:
        line_surface = font.render(line, True, (255, 255, 255))
        surface.blit(line_surface, (x, y))
        y += line_surface.get_height() + 5
    
def draw_button(font, rect, text, is_hovered=False):
    """Draws a button with hover effects."""
    if is_hovered:
        pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, rect, border_radius=settings.BUTTON_CORNER_RADIUS)
    else:
        pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, rect, border_radius=settings.BUTTON_CORNER_RADIUS)
    pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, rect, 2, border_radius=settings.BUTTON_CORNER_RADIUS)
    button_text = font.render(text, True, settings.BUTTON_TEXT_COLOR )
    text_rect = button_text.get_rect(center=rect.center)
    settings.display_surface.blit(button_text, text_rect)


# Handle clicks for menu, back, and next buttons
def handleMenuClicks(menu_button, back_button, next_button, mouse_x, mouse_y, curr_state, back_state=None, next_state=None):
    if menu_button.collidepoint(mouse_x, mouse_y):
        return settings.GameState.MAIN_MENU
    elif back_state and back_button.collidepoint(mouse_x, mouse_y):
        return back_state
    elif next_state and next_button.collidepoint(mouse_x, mouse_y):
        return next_state
    return curr_state

def renderCommonInstructionElements(menu_button, back_button, next_button, subtitle_text):

    MENU_BUTTON_WIDTH = 150
    MENU_BUTTON_HEIGHT = 55
    MENU_BUTTON_X, MENU_BUTTON_Y = settings.GAME_PIXEL_SIZE * 2.5, settings.GAME_PIXEL_SIZE * 2

    ARROW_BUTTON_WIDTH = 75
    ARROW_BUTTON_HEIGHT = 43
    ARROW_BUTTON_Y = settings.WINDOW_HEIGHT - settings.GAME_PIXEL_SIZE * 3.5
    NEXT_BUTTON_X = settings.WINDOW_WIDTH - settings.GAME_PIXEL_SIZE * 6
    BACK_BUTTON_X = NEXT_BUTTON_X - ARROW_BUTTON_WIDTH - settings.GAME_PIXEL_SIZE*.5

    TEXT_LEFT_ALIGNMENT = settings.GAME_PIXEL_SIZE * 3.5

    SUBTITLE_TEXT_Y = settings.GAME_PIXEL_SIZE * 5

    title_font = pygame.font.Font(settings.FONT_PATH, 80)
    subtitle_font = pygame.font.Font(settings.FONT_PATH, 40)
    text_font = pygame.font.SysFont("courier", 16)
    button_font = pygame.font.Font(settings.FONT_PATH, 23)

    # Text
    menu_text = button_font.render("<- MENU", True, settings.BUTTON_TEXT_COLOR)
    back_text = button_font.render("<-", True, settings.BUTTON_TEXT_COLOR)
    next_text = button_font.render("->", True, settings.BUTTON_TEXT_COLOR)

    # Get text positions within buttons
    menu_text_width, menu_text_height = menu_text.get_size()
    menu_text_x = menu_button.centerx - menu_text_width // 2
    menu_text_y = menu_button.centery - menu_text_height // 2

    back_text_width, back_text_height = back_text.get_size()
    back_text_x = back_button.centerx - back_text_width // 2
    back_text_y = back_button.centery - back_text_height // 2

    next_text_width, next_text_height = next_text.get_size()
    next_text_x = next_button.centerx - next_text_width // 2
    next_text_y = next_button.centery - next_text_height // 2

    # Calculate positioning for title
    total_width = sum(title_font.render(c, True, settings.GESTURIS_COLOURS[0]).get_width() for c in "GESTURIS")
    title_x = (settings.WINDOW_WIDTH - total_width) // 2 # Set initial x position so that text is centered

    settings.display_surface.fill(settings.MENU_BG_COLOR)

    # Title
    total_width = sum(title_font.render(c, True, settings.GESTURIS_COLOURS[0]).get_width() for c in "GESTURIS")
    title_x = (settings.WINDOW_WIDTH - total_width) // 2
    renderTitle(title_font, "GESTURIS", title_x, settings.GAME_PIXEL_SIZE * 0.6)

    # Subtitle
    subtitle_surface = subtitle_font.render(subtitle_text, True, (255, 255, 255))
    settings.display_surface.blit(subtitle_surface, (settings.GAME_PIXEL_SIZE * 3.5, SUBTITLE_TEXT_Y))

    # Render buttons
    mouse_x, mouse_y = pygame.mouse.get_pos()

    def renderButton(button, text_surface, x, y):
        if button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, button, 0, settings.BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, button)
        pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)
        settings.display_surface.blit(text_surface, (x, y))

    # Create text surfaces
    menu_text = button_font.render("<- MENU", True, settings.BUTTON_TEXT_COLOR)
    back_text = button_font.render("<-", True, settings.BUTTON_TEXT_COLOR)
    next_text = button_font.render("->", True, settings.BUTTON_TEXT_COLOR)

    # Draw buttons
    menu_text_x = menu_button.centerx - menu_text.get_width() // 2
    menu_text_y = menu_button.centery - menu_text.get_height() // 2
    renderButton(menu_button, menu_text, menu_text_x, menu_text_y)

    back_text_x = back_button.centerx - back_text.get_width() // 2
    back_text_y = back_button.centery - back_text.get_height() // 2
    renderButton(back_button, back_text, back_text_x, back_text_y)

    next_text_x = next_button.centerx - next_text.get_width() // 2
    next_text_y = next_button.centery - next_text.get_height() // 2
    renderButton(next_button, next_text, next_text_x, next_text_y)

    # Check for button clicks and update state as needed


# This method will return a menu action
def displayInstructionsPage1(curr_state):

    running = True

    INSTRUCTIONS_TEXT = [
        "Welcome to Gesturis, which puts a twist on the classic game of Tetris by using hand gestures to",
        "control block movement and handling.",
        "",
        "GOAL: The main objective of the game is to arrange a series of shapes such that they form complete lines. Once",
        "a line has been filled/completed, it will disappear and increase your score. There are 7 different shapes",
        "total, each comprised of 4 block units, which you can move and rotate as they fall. Clearing more lines at once",
        "will score the player more points.",
        "",
        "GAME END: If you fail to continuously clear lines, the blocks will eventually stack up to the top. If any block",
        "reaches to very top of the playing board, it is GAME OVER.",
        "",
        "GAME CONTROLS: Blocks will come one at a time, and there are 6 possible actions the player can perform on the",
        "block - right movement, left movement, rotation clockwise/right, rotation counter-clockwise/left, hold/swap and",
        "drop. The player will create hand gestures to control the blocks (see next page)",
        "",
        "When a block is “swapped”, it switches the current block in play with the block in the “hold” position, and",
        "becomes the new block being held. If there is no block being held yet, the current block will simply move to",
        "the “hold” position and the next block will come in.",
        "",
        "Dropping a block will cause the current block to move all the way down until collision happens."
    ]
    TEXT_LEFT_ALIGNMENT = settings.GAME_PIXEL_SIZE * 3.5
    SUBTITLE_TEXT_Y = settings.GAME_PIXEL_SIZE * 5

    text_font = pygame.font.SysFont("courier", 16)

    # Button setup
    MENU_BUTTON_X, MENU_BUTTON_Y = settings.GAME_PIXEL_SIZE * 2.5, settings.GAME_PIXEL_SIZE * 2
    MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT = 150, 55

    ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT = 75, 43
    ARROW_BUTTON_Y = settings.WINDOW_HEIGHT - settings.GAME_PIXEL_SIZE * 3.5
    NEXT_BUTTON_X = settings.WINDOW_WIDTH - settings.GAME_PIXEL_SIZE * 6
    BACK_BUTTON_X = NEXT_BUTTON_X - ARROW_BUTTON_WIDTH - settings.GAME_PIXEL_SIZE * 0.5

    menu_button = pygame.Rect(MENU_BUTTON_X, MENU_BUTTON_Y, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
    back_button = pygame.Rect(BACK_BUTTON_X, ARROW_BUTTON_Y, ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT)
    next_button = pygame.Rect(NEXT_BUTTON_X, ARROW_BUTTON_Y, ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                new_state = handleMenuClicks(menu_button, back_button, next_button, mouse_x, mouse_y, curr_state, next_state=settings.GameState.INSTRUCTIONS_2)
                if new_state != curr_state:
                    return new_state  # Exit current instructions page and change state

        renderCommonInstructionElements(menu_button, back_button, next_button, "HOW TO PLAY")

        # Draw instructions text
        write_text(settings.display_surface, INSTRUCTIONS_TEXT, text_font, TEXT_LEFT_ALIGNMENT, SUBTITLE_TEXT_Y + (settings.GAME_PIXEL_SIZE * 2.75))

        pygame.display.update()
    
    pygame.quit()
    sys.exit()


def displayInstructionsPage2(curr_state):
    running = True

     # Button setup
    MENU_BUTTON_X, MENU_BUTTON_Y = settings.GAME_PIXEL_SIZE * 2.5, settings.GAME_PIXEL_SIZE * 2
    MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT = 150, 55

    ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT = 75, 43
    ARROW_BUTTON_Y = settings.WINDOW_HEIGHT - settings.GAME_PIXEL_SIZE * 3.5
    NEXT_BUTTON_X = settings.WINDOW_WIDTH - settings.GAME_PIXEL_SIZE * 6
    BACK_BUTTON_X = NEXT_BUTTON_X - ARROW_BUTTON_WIDTH - settings.GAME_PIXEL_SIZE * 0.5

    menu_button = pygame.Rect(MENU_BUTTON_X, MENU_BUTTON_Y, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
    back_button = pygame.Rect(BACK_BUTTON_X, ARROW_BUTTON_Y, ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT)
    next_button = pygame.Rect(NEXT_BUTTON_X, ARROW_BUTTON_Y, ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT)

    INSTRUCTIONS_TEXT = [
        "Hello"
    ]

    # Load images
    ICON_SCALE = 100
    victory_hand = pygame.image.load("images/victory_hand.png")
    scaled_victory_hand = pygame.transform.scale(victory_hand, (ICON_SCALE, ICON_SCALE))

    point_hand = pygame.image.load("images/point_hand.png")
    scaled_point_hand = pygame.transform.scale(point_hand, (ICON_SCALE, ICON_SCALE))

    thumbs_up = pygame.image.load("images/thumbs_up.png")
    scaled_thumbs_up = pygame.transform.scale(thumbs_up, (ICON_SCALE, ICON_SCALE))

    thumbs_down = pygame.image.load("images/thumbs_down.png")
    scaled_thumbs_down = pygame.transform.scale(thumbs_down, (ICON_SCALE, ICON_SCALE))

    open_palm = pygame.image.load("images/open_palm.png")
    scaled_open_palm = pygame.transform.scale(open_palm, (ICON_SCALE, ICON_SCALE))

    i_love_you = pygame.image.load("images/i_love_you.png")
    scaled_i_love_you = pygame.transform.scale(i_love_you, (ICON_SCALE, ICON_SCALE))

    TEXT_LEFT_ALIGNMENT = settings.GAME_PIXEL_SIZE * 3.5
    SUBTITLE_TEXT_Y = settings.GAME_PIXEL_SIZE * 5

    # Text settings
    gesture_type_font = pygame.font.Font(settings.FONT_PATH, 20)
    text_font = pygame.font.SysFont("courier", 16)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                new_state = handleMenuClicks(menu_button, back_button, next_button, mouse_x, mouse_y, curr_state, back_state=settings.GameState.INSTRUCTIONS_1)
                if new_state != curr_state:
                    return new_state  # Exit current instructions page and change state

        renderCommonInstructionElements(menu_button, back_button, next_button, "GESTURES:")

        # Draw instructions text
        write_text(settings.display_surface, INSTRUCTIONS_TEXT, text_font, TEXT_LEFT_ALIGNMENT, SUBTITLE_TEXT_Y + (settings.GAME_PIXEL_SIZE * 2.75))

        pygame.display.update()
    
    pygame.quit()
    sys.exit()