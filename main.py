import pygame
import random
import settings
import sys
import os
from Box import Box
from Mino_L import Mino_L
from Mino_J import Mino_J
from Mino_O import Mino_O
from Mino_I import Mino_I
from Mino_S import Mino_S
from Mino_Z import Mino_Z
from Mino_T import Mino_T
from menu import displayMenu
from instructions import displayInstructionsPage1, displayInstructionsPage2

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

# Return the number updated number of lines and updated score
def checkLineClear(lines, score):
    grid = list()
    total_lines_cleared = 0

    # Create empty grid
    for i in range(10):
        temp = list()
        for j in range(20):
            temp.append(None)
        grid.append(temp)

    # Map in current static blocks into our empty grid
    for i in range(len(settings.staticBlocks)):
        grid[int(settings.staticBlocks[i].x / settings.GAME_PIXEL_SIZE)][int(settings.staticBlocks[i].y / settings.GAME_PIXEL_SIZE)] = i

    delete = list()
 
    offset = 0 # to keep track of how far down non-cleared blocks have to move
    for y in range(19, 0 , -1):
        clear = True
        for x in range(10):
            if grid[x][y] is None: # there is an empty block => not clearable
                clear = False
            else:
                settings.staticBlocks[grid[x][y]].y += offset
            
        if clear:  # current row can be cleared
            total_lines_cleared += 1
            for x in range(10):
                delete.append(settings.staticBlocks[grid[x][y]])
            offset += settings.GAME_PIXEL_SIZE
    
    for i in delete:
        settings.staticBlocks.remove(i)

    # Update score based on number of cleared lines, update # lines cleared total
    lines += total_lines_cleared
    if total_lines_cleared == 1:
        score += 10
    elif total_lines_cleared == 2:
        score += 30
    elif total_lines_cleared == 3:
        score += 50
    elif total_lines_cleared == 4:
        score += 80
    
    return (lines, score)

# General Setup
pygame.init()

