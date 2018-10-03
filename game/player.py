import pygame
import math
import random
from game import *
from vector import *
from ball import *
import controller_commands

pygame.init()


vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, cont_id):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((40, 40))
        self.image.fill(BGCOLOR)
        self.color = PLAYER_COLOR
        pygame.draw.circle(self.image,(self.color),(PLAYER_SIZE,PLAYER_SIZE),PLAYER_SIZE)
        self.Acceleration = 0
        self.Angle = PLAYER_START_ANGLE
        self.catchAngle = math.radians(90)
        self.catchRadius = 30
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(20, WIDTH - 20), random.randint(20, WIDTH - 20)]
        self.prevAngle = PLAYER_START_ANGLE
        self.cont_id = cont_id
        #if controller_commands.Xbox_Controller.NUMBUTTONS_xbox == 10:
        #self.XBOX = controller_commands.Xbox_Controller()
        #elif controller_commands.Playstation_Controller.NUMBUTTONS_playstation == 14:
        #self.PLAYSTATION = controller_commands.Playstation_Controller()
        self.posx = self.rect.center[0]
        self.posy = self.rect.center[1]
        self.ball = False
        self.hit = False

    def drawPlayer(self, screen):
        D = polar_to_vector2(math.radians(self.Angle), 1)
        n = PLAYER_SIZE + 20
        pygame.draw.circle(screen, (PLAYER_COLOR), (int(self.posx), int(self.posy)), PLAYER_SIZE)
        pygame.draw.line(screen, (255, 0, 0,), (self.posx, self.posy), (
        self.posx + ((PLAYER_SIZE - 2) * math.cos(math.radians(self.Angle))),
        self.posy - ((PLAYER_SIZE - 2) * math.sin(math.radians(self.Angle)))), 2)
        central_angle = D.radians_inv
        start_angle = central_angle - self.catchAngle
        end_angle = central_angle + self.catchAngle
        C = Vector2(self.posx, self.posy)
        pygame.draw.arc(screen, (255, 255, 255), (C.x - n, C.y - n, 2 * n, 2 * n),
                        start_angle, end_angle, 1)



    def updatePlayer(self, ballList):

        self.Acceleration *= PLAYER_FRICTION

        dx = self.Acceleration * math.cos(math.radians(self.Angle))
        dy = -1 * self.Acceleration * math.sin(math.radians(self.Angle))

        self.posx += dx
        self.posy += dy

        if self.posx < 0 + PLAYER_SIZE / 2:
            self.posx = 0 + PLAYER_SIZE / 2
        if self.posx > WIDTH - PLAYER_SIZE / 2:
            self.posx = WIDTH - PLAYER_SIZE / 2
        if self.posy < 0 + PLAYER_SIZE / 2:
            self.posy = 0 + PLAYER_SIZE / 2
        if self.posy > HEIGHT - PLAYER_SIZE / 2:
            self.posy = HEIGHT - PLAYER_SIZE / 2

        if self.Acceleration < 0.5 and self.Acceleration > -0.5:
            self.Acceleration = 0

        self.rect.center = [self.posx, self.posy]

        # for ball in ballList:
        #     distance = (((ball.x - self.posx) ** 2) + ((ball.y - self.posy) ** 2)) ** (1 / 2)
        #     if distance < PLAYER_SIZE+ball.radius:
        #         self.hit = True


    def catch(self, ball):
        Q = Vector2(ball.x, ball.y) - Vector2(self.posx, self.posy)
        D = polar_to_vector2(math.radians(self.Angle), 1)
        distance = (((ball.x - self.posx)**2) + ((ball.y - self.posy)**2))**(1/2)
        alpha = math.acos(dot(Q, D) / Q.magnitude)
        if alpha < self.catchAngle and distance <= self.catchRadius+PLAYER_SIZE+ball.radius and self.ball == False:
            self.ball = True
            return True

    def input(self, ballList, cont_id):
        pygame.event.pump()

        keys = pygame.key.get_pressed()
        (mouse_x, mouse_y) = pygame.mouse.get_pos()

        for player in self.game.player:
             if player.xbox_connected == True:
                 #joystick & trigger controller for xbox
                 if player.axis_TRIGGER_RIGHT > -0.01:
                     self.Acceleration -= PLAYER_ACC
                 if player.axis_TRIGGER_LEFT < 0.01:
                     self.Acceleration += PLAYER_ACC

                 dx = round(player.axis_LEFT_STICK[0], 2)
                 dy = round(-player.axis_LEFT_STICK[1], 2)


                 if abs(dx) == 0.0 and abs(dy) == 0.0:
                     self.Angle = self.prevAngle
                 else:
                     self.Angle = math.degrees(math.atan2(dy, dx))
                 self.prevAngle = self.Angle

             elif player.play_connected == True:
                 #joystick & trigger controller for playstation
                 if player.button_L2 == 1:
                     self.Acceleration += PLAYER_ACC
                 if player.button_R2 == 1:
                     self.Acceleration -= PLAYER_ACC

                 dx = round(player.axis_LEFT_STICK[0], 2)
                 dy = round(-player.axis_LEFT_STICK[1], 2)

                 print(self.Angle)

                 if abs(dx) == 0.0 and abs(dy) == 0.0:
                     self.Angle = self.prevAngle
                 else:
                     self.Angle = math.degrees(math.atan2(dy, dx))
                 self.prevAngle = self.Angle

             else:
                # key_board_controls

                if keys[pygame.K_w]:
                    self.Acceleration += PLAYER_ACC
                if keys[pygame.K_s]:
                    self.Acceleration -= PLAYER_ACC
                if keys[pygame.K_SPACE]:
                    for i in ballList:
                        if self.catch(i):
                            ballList.remove(i)
                if keys[pygame.K_e]:
                    result = self.throw()
                    if result != None:
                        ballList.append(result)

                dx = mouse_x - self.posx
                dy = mouse_y - self.posy
                self.Angle = math.degrees(math.atan2(-dy, dx))
                return ballList

    def throw(self):
        if self.ball:
            D = polar_to_vector2(math.radians(self.Angle), 1)
            Dn = D.normalized
            Ds = D * PLAYER_SIZE *2
            ball = Ball(Ds.x + self.posx, Ds.y + self.posy)
            ball.motion = Dn * 2
            self.ball = False
            return ball
        else:
            pass







