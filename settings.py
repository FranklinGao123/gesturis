import pygame
from Key_Handler import Key_Handler
from enum import Enum

class GameState(Enum):
    MAIN_MENU = "main menu"
    SINGLEPLAYER = "singleplayer"
    MULTIPLAYER = "multiplayer"
    PAUSE = "pause"
    SETTINGS = "settings"
    INSTRUCTIONS_1 = "instructions1"
    INSTRUCTIONS_2 = "instructions2"
    QUIT = "quit"

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Gesturis')

# Basic dimenion settings
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

# Gestures coordinates
INDIV_GESTURES_TEXT_X = GESTURES_BOX_X + (GAME_PIXEL_SIZE * .75)
RIGHT_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 2.5)
LEFT_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 4)
ROTATE_RIGHT_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 5.5)
ROTATE_LEFT_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 7)
HOLD_SWAP_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 8.5)
DROP_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 10)

# Piece Positionings
NEXT_PIECE_X, NEXT_PIECE_Y = GAME_X_OFFSET - (GAME_PIXEL_SIZE * 6.5), GAME_Y_OFFSET + (GAME_PIXEL_SIZE * 3)
HOLD_PIECE_X, HOLD_PIECE_Y = GAME_X_OFFSET + GAME_PIXEL_SIZE * 10 + 50, GAME_Y_OFFSET


DROP_INTERVAL = 600

INPUT_INTERVAL = 100

KEYHANDLER = Key_Handler()

staticBlocks = list()

hold = None
held = False