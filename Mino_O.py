import settings
from Mino import Mino

class Mino_O(Mino):
    def __init__(self):
        super().create('yellow2')
    
    def setXY(self, x ,y):
        # o o
        # o o
        # 
        self.b[0].x = x
        self.b[0].y = y
        self.b[1].x = x
        self.b[1].y = y - settings.GAME_PIXEL_SIZE
        self.b[2].x = x + settings.GAME_PIXEL_SIZE
        self.b[2].y = y - settings.GAME_PIXEL_SIZE
        self.b[3].x = x + settings.GAME_PIXEL_SIZE
        self.b[3].y = y