# Button class to create our on-screen buttons
from globals import *
import pygame



class Button(pygame.sprite.Sprite):
    """Allows for the creation of buttons. Give the class its parameters and make a button
    that is any color, size, font and position"""
    def __init__(self, w, h, label="Button", color=RED):
        super().__init__()
        self.image1 = pygame.image.load("../assets/DBZ_GUIArt/DBZ_Main Menu/Buttons/DBZ_ButtonNormal.png")
        self.image2 = pygame.image.load("../assets/DBZ_GUIArt/DBZ_Main Menu/Buttons/DBZ_ButtonHover.png")
        self.label = label
        self.color = color
        self.image = self.image1
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.labelSurf = gameFont.render(self.label, \
                                         True, \
                                         WHITE)

        self.labelSize = gameFont.size(self.label)
        self.offset = ((w - self.labelSize[0])//2, (h - self.labelSize[1])//2)
        self.image.blit(self.labelSurf, self.offset)
        self.w = w
        self.h = h

    def onClick(self):
        """Return a message"""
        return self.label

    def onHover(self):
        """Highlight our button"""
        self.image = self.image2
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.image.blit(self.labelSurf, self.offset)

    def draw(self):
        """Draw Default button"""
        self.image = self.image1
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.image.blit(self.labelSurf, self.offset)

    def setPos(self, pos):
        """Set the center pos of the button"""
        self.rect.center = pos



