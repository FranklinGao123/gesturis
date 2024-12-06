import pygame
from Recognizer_Task import Recognizer_Task

class Key_Handler:
    prev = []
    cur = []
    counter = 0
    recog = Recognizer_Task()

    def __init__(self):
        # self.cur = pygame.key.get_pressed()
        self.cur = self.recog.recognition()
        self.prev = self.cur
    
    def check_input(self, gesture):
        # self.cur = pygame.key.get_pressed()
        self.cur = self.recog.recognition()
        if self.cur == gesture and self.prev != gesture:
            self.prev = self.cur
            return 1
        elif self.cur == gesture and self.prev == gesture:
            if self.counter == 100:
                self.counter = 0
                return 1
            else:
                return 0
            
    def update(self):
        self.counter += 1
        if self.counter > 100:
            self.counter = 0
        self.prev = self.cur
"""
    def check_up(self):
        # self.cur = pygame.key.get_pressed()
        self.cur = gesture_input_handler.needed_result
        if self.cur[pygame.K_UP] == 1 and self.prev[pygame.K_UP] == 0:
            self.prev = self.cur
            return 1
        return 0

    def check_space(self):
        # self.cur = pygame.key.get_pressed()
        self.cur = gesture_input_handler.needed_result
        if self.cur[pygame.K_SPACE] == 1 and self.prev[pygame.K_SPACE] == 0:
            self.prev = self.cur
            return 1
        return 0
    
    def check_hold(self):
        # self.cur = pygame.key.get_pressed()
        self.cur = gesture_input_handler.needed_result
        if self.cur[pygame.K_c] == 1 and self.prev[pygame.K_c] == 0:
            self.prev = self.cur
            return 1
        return 0
"""  
          
    
