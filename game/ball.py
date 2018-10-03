#class for a bouncing dodgeball

from vector import *
import pygame
import math

BALLRADIUS = 16
ACCEL_FACTOR = 0

class Ball(object):
    def __init__(self,x,y):
        """initialize a ball object with default values"""
        self.x = x
        self.y = y
        self.radius = BALLRADIUS
        self.motion = Vector2(0,0)

    def draw(self, surface):
        """basic draw method for the ball"""
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius, 0)
    def move(self,walls):
        """moves the ball, and checks for any collisions with the given walls."""
        #checks for a collision at newX and newY before moving there
        newX = self.x + self.motion.x
        newY = self.y + self.motion.y
        collisionDetected = False
        #vline = ((self.x,self.y),(newX,newY)) #velocity line, the line between first point and second points
        for wall in walls: #check for intersecting with each wall
            #wline = ((wall.x1,wall.y1),(wall.x2,wall.y2)) #convert the wall into a line
            #calculate distance between endpoint of ball and the closeset point of the line
            distance = (abs((wall.y2-wall.y1)*newX - (wall.x2-wall.x1)*newY + wall.x2*wall.y1 - wall.y2*wall.x1)
                /((wall.y2-wall.y1)**2 + (wall.x2-wall.x1)**2)**0.5)
            if distance < self.radius + wall.radius-2: #determine if ball has collided
                #check collision between ball and line corners
                wallLength = ((wall.x2-wall.x1)**2 + (wall.y2-wall.y1)**2)**0.5
                if ((newX - wall.x1) ** 2 + (newY - wall.y1) ** 2) ** 0.5 < self.radius + wall.radius-2:
                    collisionDetected = True
                    angle = math.atan2(self.y - wall.y1, self.x - wall.x1)
                    self.bounce(angle, True)
                elif ((newX- wall.x2) ** 2 + (newY - wall.y2) ** 2) ** 0.5 < self.radius + wall.radius-2:
                    collisionDetected = True
                    angle = math.atan2(self.y - wall.y2, self.x - wall.x2)
                    self.bounce(angle, True)
                #check whether the ball is colliding within the line bounds
                elif ((newX-wall.x1)**2 + (newY-wall.y1)**2)**0.5 < wallLength+self.radius-2 \
                        and ((newX-wall.x2)**2 + (newY-wall.y2)**2)**0.5 < wallLength+self.radius-2:
                    collisionDetected = True
                    angle = math.atan2(wall.y2-wall.y1,wall.x2-wall.x1)
                    self.bounce(angle)
            if collisionDetected: #only collide with one wall per frame
                break
        if not collisionDetected:
            self.x = newX
            self.y = newY
        else: #accelerate the ball after each collision
            self.motion = self.motion.normalized * (self.motion.magnitude+ACCEL_FACTOR)

    def bounce(self,angle,normal=False):
        """reflects the ball. If normal=false, angle should be perpendicular, if normal=true, angle should be parallel."""
        #get normal angle
        direction = self.motion.radians
        collisionAngle = direction-angle
        if normal:
            normalAngle = angle
        elif collisionAngle > 0:
            normalAngle = angle - math.pi/2
        else:
            normalAngle = angle + math.pi/2
        normalVector = polar_to_vector2(normalAngle,1)
        #uses vector reflection formula
        self.motion = -2 * (self.motion.Dot(normalVector)) * normalVector + self.motion