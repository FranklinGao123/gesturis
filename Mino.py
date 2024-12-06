import pygame
from Block import Block
import settings

class Mino:
    auto_drop_counter = 0

    def create(self, c):
        self.left, self.right, self.bottom = False, False, False
        self.active = False
        self.b = list()
        self.tempB = list()
        self.direction = 1
        self.hold = False
        for i in range(4):
            self.b.append(Block(c))
            self.tempB.append(Block(c))
    
    def setActivePiece(self):
        self.active = True

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
            if i.x <= 0:
                self.left = True
        
        for j in settings.staticBlocks:
            for i in self.b:
                if i.x == j.x + settings.GAME_PIXEL_SIZE and i.y == j.y:
                    self.left = True

        for i in self.b:
            if i.x >= settings.GAME_PIXEL_SIZE * 9:
                self.right = True

        for j in settings.staticBlocks:
            for i in self.b:
                if i.x == j.x - settings.GAME_PIXEL_SIZE and i.y == j.y:
                    self.right = True
        
        for i in self.b:
            if i.y >= settings.GAME_PIXEL_SIZE * 19:
                self.bottom = True
        
        for j in settings.staticBlocks:
            for i in self.b:
                if i.y == j.y - settings.GAME_PIXEL_SIZE and i.x == j.x:
                    self.bottom = True

    def cannotRotate(self):
        for i in self.tempB:
            if i.x < 0:
                return True

        for i in self.tempB:
            if i.x > settings.GAME_PIXEL_SIZE * 9:
                return True
        
        for i in self.tempB:
            if i.y > settings.GAME_PIXEL_SIZE * 19:
                return True

        for j in settings.staticBlocks:
            for i in self.tempB:
                if i.y == j.y and i.x == j.x:
                    return True

    def setXY():
        pass

    def updateXY(self, direction):
        if not self.cannotRotate():
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
        if settings.KEYHANDLER.check_input(['Thumb_Up']):
            options = {
                1: self.getDirection2,
                2: self.getDirection3,
                3: self.getDirection4,
                4: self.getDirection1
            }
            options[self.direction]()

        self.checkMovementCollision()

        if not self.left and settings.KEYHANDLER.check_input(['Pointing_Up']):
            self.b[0].x -= settings.GAME_PIXEL_SIZE
            self.b[1].x -= settings.GAME_PIXEL_SIZE
            self.b[2].x -= settings.GAME_PIXEL_SIZE
            self.b[3].x -= settings.GAME_PIXEL_SIZE

        if not self.right and settings.KEYHANDLER.check_input(['Victory']):
            self.b[0].x += settings.GAME_PIXEL_SIZE
            self.b[1].x += settings.GAME_PIXEL_SIZE
            self.b[2].x += settings.GAME_PIXEL_SIZE
            self.b[3].x += settings.GAME_PIXEL_SIZE 

        if not self.bottom and (self.auto_drop_counter >= settings.DROP_INTERVAL or settings.KEYHANDLER.check_input(['Closed_Fist'])):
            self.b[0].y += settings.GAME_PIXEL_SIZE
            self.b[1].y += settings.GAME_PIXEL_SIZE
            self.b[2].y += settings.GAME_PIXEL_SIZE
            self.b[3].y += settings.GAME_PIXEL_SIZE
            self.auto_drop_counter = 0
        elif self.bottom:
            if self.auto_drop_counter >= settings.DROP_INTERVAL:
                self.active = False

        if settings.KEYHANDLER.check_input(['Closed_Fist']):
            while not self.bottom:
                self.b[0].y += settings.GAME_PIXEL_SIZE
                self.b[1].y += settings.GAME_PIXEL_SIZE
                self.b[2].y += settings.GAME_PIXEL_SIZE
                self.b[3].y += settings.GAME_PIXEL_SIZE
                self.checkMovementCollision()
            self.active = False
        
        if settings.KEYHANDLER.check_input(['ILoveYou']):
            if not settings.held:
                self.hold = True
                settings.held = True


    def blit(self):
        for i in self.b:
            i.blit()
    
    def blitNext(self):
        for i in self.b:
            i.blitNext()

    def blitHold(self):
        for i in self.b:
            i.blitHold()
