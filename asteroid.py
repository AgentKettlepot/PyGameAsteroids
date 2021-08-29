import pygame
# generate random integer values
from random import seed
from random import randint

class asteroid (object):
    def __init__ (self, x, y, height, width, health, vel):
        self.x= x
        self.y=y
        self.vel = vel
        self.height= height
        self.width= width
        self.health = health

    def GenerateRandomPos(self, screen_width, asteroid_collection, score):
        x_pos = randint(0, screen_width)
        y_pos = randint (-20, 5)
        counter=1
        vel = -2
        if score > 300 and counter==1:
            counter+=1
            vel -=1
            if score > 500 and counter==2:
                counter+=1
                vel -=2
        NewAsteroid = asteroid (x_pos, y_pos, 36, 36, counter, vel)
        asteroid_collection.append(NewAsteroid)
        x_pos=0

    def draw(self, win, asteroid):
        pygame.draw.circle(win, (0,0,0), (asteroid.x,asteroid.y), asteroid.width//2, 10)
        pygame.draw.circle(win, (255,255,255), (asteroid.x,asteroid.y), 6)

    def move(self):
        self.y -=self.vel
