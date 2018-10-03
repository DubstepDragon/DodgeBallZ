"""
import pygame
from vector import *
#press w to move forward in mouse pos direction
#press space to create ball

class player:
    def __init__(self):
        self.pos = Vector2(400, 300)
        self.rad = 20
        self.area = None
        self.dir = None
        self.Ball = []
        self.caught = 0
    def update(self, dt, w, h):
        x, y = pygame.mouse.get_pos()
        mpos = Vector2(x, y)
        self.dir = (mpos - self.pos).normalized
        for b in self.Ball:
            b.update(dt, w, h)
            a = self.pos.x - b.pos.x
            c = self.pos.y - b.pos.y
            d = (a **2 + c **2) ** .5
            if d < self.rad + b.rad - 5:
                self.Ball.remove(b)
    def catch(self, dt, w, h):
        for b in self.Ball:
            b.update(dt, w, h)
            a = self.pos.x - b.pos.x
            c = self.pos.y - b.pos.y
            d = (a **2 + c **2) ** .5
            if d < self.rad + b.rad + 5:
                self.Ball.remove(b)
                self.caught += 1
            #e = self.pos - b.pos 
            #if Vector.Dot(e, e) < (self.pos + b.pos) * (self.pos + b.pos):
                #self.Ball.remove(b)
                #self.caught += 1
    def throw(self):
        pos = self.pos + (self.rad+5) * self.dir
        vel = self.dir * 600
        self.Ball.append(ball(vel, pos))
    def move(self, dt):
        self.pos += 5 * self.dir
    def draw(self, surf, font1):
        for b in self.Ball:
            b.draw(surf)
        pygame.draw.circle(surf, (255, 0, 0), self.pos.i, self.rad)
        catches = font1.render("Catches:" + str(self.caught), True, (255, 255, 255))
        surf.blit(catches, (0,0))
class ball:
    def __init__(self, vel, pos):
        self.pos = pos
        self.rad = 10
        self.area = None
        self.vel = vel
    def update(self, dt, screen_w, screen_h):
        self.pos += self.vel *dt
        if self.pos.x < self.rad or self.pos.x > screen_w - self.rad:
            self.vel.x = -self.vel.x
        if self.pos.y < self.rad or self.pos.y > screen_h - self.rad:
            self.vel.y = -self.vel.y 
    def draw(self, surf):
        pygame.draw.circle(surf, (0, 255, 0), self.pos.i, self.rad)

pygame.font.init()
pygame.display.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
P = player()
#B = ball()
done = False
width = 800
height = 600
catch_cooldown = 0.0
font1 = pygame.font.SysFont('Courier New', 20)
while not done:
    dt = clock.tick(60) / 1000.0
    catch_cooldown += dt
    
    event = pygame.event.poll()
    if event.type ==pygame.QUIT:
        done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            P.throw()
        if event.key == pygame.K_e and catch_cooldown >= 1.0:
            P.catch(dt, width, height)
            catch_cooldown = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True
    if keys[pygame.K_w]:
        P.move(dt)
    P.update(dt, width, height)
    #B.update(dt)

    screen.fill((0, 0, 0))
    P.draw(screen, font1)
    #B.draw(screen)
    pygame.display.flip()

pygame.display.quit()
"""