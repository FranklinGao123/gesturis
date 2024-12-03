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
        pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOUR, rect, border_radius=settings.BUTTON_CORNER_RADIUS)
    else:
        pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOUR, rect, border_radius=settings.BUTTON_CORNER_RADIUS)
    pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOUR, rect, 2, border_radius=settings.BUTTON_CORNER_RADIUS)
    button_text = font.render(text, True, settings.BUTTON_TEXT_COLOUR )
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
    menu_text = button_font.render("<- MENU", True, settings.BUTTON_TEXT_COLOUR)
    back_text = button_font.render("<-", True, settings.BUTTON_TEXT_COLOUR)
    next_text = button_font.render("->", True, settings.BUTTON_TEXT_COLOUR)

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

    settings.display_surface.fill(settings.MENU_BG_COLOUR)

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
            pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOUR, button, 0, settings.BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOUR, button)
        pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOUR, button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)
        settings.display_surface.blit(text_surface, (x, y))

    # Create text surfaces
    menu_text = button_font.render("<- MENU", True, settings.BUTTON_TEXT_COLOUR)
    back_text = button_font.render("<-", True, settings.BUTTON_TEXT_COLOUR)
    next_text = button_font.render("->", True, settings.BUTTON_TEXT_COLOUR)

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


def wrap_text(text, font, max_width):
    """Wrap text to fit within a specified width."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        # Check if adding the next word exceeds the width
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:  # Add the last line
        lines.append(' '.join(current_line))

    return lines



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

    ICON_SCALE = 100
    
    # Load and scale images
    ICON_SCALE = 80
    gestures = {
        "MOVE RIGHT": {"image": pygame.image.load("images/thumbs_up.png"), "desc": "Make a thumbs UP motion with one hand."},
        "ROTATE RIGHT": {"image": pygame.image.load("images/point_hand.png"), "desc": "Point up with your index finger in one hand."},
        "SWAP/HOLD": {"image": pygame.image.load("images/i_love_you.png"), "desc": "Make an 'I love you' hand sign."},
        "MOVE LEFT": {"image": pygame.image.load("images/thumbs_down.png"), "desc": "Make a thumbs DOWN motion with one hand."},
        "ROTATE LEFT": {"image": pygame.image.load("images/victory_hand.png"), "desc": "Make a 'peace' sign with one hand."},
        "DROP BLOCK": {"image": pygame.image.load("images/open_palm.png"), "desc": "Make a fist with one hand."},
    }

    for key in gestures:
        gestures[key]["image"] = pygame.transform.scale(gestures[key]["image"], (ICON_SCALE, ICON_SCALE))

    # Text settings
    gesture_type_font = pygame.font.Font(settings.FONT_PATH, 20)
    text_font = pygame.font.SysFont("courier", 16)

    # Positioning variables
    GESTURE_X_START = settings.GAME_PIXEL_SIZE * 5
    GESTURE_Y_START = settings.GAME_PIXEL_SIZE * 8
    GESTURE_SPACING_X = settings.GAME_PIXEL_SIZE * 15
    GESTURE_SPACING_Y = settings.GAME_PIXEL_SIZE * 9.25

    TEXT_WRAP_WIDTH = GESTURE_SPACING_X - 100  # Adjust width based on spacing
    DESCRIPTION_LINE_HEIGHT = 20  # Spacing between lines in wrapped text

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

        # Draw gesture images and labels
        row, col = 0, 0
        for gesture, details in gestures.items():
            # Calculate positions
            x = GESTURE_X_START + (col * GESTURE_SPACING_X)
            y = GESTURE_Y_START + (row * GESTURE_SPACING_Y)
            text_start_y_offset = y + settings.GAME_PIXEL_SIZE * 1.2

            # Draw image
            settings.display_surface.blit(details["image"], (x + (settings.GAME_PIXEL_SIZE * 3.5), y))

            # Draw gesture label
            label_surface = gesture_type_font.render(gesture, True, (255, 255, 255))
            settings.display_surface.blit(label_surface, (x + (settings.GAME_PIXEL_SIZE * 2.7), y + ICON_SCALE + 5))

            # Wrap and draw description
            wrapped_lines = wrap_text(details["desc"], text_font, TEXT_WRAP_WIDTH)
            for i, line in enumerate(wrapped_lines):
                text_ypos = text_start_y_offset + ICON_SCALE + 30 + i * DESCRIPTION_LINE_HEIGHT
                desc_surface = text_font.render(line, True, (200, 200, 200))
                settings.display_surface.blit(desc_surface, (x, text_ypos)) # if i != 0 else text_ypos + 20))

            # Update row and column
            col += 1
            if col > 2:  # 3 columns per row
                col = 0
                row += 1

        pygame.display.update()
    
    pygame.quit()
    sys.exit()