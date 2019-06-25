"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import MainEngine.constants as constants

from MainEngine.platforms import MovingPlatform
from MainEngine.spritesheet_functions import SpriteSheet


class Medusa(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.atacking_frames_l = []
        self.atacking_frames_r = []
        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("res/images/medusa.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(5, 93, 56, 74, constants.WHITE)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(70, 93, 56, 74, constants.WHITE)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(199, 93, 56, 74, constants.WHITE)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(261, 93, 56, 74, constants.WHITE)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(321, 93, 56, 74, constants.WHITE)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(384, 91, 56, 74, constants.WHITE)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(448, 91, 56, 74, constants.WHITE)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.

        image = sprite_sheet.get_image(5, 93, 56, 74, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(70, 93, 56, 74, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(199, 93, 56, 74, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(261, 93, 56, 74, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(321, 93, 56, 74, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(384, 91, 56, 74, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(448, 91, 56, 74, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Attack
        image = sprite_sheet.get_image(7, 478, 61, 70, constants.WHITE)
        self.atacking_frames_r.append(image)
        image = sprite_sheet.get_image(97, 478, 67, 70, constants.WHITE)
        self.atacking_frames_r.append(image)
        image = sprite_sheet.get_image(198, 478, 73, 70, constants.WHITE)
        self.atacking_frames_r.append(image)
        image = sprite_sheet.get_image(310, 478, 73, 70, constants.WHITE)
        self.atacking_frames_r.append(image)
        image = sprite_sheet.get_image(415, 478, 82, 70, constants.WHITE)
        self.atacking_frames_r.append(image)
        image = sprite_sheet.get_image(527, 478, 98, 70, constants.WHITE)
        self.atacking_frames_r.append(image)
        image = sprite_sheet.get_image(649, 478, 98, 70, constants.WHITE)
        self.atacking_frames_r.append(image)
        image = sprite_sheet.get_image(770, 478, 97, 70, constants.WHITE)
        self.atacking_frames_r.append(image)
        image = sprite_sheet.get_image(888, 478, 97, 70, constants.WHITE)
        self.atacking_frames_r.append(image)

        image = sprite_sheet.get_image(7, 478, 61, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)
        image = sprite_sheet.get_image(97, 478, 67, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)
        image = sprite_sheet.get_image(198, 478, 73, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)
        image = sprite_sheet.get_image(310, 478, 73, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)
        image = sprite_sheet.get_image(415, 478, 82, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)
        image = sprite_sheet.get_image(527, 478, 98, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)
        image = sprite_sheet.get_image(649, 478, 98, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)
        image = sprite_sheet.get_image(770, 478, 97, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)
        image = sprite_sheet.get_image(888, 478, 97, 70, constants.WHITE)
        image = pygame.transform.flip(image, True, False)
        self.atacking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def medusaAI(self):
        dir = self.level.player.rect.x - self.rect.x
        if dir > 50:
            self.change_x = 1
            if dir > 0:
                self.direction = 'R'
            else:
                self.direction = 'L'
        elif dir < -50:
            self.change_x = -1
            if dir < 0:
                self.direction = 'L'
            else:
                self.direction = 'R'
        else:
            self.change_x = 0
            self.change_y = 0
            if len(self.direction) == 2:
                self.direction = self.direction[0]

        again_looked = False
        if self.level.dir_before_medusa_look is not 'N':
            if self.level.player.direction is not self.level.dir_before_medusa_look:
                again_looked = True
                self.level.dir_before_medusa_look= self.level.player.direction

        # check if attack or not
        if self.rect.y - (self.level.player.rect.height + self.level.player.rect.y - self.rect.height) is 0 and \
                self.direction[0] is not self.level.player.direction[0] and again_looked or self.level.dir_before_medusa_look is "N":
            self.level.lives -= 1
            self.level.dir_before_medusa_look = self.level.player.direction[0]
            print(self.level.dir_before_medusa_look)
            if dir > 0:
                self.direction = "RA"
            else:
                self.direction = "LA"

    def update(self):
        """ Move the player. """
        self.medusaAI()
        # Gravity
        self.calc_grav()
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "RA":
            frame = (pos // 30) % len(self.atacking_frames_r)
            self.image = self.atacking_frames_r[frame]
        elif self.direction == "LA":
            frame = (pos // 30) % len(self.atacking_frames_l)
            self.image = self.atacking_frames_l[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0
