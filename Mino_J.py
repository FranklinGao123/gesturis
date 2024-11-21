import settings
from Mino import Mino

class Mino_J(Mino):
    def __init__(self):
        super().create("#0072B2")
    
    def setXY(self, x ,y):
        # o
        # o o o
        self.b[0].x = x
        self.b[0].y = y
        self.b[1].x = x - settings.GAME_PIXEL_SIZE
        self.b[1].y = y - settings.GAME_PIXEL_SIZE
        self.b[2].x = x - settings.GAME_PIXEL_SIZE
        self.b[2].y = y
        self.b[3].x = x + settings.GAME_PIXEL_SIZE
        self.b[3].y = y

    def getDirection1(self):
        # o
        # o o o
        self.tempB[0].x = self.b[0].x
        self.tempB[0].y = self.b[0].y
        self.tempB[1].x = self.b[0].x - settings.GAME_PIXEL_SIZE
        self.tempB[1].y = self.b[0].y - settings.GAME_PIXEL_SIZE
        self.tempB[2].x = self.b[0].x - settings.GAME_PIXEL_SIZE
        self.tempB[2].y = self.b[0].y
        self.tempB[3].x = self.b[0].x + settings.GAME_PIXEL_SIZE
        self.tempB[3].y = self.b[0].y

        super().updateXY(1)

    def getDirection2(self):
        # o o
        # o 
        # o
        self.tempB[0].x = self.b[0].x
        self.tempB[0].y = self.b[0].y
        self.tempB[1].x = self.b[0].x + settings.GAME_PIXEL_SIZE
        self.tempB[1].y = self.b[0].y - settings.GAME_PIXEL_SIZE
        self.tempB[2].x = self.b[0].x 
        self.tempB[2].y = self.b[0].y - settings.GAME_PIXEL_SIZE
        self.tempB[3].x = self.b[0].x
        self.tempB[3].y = self.b[0].y + settings.GAME_PIXEL_SIZE 

        super().updateXY(2)

    def getDirection3(self):
        # o o o
        #     o
        self.tempB[0].x = self.b[0].x
        self.tempB[0].y = self.b[0].y
        self.tempB[1].x = self.b[0].x + settings.GAME_PIXEL_SIZE
        self.tempB[1].y = self.b[0].y + settings.GAME_PIXEL_SIZE
        self.tempB[2].x = self.b[0].x + settings.GAME_PIXEL_SIZE
        self.tempB[2].y = self.b[0].y
        self.tempB[3].x = self.b[0].x - settings.GAME_PIXEL_SIZE
        self.tempB[3].y = self.b[0].y

        super().updateXY(3)

    def getDirection4(self):
        #   o
        #   o
        # o o
        self.tempB[0].x = self.b[0].x
        self.tempB[0].y = self.b[0].y
        self.tempB[1].x = self.b[0].x - settings.GAME_PIXEL_SIZE
        self.tempB[1].y = self.b[0].y + settings.GAME_PIXEL_SIZE
        self.tempB[2].x = self.b[0].x 
        self.tempB[2].y = self.b[0].y + settings.GAME_PIXEL_SIZE
        self.tempB[3].x = self.b[0].x
        self.tempB[3].y = self.b[0].y - settings.GAME_PIXEL_SIZE

        super().updateXY(4)