import pygame
import sys
import settings 
from menu import renderTitle

INSTRUCTIONS_TEXT = [
    "Welcome to Gesturis, which puts a twist on the classic game of Tetris",
    "by using hand gestures to control block movement and handling.",
    "",
    "GOAL: The main objective of the game is to arrange a series of shapes",
    "such that they form complete lines. Once a line has been filled/completed,",
    "it will disappear and increase your score.",
    "",
    "GAME END: If you fail to continuously clear lines, the blocks will",
    "eventually stack up to the top. If any block reaches the top of the board,",
    "it is GAME OVER.",
    "",
    "GAME CONTROLS: Blocks will come one at a time, and there are 6 possible",
    "actions the player can perform on the block.",
]



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

    MENU_BUTTON_WIDTH = 200
    MENU_BUTTON_HEIGHT = 66

    title_font = pygame.font.Font(None, 64)  # Adjust size as needed
    text_font = pygame.font.Font(None, 32)
    button_font = pygame.font.Font(None, 36)
    
    # Fill screen with menu background color
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        settings.display_surface.fill(settings.MENU_BG_COLOR)
        renderTitle(title_font, "GESTURIS", settings.GAME_PIXEL_SIZE * 20, settings.GAME_PIXEL_SIZE * 7)
    pygame.quit()
    sys.exit()


def displayInstructionsPage2(curr_state):
    print("IN INSTR PAGE 2")