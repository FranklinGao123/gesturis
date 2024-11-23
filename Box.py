import pygame
import settings

class Box:
    """
    A class for creating a box.

    Attributes:
        width (int): The width of the box.
        height (int): The height of the box.
        fill_colour (string): The colour of the box.
        outline (int): The thickness of the outline of the box.
        outline_colour (int): The colour of the outline of the box.
    """
    def __init__(self, width, height, fill_colour, outline=0, outline_colour=None):
        """
        Initialize the box

        Parameters:
            width (int): The width of the box.
            height (int): The height of the box.
            fill_colour (string): The colour of the box.
            outline (int): The thickness of the outline of the box.
            outline_colour (int): The colour of the outline of the box.
        """
        self.width = width
        self.height = height
        self.outline = outline
        self.outline_colour = outline_colour
        self.fill_colour = fill_colour


        self.surf_outline = pygame.Surface((width + outline * 2, height + outline * 2))
        if outline_colour:
            self.surf_outline.fill(outline_colour)
        self.surf = pygame.Surface((width, height))
        self.surf.fill(fill_colour)

    def blit(self, x, y):
        """
        Printing the box onto the screen

        Parameters:
            x (int): The x-coordinate of the screen.
            y (int): the y-coordinate fo the screen.
        """
        settings.display_surface.blit(self.surf_outline, (x - self.outline, y - self.outline))
        settings.display_surface.blit(self.surf, (x, y))

    def fill(self, fill_colour):
        """
        Updates the fill color of the inner surface.

        Parameters:
            fill_colour (string): The new fill color.
        """
        self.fill_colour = fill_colour
        self.surf.fill(fill_colour)