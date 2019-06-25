"""
Global constants
"""
import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BACKGROUND = (76, 90, 142)

# Screen dimensions
img = pygame.image.load("res/images/greek_background.jpg")
SCREEN_HEIGHT = img.get_rect().height
SCREEN_WIDTH = (800 * SCREEN_HEIGHT) // 600
