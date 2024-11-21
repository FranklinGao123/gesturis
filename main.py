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
    return piece[i]()

def checkLineClear():
    grid = list()
    for i in range(10):
        temp = list()
        for j in range(20):
            temp.append(None)
        grid.append(temp)

    for i in range(len(settings.staticBlocks)):
        grid[int(settings.staticBlocks[i].x / settings.GAME_PIXEL_SIZE)][int(settings.staticBlocks[i].y / settings.GAME_PIXEL_SIZE)] = i

    delete = list()

    offset = 0
    for y in range(19, 0 , -1):
        clear = True
        for x in range(10):
            if grid[x][y] is None:
                clear = False
            else:
                settings.staticBlocks[grid[x][y]].y += offset
            
        if clear:
            for x in range(10):
                delete.append(settings.staticBlocks[grid[x][y]])
            offset += settings.GAME_PIXEL_SIZE
    
    for i in delete:
        settings.staticBlocks.remove(i)
        



# General Setup
pygame.init()
running = True

# tetris grid 20x10
game_board = Box(settings.GAME_WIDTH, settings.GAME_HEIGHT, 'white', 10, 'lightgray')
next_piece = Box(settings.GAME_PIXEL_SIZE * 6, settings.GAME_PIXEL_SIZE * 6, 'white', 10, 'lightgray')
hold_piece = Box(settings.GAME_PIXEL_SIZE * 6, settings.GAME_PIXEL_SIZE * 6, 'white', 10, 'lightgray')

# tetris pieces
current = Mino_J()
current.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)
current.setActivePiece()
next = pickPiece()
next.setXY(0,0)


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    settings.display_surface.fill('white')
    game_board.bilt(settings.WINDOW_WIDTH/2 - settings.GAME_WIDTH/2 - 1, settings.WINDOW_HEIGHT/2 - settings.GAME_HEIGHT/2 - 1)
    next_piece.bilt(settings.NEXT_PIECE_X, settings.NEXT_PIECE_Y)
    hold_piece.bilt(settings.HOLD_PIECE_X, settings.HOLD_PIECE_Y)

    for i in settings.staticBlocks:
        i.bilt()
    current.bilt()
    next.biltNext()
    if settings.hold:
        settings.hold.biltHold()


    
    pygame.display.update()
    current.update()
    if current.hold:
        if settings.hold is None:
            settings.hold = current
            current = next
            current.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)
            current.setActivePiece()
            next = pickPiece()
            next.setXY(0,0)
        else:
            temp = current
            current = settings.hold
            settings.hold = temp
            current.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)
            current.auto_drop_counter = 0
            current.hold = False
        
    if not current.active:
        settings.held = False
        for i in current.b:
            settings.staticBlocks.append(i)
        current = next
        current.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)
        current.setActivePiece()
        next = pickPiece()
        next.setXY(0,0)
        checkLineClear()
    settings.KEYHANDLER.update()
    

# Close the window
pygame.quit()



