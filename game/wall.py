#class for a wall that reflects a ball contacting it
from settings import *
import pygame

WALLRADIUS = 8

class Wall(object):
    def __init__(self,x1,y1,x2,y2):
        """initialize a wall object as a line between the two given points."""
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.radius = WALLRADIUS

    def draw(self,surface):
        """draw a line representing the wall, with circles for the endpoint"""
        pygame.draw.circle(surface,(255,0,0),(self.x1,self.y1),self.radius,0)
        pygame.draw.circle(surface, (255,0,0), (self.x2, self.y2), self.radius, 0)
        pygame.draw.line(surface,(255,0,0),(self.x1,self.y1),(self.x2,self.y2),self.radius*2)

#class for the walls at the edge of the map
class BorderWall(Wall):
    def __init__(self,x1,y1,x2,y2):
        super().__init__(x1,y1,x2,y2)
        self.radius = 0


def generateBorderWalls(screen_width,screen_height):
    """Generates walls around the edges of the field"""
    LEFT = 0
    RIGHT = screen_width
    TOP = 0
    BOTTOM = screen_height
    walls = []
    walls.append(BorderWall(LEFT, TOP, RIGHT, TOP)) #top
    walls.append(BorderWall(RIGHT, TOP, RIGHT, BOTTOM)) #right
    walls.append(BorderWall(LEFT, TOP, LEFT, BOTTOM)) #left
    walls.append(BorderWall(LEFT, BOTTOM, RIGHT, BOTTOM)) #bottom
    return walls
