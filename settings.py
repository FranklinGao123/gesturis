import pygame
from Key_Handler import Key_Handler

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Gesturis')

GAME_PIXEL_SIZE = 25
GAME_WIDTH, GAME_HEIGHT = 10 * GAME_PIXEL_SIZE, 20 * GAME_PIXEL_SIZE
GAME_X_OFFSET = WINDOW_WIDTH/2 - GAME_WIDTH/2
GAME_Y_OFFSET = WINDOW_HEIGHT/2 - GAME_HEIGHT/2

START_LOCATION_X, START_LOCATION_Y = GAME_WIDTH/2 - GAME_PIXEL_SIZE, GAME_PIXEL_SIZE

NEXT_PIECE_X, NEXT_PIECE_Y = START_LOCATION_X - WINDOW_WIDTH/2 + GAME_WIDTH * 1.5,  START_LOCATION_Y - WINDOW_HEIGHT/2 - GAME_HEIGHT/4

DROP_INTERVAL = 60

INPUT_INTERVAL = 10

KEYHANDLER = Key_Handler()