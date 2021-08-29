import pygame
from random import seed
from random import randint

class health_boost(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.health = 5

    def draw(self, win):
        pygame.draw.circle(win, (255,255,255), (self.x,self.y), self.width)

    def move(self):
        self.y += self.vel

    def GenerateRandomLocs(screen_width, boost_collection):
        x_pos = randint(0, screen_width)
        y_pos = randint (-20, 5)
        NewBoost = health_boost(x_pos, y_pos, 8, 8)
        boost_collection.append(NewBoost)
        x_pos=0