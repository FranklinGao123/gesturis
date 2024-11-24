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

    # Buttons
    menu_button = pygame.Rect(MENU_BUTTON_X, MENU_BUTTON_Y, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
    back_button = pygame.Rect(BACK_BUTTON_X, ARROW_BUTTON_Y, ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT)
    next_button = pygame.Rect(NEXT_BUTTON_X, ARROW_BUTTON_Y, ARROW_BUTTON_WIDTH, ARROW_BUTTON_HEIGHT)

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
    
    # Fill screen with menu background color
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        settings.display_surface.fill(settings.MENU_BG_COLOR)
        renderTitle(title_font, "GESTURIS", title_x, settings.GAME_PIXEL_SIZE * 0.6)

        subtitle_text = subtitle_font.render("HOW TO PLAY", True, (255, 255, 255))
        settings.display_surface.blit(subtitle_text, (TEXT_LEFT_ALIGNMENT, SUBTITLE_TEXT_Y))

        # Draw instructions text
        write_text(settings.display_surface, INSTRUCTIONS_TEXT, text_font, TEXT_LEFT_ALIGNMENT, SUBTITLE_TEXT_Y + (settings.GAME_PIXEL_SIZE * 2.75))

        # Draw buttons with hover effect
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if menu_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, menu_button, 0, settings.BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, menu_button)
        pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, menu_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

        if back_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, back_button, 0, settings.BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, back_button)
        pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, back_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

        if next_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(settings.display_surface, settings.BUTTON_HOVER_COLOR, next_button, 0, settings.BUTTON_CORNER_RADIUS)
        else:
            pygame.draw.rect(settings.display_surface, settings.BUTTON_COLOR, next_button)
        pygame.draw.rect(settings.display_surface, settings.BUTTON_OUTLINE_COLOR, next_button, settings.BUTTON_OUTLINE_WIDTH, settings.BUTTON_CORNER_RADIUS)

        # Draw button text
        settings.display_surface.blit(menu_text, (menu_text_x, menu_text_y))
        settings.display_surface.blit(back_text, (back_text_x, back_text_y))
        settings.display_surface.blit(next_text, (next_text_x, next_text_y))

        pygame.display.update()
    
    pygame.quit()
    sys.exit()


def displayInstructionsPage2(curr_state):
    print("IN INSTR PAGE 2")