
# Libraries
import pygame
import sys

# Settings

# Initializing PyGame
pygame.init()

# ===== Button ===== #
class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def __draw__(self, frame):
        pygame.draw.rect(frame, (0, 255, 0), self.rect)

# ===== Menu ===== #
class MenuScreen:
    def __init__(self, frame, gameScreen):
        # Settings
        self.frame = frame
        self.gameButton = Button(100, 100, 100, 100)
        self.gameScreen = gameScreen
        self.quitButton = Button(500, 100, 100, 100)
        self.flag = True
        

    def __update__(self):
        if self.gameButton.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.flag = False
            self.gameScreen.flag = True
        elif self.quitButton.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.flag = False
            self.gameScreen.flag = True
            

    def __draw__(self):
        self.frame.fill((0, 0, 255))
        self.gameButton.__draw__(self.frame)
        self.quitButton.__draw__(self.frame)

# Quit
pygame.quit()
