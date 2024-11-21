import pygame
import random
import settings
from Box import Box
from Mino_L import Mino_L
from Mino_J import Mino_J
from Mino_O import Mino_O
from Mino_I import Mino_I
from Mino_S import Mino_S
from Mino_Z import Mino_Z
from Mino_T import Mino_T

def pickPiece():
    '''
    0 - O piece
    1 - I piece
    2 - S piece
    3 - Z piece
    4 - L piece
    5 - J piece
    6 - T piece
    '''
    mino = None
    i = random.randint(0,6)

    piece = {
        0: Mino_O,
        1: Mino_I,
        2: Mino_S,
        3: Mino_Z,
        4: Mino_L,
        5: Mino_J,
        6: Mino_T
    }
    mino = piece[i]()



# General Setup
pygame.init()
running = True

# tetris grid 20x10
game_board = Box(settings.GAME_WIDTH + 20, settings.GAME_HEIGHT + 20, 'white', 10, 'lightgray')

# tetris pieces
current = Mino_L()
current.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)





while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    settings.display_surface.fill('white')
    game_board.bilt(settings.WINDOW_WIDTH/2 - settings.GAME_WIDTH/2 - 10, settings.WINDOW_HEIGHT/2 - settings.GAME_HEIGHT/2 - 10)
    current.bilt()

    
    pygame.display.update()
    current.update()
    settings.KEYHANDLER.update()
    

# Close the window
pygame.quit()



