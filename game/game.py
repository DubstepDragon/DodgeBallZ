import pygame
import random
from globals import *
from buttons import *
from ball import *
from wall import *
from controller_commands import *
from player import *


def blit_center(screen, source_surface, pos_x, pos_y):
    """Makes an offset blit position that allows for any surface to have a center point at
    half its width and height"""
    screen.blit(source_surface, (pos_x - source_surface.get_width() / 2, pos_y - source_surface.get_height() / 2))


class Game(object):
    def __init__(self):
        """Sets up our game"""
        pygame.display.init()
        pygame.display.set_caption(TITLE)
        self.fullscreen = FULLSCREEN
        if self.fullscreen:
            self.screen = pygame.display.set_mode(RATIO, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(RATIO)
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(FPS) / 1000
        self.running = False
        self.modeNum = 0
        self.mode = None
        self.bgImage = None
        self.level = "None"
        self.levelImage = None
        self.levelImageRight = None
        self.levelImageLeft = None
        self.music = pygame.mixer.music.load("../assets/Game Moosic/Title_final.mp3")
        self.allControllers = Controller()
        self.player_ids = []
        self.player = []
        self.spriteGroup = []
        for i in self.allControllers.get_id:
            self.player_ids.append(self.allControllers.get_id[i])
            self.spriteGroup.append(Player(self, self.player_ids[i]))
        for i in self.player_ids:
            if self.allControllers.play_connected:
                self.player.append(Playstation_Controller(self.player_ids[i]))
            if self.allControllers.xbox_connected:
                self.player.append(Xbox_Controller(self.player_ids[i]))
        self.ballList = []
        self.ballList.append(Ball(WIDTH/2,HEIGHT/2))
        self.walls = generateBorderWalls(WIDTH,HEIGHT)
        self.titleSettings()
        self.mainMenuSettings()
        self.localMenuSettings()
        self.optionsMenuSettings()
        self.levelMenuSettings()
        self.changeMode("Title")

        # Set up all modes/menus

    # Settings

    def titleSettings(self):
        self.num_count = .1
        pygame.mixer.music.set_volume(self.num_count)
        self.bgImage = titleScreenBackGround
        self.bgImage = pygame.transform.scale(self.bgImage, (RATIO[0], RATIO[1]))
        self.mouseClick = None
        self.count = 0

    def mainMenuSettings(self):
        self.mouseClick = None
        self.buttonPress = None
        self.buttonCount = 0
        mainMenuList = ["Solo", "Local", "Online", "Options", "Exit"]
        buttonSize = (int((WIDTH // (WIDTH // (WIDTH * 0.15)))), int((HEIGHT // (HEIGHT // (HEIGHT * 0.09)))))
        self.mainMenuGroup = pygame.sprite.Group()

        i = len(self.mainMenuGroup.sprites())
        for item in mainMenuList:
            btn = Button(*buttonSize, item, RED)
            x = int(WIDTH * 3/5)
            y = HEIGHT * 0.16 + (buttonSize[1] + HEIGHT * 0.03) * (i + .90)
            btn.setPos((x, y))
            self.mainMenuGroup.add(btn)
            i = len(self.mainMenuGroup.sprites())
            print()

    def localMenuSettings(self):
        self.mouseClick = None
        localMenuList = ["Back", "Level", "Start"]
        buttonSize = (int((WIDTH // (WIDTH // (WIDTH * 0.15)))), int((HEIGHT // (HEIGHT // (HEIGHT * 0.09)))))
        self.localMenuGroup = pygame.sprite.Group()

        i = len(self.localMenuGroup.sprites())
        for item in localMenuList:
            btn = Button(*buttonSize, item, RED)
            x = WIDTH / 4 + (WIDTH / 4 * i)
            y = int(HEIGHT - buttonSize[1])
            btn.setPos((x, y))
            self.localMenuGroup.add(btn)
            i = len(self.localMenuGroup.sprites())

    def optionsMenuSettings(self):
        self.mouseClick = None
        optionsMenuList = ["Back", "Volume", "Resolution"]
        buttonSize = (int((WIDTH // (WIDTH // (WIDTH * 0.15)))), int((HEIGHT // (HEIGHT // (HEIGHT * 0.09)))))
        self.optionsMenuGroup = pygame.sprite.Group()

        i = len(self.optionsMenuGroup.sprites())
        for item in optionsMenuList:
            btn = Button(*buttonSize, item, RED)
            x = WIDTH / 4 + (WIDTH / 4 * i)
            y = int(HEIGHT - buttonSize[1])
            btn.setPos((x, y))
            self.optionsMenuGroup.add(btn)
            i = len(self.optionsMenuGroup.sprites())

    def levelMenuSettings(self):
        self.mouseClick = None
        levelMenuList = ["Left", "Select", "Right"]
        buttonSize = (int((WIDTH // (WIDTH // (WIDTH * 0.15)))), int((HEIGHT // (HEIGHT // (HEIGHT * 0.09)))))
        self.levelList = ["None", "Space", "Mountain", "Plains"]
        self.levelCount = 0
        self.levelMenuGroup = pygame.sprite.Group()
        self.playerGroup = pygame.sprite.Group()

        i = len(self.levelMenuGroup.sprites())
        for item in levelMenuList:
            btn = Button(*buttonSize, item, RED)
            x = WIDTH / 4 + (WIDTH / 4 * i)
            y = int(HEIGHT - buttonSize[1])
            btn.setPos((x, y))
            self.levelMenuGroup.add(btn)
            i = len(self.levelMenuGroup.sprites())

    # Runs the program

    def run(self):
        """Runs our game"""
        self.running = True
        while self.running:
            if self.mode == "Exit":
                self.running = False
            self.dt = self.clock.tick(FPS) / 1000
            self.clock.tick(FPS)
            self.input()
            self.update()
            self.draw()
            pygame.display.update()

    # Calls the updates

    def update(self):
        """Updates the vars"""
        pass

    def titleUpdate(self):
        """Update the title screen"""
        for i in range(8):
            self.num_count += .05 * self.dt
            pygame.mixer.music.set_volume(self.num_count)
        self.count += .03
        if self.count > 1:
            self.count = 0

    def mainMenuUpdate(self):
        """Update the MainMenu screen"""
        self.bgImage = mainMenuScreenBackGround
        self.bgImage = pygame.transform.scale(self.bgImage, (RATIO[0], RATIO[1]))

        if self.buttonCount < 1:
            self.buttonCount = 5
        elif self.buttonCount > 5:
            self.buttonCount = 1

        self.count += .05
        if self.count > 1:
            self.count = 0

    def localMenuUpdate(self):
        """Update the Local Menu screen"""
        self.bgImage = localMenuScreenBackGround
        self.bgImage = pygame.transform.scale(self.bgImage, (RATIO[0], RATIO[1]))

        if self.level == "Space":
            self.levelImage = spaceLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH//5, HEIGHT//4))

        elif self.level == "Mountain":
            self.levelImage = mountainLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH // 5, HEIGHT // 4))

        elif self.level == "Plains":
            self.levelImage = plainsLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH // 5, HEIGHT // 4))

        else:
            self.levelImage = pygame.Surface((WIDTH//5, HEIGHT//4))

        self.count += .05
        if self.count > 1:
            self.count = 0

    def optionsMenuUpdate(self):
        self.bgImage = localMenuScreenBackGround
        self.bgImage = pygame.transform.scale(self.bgImage, (RATIO[0], RATIO[1]))

    def levelMenuUpdate(self):
        """Update the Level Menu screen"""
        self.level = self.levelList[self.levelCount]

        if self.level == "Space":
            self.levelImage = spaceLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH // 2, HEIGHT // 2))
            self.levelImageRight = mountainLevelImage
            self.levelImageRight = pygame.transform.scale(self.levelImageRight, (WIDTH // 7, HEIGHT // 2))
            self.levelImageLeft = pygame.Surface((WIDTH // 7, HEIGHT // 2))

        elif self.level == "Mountain":
            self.levelImage = mountainLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH // 2, HEIGHT // 2))
            self.levelImageRight = plainsLevelImage
            self.levelImageRight = pygame.transform.scale(self.levelImageRight, (WIDTH // 7, HEIGHT // 2))
            self.levelImageLeft = spaceLevelImage
            self.levelImageLeft = pygame.transform.scale(self.levelImageLeft, (WIDTH // 7, HEIGHT // 2))

        elif self.level == "Plains":
            self.levelImage = plainsLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH // 2, HEIGHT // 2))
            self.levelImageRight = pygame.Surface((WIDTH // 7, HEIGHT // 2))
            self.levelImageLeft = mountainLevelImage
            self.levelImageLeft = pygame.transform.scale(self.levelImageLeft, (WIDTH // 7, HEIGHT // 2))

        else:
            self.levelImage = pygame.Surface((WIDTH // 2, HEIGHT // 2))
            self.levelImageRight = spaceLevelImage
            self.levelImageRight = pygame.transform.scale(self.levelImageRight, (WIDTH // 7, HEIGHT // 2))
            self.levelImageLeft = plainsLevelImage
            self.levelImageLeft = pygame.transform.scale(self.levelImageLeft, (WIDTH // 7, HEIGHT // 2))

    def gameMenuUpdate(self):
        """Update the Level Menu screen"""
        self.level = self.levelList[self.levelCount]

        if self.level == "Space":
            self.levelImage = spaceLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH, HEIGHT))

        elif self.level == "Mountain":
            self.levelImage = mountainLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH, HEIGHT))

        elif self.level == "Plains":
            self.levelImage = plainsLevelImage
            self.levelImage = pygame.transform.scale(self.levelImage, (WIDTH, HEIGHT))

        else:
            self.levelImage = pygame.Surface((WIDTH, HEIGHT))
            self.levelImageRight = spaceLevelImage

        for sprite in self.spriteGroup:
            sprite.updatePlayer(self.ballList)

        # for ball in self.ballList:
        #     ball.move(self.walls)

    # Gets the inputs

    def input(self):
        """Process Input"""
        pass

    def titleInput(self):
        """Process the Title input"""
        # keyboard input
        eventList = pygame.event.get()
        keys = pygame.key.get_pressed()

        for j in self.player:
            if isinstance(j, Xbox_Controller):
                if j.button_START == 1:
                    self.changeMode("MainMenu")

            if isinstance(j, Playstation_Controller):
                if j.button_OPTIONS == 1:
                    self.changeMode("MainMenu")

        for event in eventList:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_RETURN:
                    self.changeMode("MainMenu")

                if event.key == pygame.K_f and keys[pygame.K_LALT]:
                    self.toggleFullscreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.changeMode("MainMenu")

    def mainMenuInput(self):
        """Process the Main Menu input"""
        # keyboard input
        keys = pygame.key.get_pressed()
        self.mouseClick = 0
        eventList = pygame.event.get()
        if len(self.player) != 0:
            for j in self.player:
                if isinstance(j, Xbox_Controller):
                    if j.button_A == 1:
                        self.buttonPress = True

                    if j.axis_LEFT_STICK[1] > 0.5:
                        self.buttonCount -= 1

                    if j.axis_LEFT_STICK[1] < -0.5:
                        self.buttonCount += 1

                if isinstance(j, Playstation_Controller):
                    if j.button_X == 1:
                        self.buttonPress = True

        for event in eventList:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_f and keys[pygame.K_LALT]:
                    self.toggleFullscreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseClick = event.button

    def localMenuInput(self):
        """Process the Local Menu input"""
        # keyboard input
        keys = pygame.key.get_pressed()
        self.mouseClick = 0
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_f and keys[pygame.K_LALT]:
                    self.toggleFullscreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseClick = event.button

    def optionsMenuInput(self):
        """Process the Options Menu input"""
        # keyboard input
        keys = pygame.key.get_pressed()
        self.mouseClick = 0
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_f and keys[pygame.K_LALT]:
                    self.toggleFullscreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseClick = event.button

    def levelMenuInput(self):
        """Process the Level Menu input"""
        # keyboard input
        keys = pygame.key.get_pressed()
        self.mouseClick = 0
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_f and keys[pygame.K_LALT]:
                    self.toggleFullscreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseClick = event.button

    def gameMenuInput(self):
        """Process the Level Menu input"""
        # keyboard input
        keys = pygame.key.get_pressed()
        self.mouseClick = 0
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_f and keys[pygame.K_LALT]:
                    self.toggleFullscreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseClick = event.button

        for sprite in self.spriteGroup:
            for player in self.player:
                self.ballList = sprite.input(self.ballList, player.get_id)


    # Draws the modes

    def drawTitle(self):
        """Draws the title/splash screen"""
        blit_center(self.screen, self.bgImage, RATIO[0] / 2, RATIO[1] / 2)

        if self.count < 0.5:
            tempFontColor = RED
        else:
            tempFontColor = BLUE

        blit_center(self.screen, pressStartFont.render("PRESS START", True, tempFontColor), RATIO[0]/2, RATIO[1] - RATIO[1]/5)

    def drawMainMenu(self):
        """Draw the mode selection screen"""
        blit_center(self.screen, self.bgImage, RATIO[0] / 2, RATIO[1] / 2)
        mousePos = pygame.mouse.get_pos()

        for btn in self.mainMenuGroup:
            if btn.rect.collidepoint(mousePos):
                btn.onHover()

                if self.mouseClick == 1:
                    self.changeMode(btn.onClick())

                elif self.buttonPress:
                    self.changeMode(btn.onClick())

            else:
                btn.draw()

            self.mainMenuGroup.draw(self.screen)

    def drawOptionsMenu(self):
        """Draw the options menu for adjusting certain aspects
        to the players perspective"""
        blit_center(self.screen, self.bgImage, RATIO[0] / 2, RATIO[1] / 2)
        mousePos = pygame.mouse.get_pos()

        for btn in self.optionsMenuGroup:
            if btn.rect.collidepoint(mousePos):
                btn.onHover()

                if self.mouseClick == 1:
                    self.changeMode(btn.onClick)

                if self.mouseClick == 1 and btn.label == "Back":
                    self.changeMode("MainMenu")

            else:
                btn.draw()

            self.optionsMenuGroup.draw(self.screen)

    def drawSoloMenu(self):
        """Draw the options menu for AI purposes"""
        pass

    def drawLocalMenu(self):
        """Draws the local screen menu for local purposes"""
        blit_center(self.screen, self.bgImage, RATIO[0] / 2, RATIO[1] / 2)
        mousePos = pygame.mouse.get_pos()
        for btn in self.localMenuGroup:
            if btn.rect.collidepoint(mousePos):
                btn.onHover()

                if self.mouseClick == 1 and btn.label == "Back":
                    self.changeMode("MainMenu")

                elif self.mouseClick == 1:
                    self.changeMode(btn.onClick())
            else:
                btn.draw()

            # Level Selection
            self.screen.blit(self.levelImage, (WIDTH / 5 * 2, HEIGHT / 5 * 3))

            pygame.draw.rect(self.screen, WHITE, (WIDTH / 5 * 2, HEIGHT / 5 * 3, WIDTH / 5, HEIGHT / 4), int(WIDTH * 0.0026))

            blit_center(self.screen, gameFont.render(self.level, True, WHITE), WIDTH / 2,
                        HEIGHT * 0.57)

            # Player Join

            # P1
            pygame.draw.rect(self.screen, WHITE, (WIDTH / 8, HEIGHT / 10, WIDTH / 9 * 2, HEIGHT / 10 * 3), int(WIDTH * 0.0026))
            if len(self.player) >= 1:
                blit_center(self.screen, gameFont.render("Player One", True, WHITE), WIDTH / 4,
                            HEIGHT / 12)

            # P2
            pygame.draw.rect(self.screen, WHITE, (WIDTH / 8, HEIGHT / 10 * 5, WIDTH / 9 * 2, HEIGHT / 10 * 3), int(WIDTH * 0.0026))
            if len(self.player) >= 2:
                blit_center(self.screen, gameFont.render("Player Two", True, WHITE), WIDTH / 4,
                            HEIGHT / 12 * 5.75)

            # P3
            pygame.draw.rect(self.screen, WHITE, (WIDTH / 8 * 7, HEIGHT / 10, -WIDTH / 9 * 2, HEIGHT / 10 * 3), int(WIDTH * 0.0026))
            if len(self.player) >= 3:
                blit_center(self.screen, gameFont.render("Player Three", True, WHITE), WIDTH / 4 * 3,
                            HEIGHT / 12)

            # P4
            pygame.draw.rect(self.screen, WHITE, (WIDTH / 8 * 7, HEIGHT / 10 * 5, -WIDTH / 9 * 2, HEIGHT / 10 * 3), int(WIDTH * 0.0026))
            if len(self.player) == 4:
                blit_center(self.screen, gameFont.render("Player Four", True, WHITE), WIDTH / 4 * 3,
                            HEIGHT / 12 * 5.75)

            # Buttons
            self.localMenuGroup.draw(self.screen)

    def drawOnlineMenu(self):
        """Draws the online screen menu for network purposes"""
        pass

    def drawLevelMenu(self):
        """Draws the level selection menu"""
        blit_center(self.screen, self.bgImage, RATIO[0] / 2, RATIO[1] / 2)

        mousePos = pygame.mouse.get_pos()

        for btn in self.levelMenuGroup:
            if btn.rect.collidepoint(mousePos):
                btn.onHover()

                if self.mouseClick == 1 and btn.label == "Left":
                    self.levelCount -= 1
                    if self.levelCount < 0:
                        self.levelCount = 3

                elif self.mouseClick == 1 and btn.label == "Right":
                    self.levelCount += 1
                    if self.levelCount > 3:
                        self.levelCount = 0

                elif self.mouseClick == 1 and btn.label == "Select":
                    self.changeMode("Local")

            else:
                btn.draw()

            self.screen.blit(self.levelImage, (WIDTH / 4, HEIGHT / 4))
            pygame.draw.rect(self.screen, WHITE, (WIDTH / 4, HEIGHT / 4, WIDTH / 2, HEIGHT / 2), int(WIDTH * 0.0026))
            blit_center(self.screen, pressStartFont.render(self.level, True, WHITE), WIDTH / 2,
                        HEIGHT / 7)
            self.screen.blit(self.levelImageLeft, (WIDTH / 14, HEIGHT / 4))
            self.screen.blit(self.levelImageRight, (WIDTH / 14 * 11, HEIGHT / 4))
            pygame.draw.rect(self.screen, WHITE, (WIDTH / 14, HEIGHT / 4, WIDTH / 7, HEIGHT / 2), int(WIDTH * 0.0026))
            pygame.draw.rect(self.screen, WHITE, (WIDTH / 14 * 11, HEIGHT / 4, WIDTH / 7, HEIGHT / 2), int(WIDTH * 0.0026))

            self.levelMenuGroup.draw(self.screen)

    def drawGameMenu(self):
        """Draws the main game"""
        blit_center(self.screen, self.levelImage, RATIO[0] / 2, RATIO[1] / 2)
        for sprite in self.spriteGroup:
            sprite.drawPlayer(self.screen)

        # for ball in self.ballList:
        #     ball.draw(self.screen)

        for wall in self.walls:
            wall.draw(self.screen)

    def drawContinueMenu(self):
        """Draws the continuing menu for either
        selecting a new level, choosing a new mode,
        or exit the game entirely"""
        pass

    def drawCreditsMenu(self):
        """Draw the ending screen and show the credits"""
        self.running = False

    def draw(self):
        """Draws the game scene"""
        pass

        # Changes the mode

    def changeMode(self, mode):
        self.buttonPress = False

        if mode != self.mode:
            self.mode = mode
        else:
            return

        if self.mode == "Title":
            pygame.mixer.music.play(-1)
            self.input = self.titleInput
            self.update = self.titleUpdate
            self.draw = self.drawTitle

        elif self.mode == "MainMenu":
            self.input = self.mainMenuInput
            self.update = self.mainMenuUpdate
            self.draw = self.drawMainMenu

        elif self.mode == "Local":
            self.input = self.localMenuInput
            self.update = self.localMenuUpdate
            self.draw = self.drawLocalMenu

        elif self.mode == "Options":
            self.input = self.optionsMenuInput
            self.update = self.optionsMenuUpdate
            self.draw = self.drawOptionsMenu

        elif self.mode == "Level":
            self.input = self.levelMenuInput
            self.update = self.levelMenuUpdate
            self.draw = self.drawLevelMenu

        elif self.mode == "Start":
            if self.level == "None":
                self.changeMode("Local")

            else:
                pygame.mixer.stop()
                self.input = self.gameMenuInput
                self.update = self.gameMenuUpdate
                self.draw = self.drawGameMenu

        elif self.mode == "Exit":
            self.running = False

    def toggleFullscreen(self):
        if not self.fullscreen:
            self.screen = pygame.display.set_mode(RATIO, pygame.FULLSCREEN)
            self.fullscreen = 1
        else:
            self.screen = pygame.display.set_mode(RATIO)
            self.fullscreen = 0


