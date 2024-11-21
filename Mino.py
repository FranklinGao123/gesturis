import pygame
from Block import Block
import settings

class Mino:
    b = [None]*4
    tempB = [None]*4
    auto_drop_counter = 0
    direction = 1
    left, right, bottom = False, False, False
    active = True

    def create(self, c):
        self.b[0] = Block(c)
        self.b[1] = Block(c)
        self.b[2] = Block(c)
        self.b[3] = Block(c)
        self.tempB[0] = Block(c)
        self.tempB[1] = Block(c)
        self.tempB[2] = Block(c)
        self.tempB[3] = Block(c)

    def getDirection1():
        pass

    def getDirection2():
        pass

    def getDirection3():
        pass

    def getDirection4():
        pass

    def checkMovementCollision(self):
        self.left, self.right, self.bottom = False, False, False

        for i in self.b:
            if i.x == 0:
                self.left = True

        for i in self.b:
            if i.x == settings.GAME_PIXEL_SIZE * 10:
                self.right = True
        
        for i in self.b:
            if i.y == settings.GAME_PIXEL_SIZE * 20:
                self.bottom = True

    def checkRotationCollision(self):
        for i in self.tempB:
            if i.x < 0:
                return True

        for i in self.tempB:
            if i.x > settings.GAME_PIXEL_SIZE * 10:
                return True
        
        for i in self.tempB:
            if i.y > settings.GAME_PIXEL_SIZE * 20:
                return True

    def setXY():
        pass

    def updateXY(self, direction):
        if not self.checkRotationCollision():
            self.direction = direction
            self.b[0].x = self.tempB[0].x
            self.b[0].y = self.tempB[0].y
            self.b[1].x = self.tempB[1].x
            self.b[1].y = self.tempB[1].y
            self.b[2].x = self.tempB[2].x
            self.b[2].y = self.tempB[2].y
            self.b[3].x = self.tempB[3].x
            self.b[3].y = self.tempB[3].y

    def update(self):
        self.auto_drop_counter += 1
        if settings.KEYHANDLER.check_key(pygame.K_UP):
            options = {
                1: self.getDirection2,
                2: self.getDirection3,
                3: self.getDirection4,
                4: self.getDirection1
            }
            options[self.direction]()

        self.checkMovementCollision()

        if not self.left and settings.KEYHANDLER.check_key(pygame.K_LEFT):
            self.b[0].x -= settings.GAME_PIXEL_SIZE
            self.b[1].x -= settings.GAME_PIXEL_SIZE
            self.b[2].x -= settings.GAME_PIXEL_SIZE
            self.b[3].x -= settings.GAME_PIXEL_SIZE 

        if not self.right and settings.KEYHANDLER.check_key(pygame.K_RIGHT):
            self.b[0].x += settings.GAME_PIXEL_SIZE
            self.b[1].x += settings.GAME_PIXEL_SIZE
            self.b[2].x += settings.GAME_PIXEL_SIZE
            self.b[3].x += settings.GAME_PIXEL_SIZE 

        if not self.bottom and (self.auto_drop_counter >= settings.DROP_INTERVAL or settings.KEYHANDLER.check_key(pygame.K_DOWN)):
            self.b[0].y += settings.GAME_PIXEL_SIZE
            self.b[1].y += settings.GAME_PIXEL_SIZE
            self.b[2].y += settings.GAME_PIXEL_SIZE
            self.b[3].y += settings.GAME_PIXEL_SIZE
            self.auto_drop_counter = 0
        elif self.bottom:
            active = False

    def bilt(self):
        for i in self.b:
            i.bilt()