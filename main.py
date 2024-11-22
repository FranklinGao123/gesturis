import pygame
import random
import settings
import os
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

# Font & Text
font = pygame.font.SysFont("monaco", 18)  # Default font
bold_font = pygame.font.SysFont("monaco", 20, bold=True)  # Default font, size 48

if os.name == "posix":  # macOS or Linux
    emoji_font = pygame.font.SysFont("arial", 18)  # macOS
    # For Linux, use a path to an emoji font like Noto Color Emoji
    # font = pygame.font.Font("/usr/share/fonts/noto/NotoColorEmoji.ttf", 48)
elif os.name == "nt":  # Windows
    emoji_font = pygame.font.SysFont("segoeuiemoji", 18)
else:
    raise Exception("Unsupported platform for emoji rendering")


next_text = bold_font.render("NEXT", True, (255, 255, 255))
hold_text = bold_font.render("HOLD", True, (255, 255, 255))

score_text = font.render("SCORE:", True, (255, 255, 255))
lines_text = font.render("LINES:", True, (255, 255, 255))
mode_text = font.render("MODE:", True, (255, 255, 255))

gestures_text = bold_font.render("GESTURES:", True, (255, 255, 255))
right_text = emoji_font.render("RIGHT: ", True, (255, 255, 255))
left_text = emoji_font.render("LEFT: ", True, (255, 255, 255))
rotate_right_text = emoji_font.render("ROTATE RIGHT: ", True, (255, 255, 255))
rotate_left_text = emoji_font.render("ROTATE LEFT: ", True, (255, 255, 255))
hold_swap_text = emoji_font.render("HOLD/SWAP: ", True, (255, 255, 255))
drop_text = emoji_font.render("DROP: ", True, (255, 255, 255))

# right_text = emoji_font.render("RIGHT: ✌🏻", True, (255, 255, 255))
# left_text = emoji_font.render("LEFT: ☝🏻", True, (255, 255, 255))
# rotate_right_text = emoji_font.render("ROTATE RIGHT: 👍🏻", True, (255, 255, 255))
# rotate_left_text = emoji_font.render("ROTATE LEFT: 👎🏻", True, (255, 255, 255))
# hold_swap_text = emoji_font.render("HOLD/SWAP: 🤟🏻", True, (255, 255, 255))
# drop_text = emoji_font.render("DROP: 🖐🏻", True, (255, 255, 255))

# Board + Boxes (tetris grid 20x10)
game_board = Box(settings.GAME_WIDTH + 25, settings.GAME_HEIGHT + 25, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)
next_box = Box(settings.GAME_PIXEL_SIZE * 6, settings.GAME_PIXEL_SIZE * 6, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)
hold_box = Box(settings.GAME_PIXEL_SIZE * 6, settings.GAME_PIXEL_SIZE * 6, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)
stats_box = Box(settings.GAME_PIXEL_SIZE * 9, settings.GAME_PIXEL_SIZE * 6, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)
gestures_box = Box(settings.GAME_PIXEL_SIZE * 9, settings.GAME_PIXEL_SIZE * 12, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)

staticBlocks = list()

# Tetris pieces
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
            
    settings.display_surface.fill('black')


    # Display board + boxes
    game_board.bilt(settings.WINDOW_WIDTH/2 - settings.GAME_WIDTH/2 - settings.BOX_LINE_WIDTH, settings.WINDOW_HEIGHT/2 - settings.GAME_HEIGHT/2 - settings.BOX_LINE_WIDTH)
    next_box.bilt(settings.NEXT_BOX_X, settings.NEXT_BOX_Y)
    hold_box.bilt(settings.HOLD_BOX_X, settings.HOLD_BOX_Y)
    stats_box.bilt(settings.STATS_BOX_X, settings.STATS_BOX_Y)
    gestures_box.bilt(settings.GESTURES_BOX_X, settings.GESTURES_BOX_Y)

    # Display Text
    settings.display_surface.blit(next_text, (settings.NEXT_BOX_X + (settings.GAME_PIXEL_SIZE * 2), settings.NEXT_BOX_Y + (settings.GAME_PIXEL_SIZE * .5)))
    settings.display_surface.blit(hold_text, (settings.HOLD_BOX_X + (settings.GAME_PIXEL_SIZE * 1.9), settings.HOLD_BOX_Y + (settings.GAME_PIXEL_SIZE * .5)))

    settings.display_surface.blit(score_text, (settings.STATS_BOX_X + (settings.GAME_PIXEL_SIZE * .75), settings.STATS_BOX_Y + (settings.GAME_PIXEL_SIZE * .5)))
    settings.display_surface.blit(lines_text, (settings.STATS_BOX_X + (settings.GAME_PIXEL_SIZE * .75), settings.STATS_BOX_Y + (settings.GAME_PIXEL_SIZE * 2.5)))
    settings.display_surface.blit(mode_text, (settings.STATS_BOX_X + (settings.GAME_PIXEL_SIZE * .75), settings.STATS_BOX_Y + (settings.GAME_PIXEL_SIZE * 4.5)))

    settings.display_surface.blit(gestures_text, (settings.GESTURES_BOX_X + (settings.GAME_PIXEL_SIZE * 2.5), settings.GESTURES_BOX_Y + (settings.GAME_PIXEL_SIZE * .5)))
    settings.display_surface.blit(right_text, (settings.GESTURES_BOX_X + (settings.GAME_PIXEL_SIZE * 1), settings.GESTURES_BOX_Y + (settings.GAME_PIXEL_SIZE * 2.5)))
    settings.display_surface.blit(left_text, (settings.GESTURES_BOX_X + (settings.GAME_PIXEL_SIZE * 1), settings.GESTURES_BOX_Y + (settings.GAME_PIXEL_SIZE * 4)))
    settings.display_surface.blit(rotate_right_text, (settings.GESTURES_BOX_X + (settings.GAME_PIXEL_SIZE * 1), settings.GESTURES_BOX_Y + (settings.GAME_PIXEL_SIZE * 5.5)))
    settings.display_surface.blit(rotate_left_text, (settings.GESTURES_BOX_X + (settings.GAME_PIXEL_SIZE * 1), settings.GESTURES_BOX_Y + (settings.GAME_PIXEL_SIZE * 7)))
    settings.display_surface.blit(hold_swap_text, (settings.GESTURES_BOX_X + (settings.GAME_PIXEL_SIZE * 1), settings.GESTURES_BOX_Y + (settings.GAME_PIXEL_SIZE * 8.5)))
    settings.display_surface.blit(drop_text, (settings.GESTURES_BOX_X + (settings.GAME_PIXEL_SIZE * 1), settings.GESTURES_BOX_Y + (settings.GAME_PIXEL_SIZE * 10)))

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



