import pygame
import settings
from Box import Box

class Block:
    def __init__(self, colour):
        self.x = 0
        self.y = 0

        self.surf = Box(settings.GAME_PIXEL_SIZE - 2, settings.GAME_PIXEL_SIZE - 2, colour, 1, 'black')
        self.colour = self.setColour(colour)

    def setColour(self, colour):
        try:
            self.colour = pygame.Color(colour)
            self.surf.fill(self.colour)
            return self.colour
        except ValueError as e:
            raise ValueError(f"Invalid color input: {colour}. Error: {e}")

    def blit(self):
        self.surf.blit(settings.GAME_X_OFFSET + self.x, settings.GAME_Y_OFFSET + self.y)

    def blitNext(self):
        self.surf.blit(settings.NEXT_PIECE_X + self.x, settings.NEXT_PIECE_Y + self.y)

    def blitHold(self):
        self.surf.blit(settings.HOLD_PIECE_X + self.x, settings.HOLD_PIECE_Y + self.y)
