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

FONT_PATH = "fonts/kenney-mini.ttf"
GESTURIS_COLOURS = [
    "#FF1945",
    "#FF6C13",
    "#E1B400",
    "#0EA41E",
    "#4E84FE",
    "#AD00FA"
]
GESTURIS_COLOURS_COLOUR_BLIND = [
    "#E15A06",
    "#FAA144",
    "#FFD75A",
    "#00D053",
    "#384FDC",
    "#C64FA4"
]

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
GESTURES_BOX_X, GESTURES_BOX_Y = GAME_X_OFFSET + (1.5*225), GAME_Y_OFFSET + (GAME_PIXEL_SIZE * 9)

# Button settings
MENU_BG_COLOUR, BUTTON_COLOUR, BUTTON_COLOUR_INVERTED = (0, 0, 0), (0, 0, 0), (255, 255, 255)
BUTTON_HOVER_COLOUR, BUTTON_HOVER_COLOUR_LIGHT = (69, 69, 69), (208, 208, 208)
BUTTON_TEXT_COLOUR, BUTTON_OUTLINE_COLOUR = (255, 255, 255), (255, 255, 255)
BUTTON_OUTLINE_WIDTH = 3
BUTTON_CORNER_RADIUS = 20

# Gestures coordinates
INDIV_GESTURES_TEXT_X = GESTURES_BOX_X + (GAME_PIXEL_SIZE * .75)
RIGHT_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 2)
LEFT_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 3.5)
ROTATE_RIGHT_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 5)
ROTATE_LEFT_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 6.5)
HOLD_SWAP_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 8)
DROP_TEXT_Y = GESTURES_BOX_Y + (GAME_PIXEL_SIZE * 9.5)

# Piece Positionings
NEXT_PIECE_X, NEXT_PIECE_Y = GAME_X_OFFSET - (GAME_PIXEL_SIZE * 6.5), GAME_Y_OFFSET + (GAME_PIXEL_SIZE * 3)
HOLD_PIECE_X, HOLD_PIECE_Y = GAME_X_OFFSET + GAME_PIXEL_SIZE * 10 + 50, GAME_Y_OFFSET + (GAME_PIXEL_SIZE * 2)

# User settings
# COLOUR_BLIND_MODE = False
# SOUND_FX_VOLUME = 100
# MUSIC_VOLUME = 100

SETTINGS_STATE = {
    "sound_fx_volume": 0.5,
    "music_volume": 0.5,
    "colour_blind_mode": False,
}

PLAYER_1_TURN = True # true means player 1 turn, false means player 2

DROP_INTERVAL = 600

INPUT_INTERVAL = 100

KEYHANDLER = Key_Handler()

staticBlocks = list()

hold = None
held = False