import pygame
import settings

class Key_Handler:
    prev = []
    cur = []
    counter = 0

    def __init__(self):
        self.cur = pygame.key.get_pressed()
        self.prev = self.cur
    
    def check_key(self, key):
        self.cur = pygame.key.get_pressed()
        if self.cur[key] == 1 and self.prev[key] == 0:
            self.prev = self.cur
            return 1
        elif self.cur[key] == 1 and self.prev[key] == 1:
            if self.counter == settings.INPUT_INTERVAL:
                self.counter = 0
                return 1
            else:
                return 0

    def check_up(self):
        self.cur = pygame.key.get_pressed()
        if self.cur[pygame.K_UP] == 1 and self.prev[pygame.K_UP] == 0:
            self.prev = self.cur
            return 1
        return 0

    def check_space(self):
        self.cur = pygame.key.get_pressed()
        if self.cur[pygame.K_SPACE] == 1 and self.prev[pygame.K_SPACE] == 0:
            self.prev = self.cur
            return 1
        return 0
    
    def check_hold(self):
        self.cur = pygame.key.get_pressed()
        if self.cur[pygame.K_c] == 1 and self.prev[pygame.K_c] == 0:
            self.prev = self.cur
            return 1
        return 0
            
    def update(self):
        self.counter += 1
        if self.counter > settings.INPUT_INTERVAL:
            self.counter = 0
        self.prev = self.cur