def runGame(curr_state):
    running = True
    score = 0
    lines = 0
    mode = "SINGLE" # TODO: update when we deal with mode switching

    # Font & Text
    in_game_font = pygame.font.Font(settings.FONT_PATH, 20)  # Default font
    heading_font = pygame.font.Font(settings.FONT_PATH, 22)  # Default font, size 48

    if os.name == "posix":  # macOS or Linux
        emoji_font = pygame.font.SysFont("arial", 18)  # macOS
        # For Linux, use a path to an emoji font like Noto Color Emoji
        # font = pygame.font.Font("/usr/share/fonts/noto/NotoColorEmoji.ttf", 48)
    elif os.name == "nt":  # Windows
        emoji_font = pygame.font.SysFont("segoeuiemoji", 18)
    else:
        raise Exception("Unsupported platform for emoji rendering")

    next_text = heading_font.render("NEXT", True, (255, 255, 255))
    hold_text = heading_font.render("HOLD", True, (255, 255, 255))

    score_text = in_game_font.render(f"SCORE: {score}", True, (255, 255, 255))
    lines_text = in_game_font.render(f"LINES: {lines}", True, (255, 255, 255))
    mode_text = in_game_font.render(f"MODE: {mode}", True, (255, 255, 255))

    gestures_text = heading_font.render("GESTURES:", True, (255, 255, 255))
    right_text = in_game_font.render("RIGHT: ", True, (255, 255, 255))
    left_text = in_game_font.render("LEFT: ", True, (255, 255, 255))
    rotate_right_text = in_game_font.render("ROTATE RIGHT: ", True, (255, 255, 255))
    rotate_left_text = in_game_font.render("ROTATE LEFT: ", True, (255, 255, 255))
    hold_swap_text = in_game_font.render("HOLD/SWAP: ", True, (255, 255, 255))
    drop_text = in_game_font.render("DROP: ", True, (255, 255, 255))

    # Load images
    victory_hand = pygame.image.load("images/victory_hand.png")
    scaled_victory_hand = pygame.transform.scale(victory_hand, (25, 25))

    point_hand = pygame.image.load("images/point_hand.png")
    scaled_point_hand = pygame.transform.scale(point_hand, (25, 25))

    thumbs_up = pygame.image.load("images/thumbs_up.png")
    scaled_thumbs_up = pygame.transform.scale(thumbs_up, (25, 25))

    thumbs_down = pygame.image.load("images/thumbs_down.png")
    scaled_thumbs_down = pygame.transform.scale(thumbs_down, (25, 25))

    open_palm = pygame.image.load("images/open_palm.png")
    scaled_open_palm = pygame.transform.scale(open_palm, (25, 25))

    i_love_you = pygame.image.load("images/i_love_you.png")
    scaled_i_love_you = pygame.transform.scale(i_love_you, (25, 25))

    # Board + Boxes (tetris grid 20x10)
    game_board = Box(settings.GAME_WIDTH + 25, settings.GAME_HEIGHT + 25, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)
    next_box = Box(settings.GAME_PIXEL_SIZE * 6, settings.GAME_PIXEL_SIZE * 7, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)
    hold_box = Box(settings.GAME_PIXEL_SIZE * 6, settings.GAME_PIXEL_SIZE * 6, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)
    stats_box = Box(settings.GAME_PIXEL_SIZE * 9, settings.GAME_PIXEL_SIZE * 6, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)
    gestures_box = Box(settings.GAME_PIXEL_SIZE * 9, settings.GAME_PIXEL_SIZE * 12, settings.BOX_FILL_COLOUR, settings.BOX_LINE_WIDTH, settings.BOX_LINE_COLOUR)

    staticBlocks = list()

    # Tetris pieces
    current_piece = Mino_J()
    current_piece.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)
    current_piece.setActivePiece()
    next_piece = pickPiece()
    next_piece.setXY(0,0)

    # MAIN GAME LOOP
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        settings.display_surface.fill('black')

        # Display board + boxes
        game_board.blit(settings.WINDOW_WIDTH/2 - settings.GAME_WIDTH/2 - settings.BOX_LINE_WIDTH, settings.WINDOW_HEIGHT/2 - settings.GAME_HEIGHT/2 - settings.BOX_LINE_WIDTH)
        next_box.blit(settings.NEXT_BOX_X, settings.NEXT_BOX_Y)
        hold_box.blit(settings.HOLD_BOX_X, settings.HOLD_BOX_Y)
        stats_box.blit(settings.STATS_BOX_X, settings.STATS_BOX_Y)
        gestures_box.blit(settings.GESTURES_BOX_X, settings.GESTURES_BOX_Y)

        # Display Text
        settings.display_surface.blit(next_text, (settings.NEXT_BOX_X + (settings.GAME_PIXEL_SIZE * 2), settings.NEXT_BOX_Y + (settings.GAME_PIXEL_SIZE * .5)))
        settings.display_surface.blit(hold_text, (settings.HOLD_BOX_X + (settings.GAME_PIXEL_SIZE * 1.9), settings.HOLD_BOX_Y + (settings.GAME_PIXEL_SIZE * .5)))

        score_text = in_game_font.render(f"SCORE: {score}", True, (255, 255, 255))
        lines_text = in_game_font.render(f"LINES: {lines}", True, (255, 255, 255))
        settings.display_surface.blit(score_text, (settings.STATS_BOX_X + (settings.GAME_PIXEL_SIZE * .75), settings.STATS_BOX_Y + (settings.GAME_PIXEL_SIZE * .5)))
        settings.display_surface.blit(lines_text, (settings.STATS_BOX_X + (settings.GAME_PIXEL_SIZE * .75), settings.STATS_BOX_Y + (settings.GAME_PIXEL_SIZE * 2.5)))
        settings.display_surface.blit(mode_text, (settings.STATS_BOX_X + (settings.GAME_PIXEL_SIZE * .75), settings.STATS_BOX_Y + (settings.GAME_PIXEL_SIZE * 4.5)))

        settings.display_surface.blit(gestures_text, (settings.GESTURES_BOX_X + (settings.GAME_PIXEL_SIZE * 2.5), settings.GESTURES_BOX_Y + (settings.GAME_PIXEL_SIZE * .5)))
        settings.display_surface.blit(right_text, (settings.INDIV_GESTURES_TEXT_X, settings.RIGHT_TEXT_Y))
        settings.display_surface.blit(left_text, (settings.INDIV_GESTURES_TEXT_X, settings.LEFT_TEXT_Y))
        settings.display_surface.blit(rotate_right_text, (settings.INDIV_GESTURES_TEXT_X, settings.ROTATE_RIGHT_TEXT_Y))
        settings.display_surface.blit(rotate_left_text, (settings.INDIV_GESTURES_TEXT_X, settings.ROTATE_LEFT_TEXT_Y))
        settings.display_surface.blit(hold_swap_text, (settings.INDIV_GESTURES_TEXT_X, settings.HOLD_SWAP_TEXT_Y))
        settings.display_surface.blit(drop_text, (settings.INDIV_GESTURES_TEXT_X, settings.DROP_TEXT_Y))

        # Display images for gestures
        settings.display_surface.blit(scaled_victory_hand, (settings.INDIV_GESTURES_TEXT_X + (settings.GAME_PIXEL_SIZE * 2.75), settings.RIGHT_TEXT_Y))
        settings.display_surface.blit(scaled_point_hand, (settings.INDIV_GESTURES_TEXT_X + (settings.GAME_PIXEL_SIZE * 2.55), settings.LEFT_TEXT_Y))
        settings.display_surface.blit(scaled_thumbs_up, (settings.INDIV_GESTURES_TEXT_X + (settings.GAME_PIXEL_SIZE * 6), settings.ROTATE_RIGHT_TEXT_Y))
        settings.display_surface.blit(scaled_thumbs_down, (settings.INDIV_GESTURES_TEXT_X + (settings.GAME_PIXEL_SIZE * 5.75), settings.ROTATE_LEFT_TEXT_Y))
        settings.display_surface.blit(scaled_open_palm, (settings.INDIV_GESTURES_TEXT_X + (settings.GAME_PIXEL_SIZE * 4.5), settings.HOLD_SWAP_TEXT_Y))
        settings.display_surface.blit(scaled_i_love_you, (settings.INDIV_GESTURES_TEXT_X + (settings.GAME_PIXEL_SIZE * 2.5), settings.DROP_TEXT_Y))

        for i in settings.staticBlocks:
            i.blit()
        current_piece.blit()
        next_piece.blitNext()
        if settings.hold:
            settings.hold.blitHold()
        
        pygame.display.update()
        current_piece.update()
        if current_piece.hold:
            if settings.hold is None:
                settings.hold = current_piece
                current_piece = next_piece
                current_piece.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)
                current_piece.setActivePiece()
                next_piece = pickPiece()
                next_piece.setXY(0,0)
            else:
                temp = current_piece
                current_piece = settings.hold
                settings.hold = temp
                current_piece.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)
                current_piece.auto_drop_counter = 0
                current_piece.hold = False
            
        if not current_piece.active:
            settings.held = False
            for i in current_piece.b:
                settings.staticBlocks.append(i)
            current_piece = next_piece
            current_piece.setXY(settings.START_LOCATION_X, settings.START_LOCATION_Y)
            current_piece.setActivePiece()
            next_piece = pickPiece()
            next_piece.setXY(0,0)
            lines, score = checkLineClear(lines, score)
        settings.KEYHANDLER.update()

    pygame.quit()
    sys.exit()

def main():

    curr_state = settings.GameState.MAIN_MENU

    # TODO: add state for pause screen
    while True:
        if curr_state == settings.GameState.MAIN_MENU:
            curr_state = displayMenu(curr_state)
        elif curr_state == settings.GameState.INSTRUCTIONS_1:
            curr_state = displayInstructionsPage1(curr_state)
        elif curr_state == settings.GameState.INSTRUCTIONS_2:
            curr_state = displayInstructionsPage2(curr_state)
        elif curr_state == settings.GameState.SINGLEPLAYER or curr_state == settings.GameState.MULTIPLAYER:
            curr_state = runGame(curr_state)
        elif curr_state == settings.GameState.QUIT:
            break
        
    # Close the window
    pygame.quit()

main()

