import pygame
import settings
from Box import Box

class Block:
    def __init__(self, colour):
        self.x = 0
        self.y = 0
        self.colour = colour

        self.surf = Box(settings.GAME_PIXEL_SIZE - 2, settings.GAME_PIXEL_SIZE - 2, colour, 1, 'black')

    def colour(self, colour):
        self.colour = colour
        self.surf.fill(colour)

    def bilt(self):
        self.surf.bilt(settings.GAME_X_OFFSET + self.x, settings.GAME_Y_OFFSET + self.y)