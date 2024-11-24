import pygame
import sys
import settings 

def renderTitle(title_font, text, x, y):
    offset_x = x
    colour_ind = 0
    for c in text:
        if colour_ind == len(settings.GESTURIS_COLOURS) - 1:
            colour_ind = 0
        letter = title_font.render(c, True, settings.GESTURIS_COLOURS[colour_ind])
        settings.display_surface.blit(letter, (offset_x, y))
        offset_x += letter.get_width()
        colour_ind += 1

def drawButtonWithText(button_rect, text, font, text_color, button_color, outline_color, outline_width):
    # Calculate the text surface
    text_surface = font.render(text, True, text_color)
    text_width, text_height = text_surface.get_size()

    # Calculate the position to center the text within the button
    text_x = button_rect.centerx - text_width // 2
    text_y = button_rect.centery - text_height // 2

    # Draw the button (you can add outline if necessary)
    pygame.draw.rect(settings.display_surface, button_color, button_rect)
    pygame.draw.rect(settings.display_surface, outline_color, button_rect, outline_width)

    # Draw the text centered within the button
    settings.display_surface.blit(text_surface, (text_x, text_y))
