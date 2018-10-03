if __name__ == "__main__":
    import pygame
    from game import *

    pygame.init()   

    DBZ = Game()
    DBZ.run() #GAME LOOP

    pygame.quit()