import pygame
class spaceship(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.vel = 10
        self.width = width
        self.height = height
        self.lives = 5
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 20
        self.canFire=True


    def draw(win, spaceship):
        #make drawing later
        #image = pygame.image.load(r'G:\VSCode Transfer\Space Game\output-onlinejpgtools.jpg').convert_alpha()
        #image = pygame.transform.scale(image, (spaceship.height, spaceship.width)) 
        #win.blit(image, (spaceship.x, spaceship.y))
        pygame.draw.circle(win, (0,0,0), (spaceship.x,spaceship.y), 10)
        pygame.draw.rect(win, (255,0,0), (spaceship.hitbox[0]-20, spaceship.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0,128,0), (spaceship.hitbox[0]-20, spaceship.hitbox[1] - 20, 50 - (5 * (10 - spaceship.health)), 10))
        spaceship.hitbox = (spaceship.x + 20, spaceship.y, 28, 60)

    def Move( keys, user, screen_width):
        if keys[pygame.K_LEFT] and user.x > user.vel:
            user.x -=user.vel
        elif keys[pygame.K_RIGHT] and user.x + user.vel < screen_width:
            user.x +=user.vel

    def Get_Hit_And_Lose_Health (asteroids, ship, sound):
        health = ship.lives
        for asteroid in asteroids:
            if health > 0:
                if ship.y < asteroid.y + asteroid.height and ship.y + ship.height > asteroid.y:
                    if ship.x + ship.width > asteroid.x and ship.x < asteroid.x + asteroid.width:
                        sound.play()
                        asteroids.pop(asteroids.index(asteroid))
                        ship.health -=2
            else:
                pass

            