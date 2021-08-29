import pygame
from asteroid import *
from spaceship import *
from bullet import *
from health_boost import *
pygame.init()
screen_width = 800
screen_height = 600
win = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Space Game")
bg = pygame.image.load('G:\VSCode Transfer\Space Game\SpaceBackground1.jpg')
bgX = 0
bgX2 = bg.get_width()
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont('comicsans', 30, True, True)
bulletSound = pygame.mixer.Sound('G:\VSCode Transfer\Space Game\Game_bullet.mp3')
hitSound = pygame.mixer.Sound('G:\VSCode Transfer\Space Game\Game_hit.mp3')
music = pygame.mixer.music.load('G:\VSCode Transfer\Space Game\music.mp3')
Game_Over_Sound = pygame.mixer.Sound('G:\VSCode Transfer\Space Game\mixkit-arcade-retro-game-over-213.wav')
pygame.mixer.music.play(-1)

def redrawGameWindow():
    win.blit(bg, (0, bgX))  # draws our first bg image
    win.blit(bg, (0, bgX2))
    score_text= font.render('Score: ' + str(score), 1, (255,255,255))
    win.blit(score_text, (350,10))
    spaceship.draw(win, player)
    for asteroid in asteroids:
        asteroid.draw(win, asteroid) 
    for bullet in bullets:
        bullet.draw(win)
    for healthboosts in Health_Regens:
        healthboosts.draw(win)
    level_text = font.render('Level: ' + str(asteroid.health), 1, (0,0,0))
    win.blit(level_text, (10, 10))
    pygame.display.update()
    

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        Paused_Font = pygame.font.SysFont('comicsans', 30)
        Paused_Text = Paused_Font.render("Game Paused: Press 'c' to continue or 'q' to quit", 1, (255,0,0))
        win.blit(Paused_Text, (screen_width//2 - 250, screen_height//2))
        pygame.display.update()
        clock.tick(5)

def GameOver():
    Game_Over_Sound.play()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                
    Game_Over_Font = pygame.font.SysFont('comicsans', 30)
    Game_Over_Text = Game_Over_Font.render("Game Over: Press 'a' to play again and 'q' to quit", 1, (255,0,0))
    win.blit(Game_Over_Text, (250 - (Game_Over_Text.get_width()/2),200))
    pygame.display.update()
    clock.tick(5)

player = spaceship(250, 400, 60, 60)
asteroids = []
bullets= []
Health_Regens=[]
shootLoop=0
counter=0
for i in range(5): #creates 5 asteroids to start
    asteroid.GenerateRandomPos (screen_height, screen_width,asteroids, score) #creates 5 asteroids and initializes them into asteroids list
    health_boost.GenerateRandomLocs(screen_width, Health_Regens)

running = True
while running:
    if player.health < 0:
        pygame.mixer.music.set_volume(0)
        GameOver()

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             quit()
    clock.tick(27)
    bgX -=1.4
    bgX2 -=1.4
    if bgX < bg.get_width() * -1:  # If our bg is at the -width then reset its position
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    #check collisions here:

    for asteroid in asteroids:
        if asteroid.y >screen_height: #if asteroid is not in frame anymore
            asteroids.pop(asteroids.index(asteroid))
            player.health -=1
            score -=5
            asteroid.GenerateRandomPos (screen_width,asteroids, score)
            font1 = pygame.font.SysFont('comicsans', 100)
            text= font1.render("-5", 1, (255,0,0))
            win.blit(text, (250 - (text.get_width()/2),200))
            pygame.display.update()
            i = 0
            while i<200:
                pygame.time.delay(3)
                i+=1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i=301
                        pygame.quit()
        if asteroid.health <=0: #if asteroid is destroyed by bullet, print dead and remove asteroid from screen
            score +=10
            asteroids.pop(asteroids.index(asteroid))
            asteroid.GenerateRandomPos (screen_width,asteroids, score)
        asteroid.move()
    if len(asteroids) < 5:
        asteroid.GenerateRandomPos (screen_width,asteroids, score)
    spaceship.Get_Hit_And_Lose_Health(asteroids, player, hitSound) #spaceship gets hit and will lose a health
    for SpaceBullet in bullets:
        for asteroid in asteroids:
            #pygame.draw.rect(win, (255,0,0), (asteroid.x - asteroid.width/2, asteroid.y - asteroid.height/2, asteroid.width, asteroid.height), 2)
            if SpaceBullet.y - SpaceBullet.radius < asteroid.y + asteroid.width and SpaceBullet.y + SpaceBullet.radius > asteroid.y:
                if SpaceBullet.x + SpaceBullet.radius > asteroid.x - asteroid.width/2 and SpaceBullet.x - SpaceBullet.radius < asteroid.x + asteroid.width/2:
                    score +=1
                    asteroid.health -=1
                    try:
                        bullets.pop(bullets.index(SpaceBullet))
                    except Exception:
                        print("IGNOREEE")

        if SpaceBullet.y < screen_height and SpaceBullet.y > 0:
            SpaceBullet.move()
        elif bullet not in bullets:
            try:
                bullets.pop(bullets.index(SpaceBullet)) #removes bullet if it is off the screen 
            except Exception:
                print("IGNORE") 
    for healthboosts in Health_Regens:
        if healthboosts.y >screen_height: #if asteroid is not in frame anymore
            Health_Regens.pop(Health_Regens.index(healthboosts))
            health_boost.GenerateRandomLocs(screen_width,Health_Regens)
            pygame.display.update()
        if player.y < healthboosts.y + healthboosts.height/2 + 5 and player.y > healthboosts.y - healthboosts.height/2 - 5:
            if player.x> healthboosts.x - healthboosts.width/2 - 5 and player.x < healthboosts.x + healthboosts.width/2 + 5:
                player.health +=0.5
                pygame.display.update()
                Health_Regens.pop(Health_Regens.index(healthboosts))
                health_boost.GenerateRandomLocs(screen_width,Health_Regens)
        healthboosts.move()
    #firing bullets
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    try:
        keys = pygame.key.get_pressed()
    except KeyError:
        pass
    if keys[pygame.K_SPACE] and shootLoop==0:
        if len(bullets) <=5:
            bulletSound.play()
            NewBullet = bullet(round(player.x), round(player.y) - 20)
            bullets.append(NewBullet)
        shootLoop=1
    if keys[pygame.K_p]:
        pause()
    spaceship.Move(keys, player, screen_width) #spaceship moving
    #----------------------------------------------------
    pygame.display.update()
    redrawGameWindow()

pygame.quit()