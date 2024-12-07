import pygame
from Key_Handler import Key_Handler
from Recognizer_Task import Recognizer_Task
from enum import Enum
from Mino_L import Mino_L
from Mino_J import Mino_J
from Mino_O import Mino_O
from Mino_I import Mino_I
from Mino_S import Mino_S
from Mino_Z import Mino_Z
from Mino_T import Mino_T

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

FONT_PATH = "./fonts/kenney-mini.ttf"
GESTURIS_COLOURS = [
    "#E15A06",
    "#FAA144",
    "#FFD75A",
    "#00D053",
    "#384FDC",
    "#C64FA4"
]

# Basic dimenion settings
GAME_PIXEL_SIZE = 25
GAME_WIDTH, GAME_HEIGHT = 9 * GAME_PIXEL_SIZE, 20 * GAME_PIXEL_SIZE
GAME_X_OFFSET = WINDOW_WIDTH/2 - GAME_WIDTH/2
GAME_Y_OFFSET = WINDOW_HEIGHT/2 - GAME_HEIGHT/2

# Box settings
BOX_LINE_WIDTH = 10
BOX_LINE_COLOUR = 'white'
BOX_FILL_COLOUR = 'black'

START_LOCATION_X, START_LOCATION_Y = GAME_WIDTH/2 - GAME_PIXEL_SIZE * 0.5, GAME_PIXEL_SIZE

NEXT_BOX_X, NEXT_BOX_Y = GAME_X_OFFSET - 225, GAME_Y_OFFSET
HOLD_BOX_X, HOLD_BOX_Y = GAME_X_OFFSET + (1.5*225), GAME_Y_OFFSET
STATS_BOX_X, STATS_BOX_Y = GAME_X_OFFSET - 300, GAME_Y_OFFSET + (GAME_PIXEL_SIZE * 14)
GESTURES_BOX_X, GESTURES_BOX_Y = GAME_X_OFFSET + (1.5*225), GAME_Y_OFFSET + (GAME_PIXEL_SIZE * 8)

# Button settings
MENU_BG_COLOR, BUTTON_COLOR = (0, 0, 0), (0, 0, 0)
BUTTON_HOVER_COLOR = (69, 69, 69)
BUTTON_TEXT_COLOR, BUTTON_OUTLINE_COLOR = (255, 255, 255), (255, 255, 255)
BUTTON_OUTLINE_WIDTH = 3
BUTTON_CORNER_RADIUS = 20

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


DROP_INTERVAL = 5

INPUT_INTERVAL = 5

KEYHANDLER = Key_Handler()

RECOGNIZER = Recognizer_Task()

staticBlocks = list()

hold = None
held = False

# bag = [Mino_O, Mino_I, Mino_S, Mino_Z, Mino_L, Mino_J, Mino_T]
cur_bag = []
