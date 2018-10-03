
import pygame
from settings import *

pygame.init()

# Game options and settings
TITLE = "Dodge Ball Z"
FONTSIZE = int(RATIO[0] / 17)
buttonSize = ()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

# Fonts/Font Surface
pressStartFont = pygame.font.Font("../assets/Fonts/DodgeBallzFont.ttf", FONTSIZE)
gameFont = pygame.font.Font("../assets/Fonts/DodgeBallzFont.ttf", FONTSIZE//2)

# Images
titleScreenBackGround = pygame.image.load("../assets/DBZ_GUIArt/DBZ_Press Start/StartMenu_Background.png")
mainMenuScreenBackGround = pygame.image.load("../assets/DBZ_GUIArt/DBZ_Main Menu/MainMenu_Background.png")
localMenuScreenBackGround = pygame.image.load("../assets/DBZ_GUIArt/DBZ_Options/OptionsMenu_Background.png")
spaceLevelImage = pygame.image.load("../assets/Level Art/Space.png")
mountainLevelImage = pygame.image.load("../assets/Level Art/Mountain.png")
plainsLevelImage = pygame.image.load("../assets/Level Art/Plains.png")
