import pygame

pygame.init()

# Game options and settings
WIDTH = 1000
HEIGHT = 800
RATIO = (WIDTH, HEIGHT)
FPS = 60
FULLSCREEN = 0

#player values
PLAYER_ACC = 1
PLAYER_FRICTION = 0.95
PLAYER_SIZE = (20)
PLAYER_COLOR = (0, 255, 0)
PLAYER_TURNSPD = 4
PLAYER_START_ANGLE = 90
THROW_VEL = 2
BGCOLOR = (0, 0, 0)



def blit_center(screen, source_surface, pos_x, pos_y):
    """Makes an offset blit position that allows for any surface to have a center point at
    half its width and height"""
    screen.blit(source_surface, (pos_x - source_surface.get_width() / 2, pos_y - source_surface.get_height() / 2))




