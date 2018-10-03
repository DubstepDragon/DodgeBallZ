#runs a bouncing ball prototype

import pygame
import random
from ball import *
from wall import *
from settings import *

if __name__ == "__main__": #prevent code from executing if not being directly ran

    pygame.init()
    surface = pygame.display.set_mode((800,600))
    ball = Ball(400,300)
    #creates a random motion for the ball
    ball.motion = Vector2(random.uniform(-10,10),random.uniform(-10,10))
    #generates four walls around the border
    walls = generateBorderWalls()
    #generate walls for testing
    #walls.append(Wall(500,100,500,500))
    walls.append(Wall(500,300,700,500))
    walls.append(Wall(500,100,500,300))
    FPSclock = pygame.time.Clock()

    while True:
        FPSclock.tick(60)
        pygame.event.pump()
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_ESCAPE]: #exit prototype
            break
        if keysPressed[pygame.K_SPACE]: #respawn ball
            ball = Ball(400,300)
            ball.motion = Vector2(random.uniform(-10, 10), random.uniform(-10, 10))

        pygame.draw.rect(surface,(0,0,0),(0,0,800,600),0)
        ball.move(walls)
        ball.draw(surface)
        for wall in walls:
            wall.draw(surface)
        pygame.display.update()

    pygame.display.quit()
