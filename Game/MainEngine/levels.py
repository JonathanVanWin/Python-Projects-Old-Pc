import pygame

import MainEngine.constants as constants
import MainEngine.platforms as platforms

from MainEngine.medusa import Medusa


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.lives = 4
        # initialize to "None"
        self.dir_before_medusa_look = 'N'
    # Update everything on this level

    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("res/images/greek_background.jpg").convert()
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.STONE_PLATFORM_BIG, 800, constants.SCREEN_HEIGHT - platforms.STONE_PLATFORM_BIG[3]]]
        num_middle_pil = 1
        temp = self.pillar(800 + platforms.STONE_PLATFORM_BIG[2] // 2, constants.SCREEN_HEIGHT - platforms.STONE_PLATFORM_BIG[3], num_middle_pil)
        for middle in temp:
            level.append(middle)
        self.medusa = Medusa()
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_SMALL)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

    def pillar(self, x_pos, y_pos, num_middle):
        y_pos -= platforms.GREEK_PILLAR_LOW[3]
        pillar = [[platforms.GREEK_PILLAR_LOW, x_pos, y_pos]]
        for i in range(num_middle):
            y_pos -= platforms.GREEK_PILLAR_MIDDLE[3]
            pillar.append([platforms.GREEK_PILLAR_MIDDLE, x_pos, y_pos])

        y_pos -= platforms.GREEK_PILLAR_HIGH[3]
        pillar.append([platforms.GREEK_PILLAR_HIGH, x_pos, y_pos])
        return pillar
