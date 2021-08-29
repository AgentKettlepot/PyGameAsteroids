import pygame
class bullet (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 8
        self.radius = 4

    def draw(self, win):
        pygame.draw.circle(win, (255,0,0), (self.x,self.y), self.radius)

    def move(self):
        self.y -=self.vel