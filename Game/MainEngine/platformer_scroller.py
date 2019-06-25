"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller example.

From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

import MainEngine.constants as constants
import MainEngine.levels as levels

from MainEngine.player import Player
from MainEngine.medusa import Medusa


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    # Create the player
    medusa = Medusa()
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    # level_list.append(levels.Level_01(player))
    # level_list.append(levels.Level_02(player))
    level_list[0].medusa = Medusa()

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    medusa.level = current_level
    medusa.rect.x = 310
    medusa.rect.y = constants.SCREEN_HEIGHT - medusa.rect.height

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    active_sprite_list.add(medusa)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    num_frame = 0
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_k:
                    if player.direction == "R":
                        player.attack_right()
                    else:
                        player.attack_left()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        # print("extra"+str(-current_level.world_shift-constants.SCREEN_WIDTH))
        if player.rect.right >= 500 and -current_level.world_shift - constants.SCREEN_WIDTH < 0:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)


        # If the player gets near the left side, shift the world right (+x)
        elif player.rect.left <= 120 and current_level.world_shift < 0:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # print(str(-current_level.world_shift))
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        # print(str(current_position) + " ")
        '''
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        '''
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        num_frame += 1
        if num_frame % 60 == 0:
            print(str(num_frame // 60))

        current_level.draw(screen)
        active_sprite_list.draw(screen)
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        red_heart = pygame.image.load("res/images/red_heart.png").convert()
        red_heart.set_colorkey((0, 0, 0))
        gray_heart = pygame.image.load("res/images/gray_heart.png").convert()
        gray_heart.set_colorkey((0, 0, 0))
        next_x_pos_heart = constants.SCREEN_WIDTH - red_heart.get_width()
        for i in range(player.level.lives):
            screen.blit(red_heart, (next_x_pos_heart, red_heart.get_height()))
            next_x_pos_heart -= red_heart.get_width()

        num_gray = 3 - player.level.lives
        if num_gray>3:
            num_gray = 3
        if num_gray > 0:
            for i in range(num_gray):
                screen.blit(gray_heart, (next_x_pos_heart, gray_heart.get_height()))
                next_x_pos_heart -= gray_heart.get_width()

        if player.level.lives <= 0:
            textsurface = myfont.render('You died :(', False, (0, 0, 0))
            screen.blit(textsurface, (constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2))

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
