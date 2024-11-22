import pygame
from Key_Handler import Key_Handler

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Gesturis')

GAME_PIXEL_SIZE = 25
GAME_WIDTH, GAME_HEIGHT = 10 * GAME_PIXEL_SIZE, 20 * GAME_PIXEL_SIZE
GAME_X_OFFSET = WINDOW_WIDTH/2 - GAME_WIDTH/2
GAME_Y_OFFSET = WINDOW_HEIGHT/2 - GAME_HEIGHT/2

# Box settings
BOX_LINE_WIDTH = 10
BOX_LINE_COLOUR = 'white'
BOX_FILL_COLOUR = 'black'

START_LOCATION_X, START_LOCATION_Y = GAME_WIDTH/2 - GAME_PIXEL_SIZE, GAME_PIXEL_SIZE

NEXT_BOX_X, NEXT_BOX_Y = GAME_X_OFFSET - 225, GAME_Y_OFFSET
HOLD_BOX_X, HOLD_BOX_Y = GAME_X_OFFSET + (1.5*225), GAME_Y_OFFSET
STATS_BOX_X, STATS_BOX_Y = GAME_X_OFFSET - 300, GAME_Y_OFFSET + (GAME_PIXEL_SIZE * 14)
GESTURES_BOX_X, GESTURES_BOX_Y = GAME_X_OFFSET + (1.5*225), GAME_Y_OFFSET + (GAME_PIXEL_SIZE * 8)

HOLD_PIECE_X, HOLD_PIECE_Y = GAME_X_OFFSET + GAME_PIXEL_SIZE * 10 + 50, GAME_Y_OFFSET

DROP_INTERVAL = 60

INPUT_INTERVAL = 10

KEYHANDLER = Key_Handler()

staticBlocks = list()

hold = None
held = False