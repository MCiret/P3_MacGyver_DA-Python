import constantes as cste
import pygame
from pygame import *
pygame.init()


class View:
    """
    To display data (maze, texts) using pygame window.
    """
    @staticmethod
    def maze_display(maze_list, window):
        """
        Pygame displaying of maze.
        :param maze_list: (list) maze tiles (Tile subclasses)
        :param window: (pygame.Surface) main window.
        """
        assert (type(maze_list) is list
                and len(maze_list) == cste.NB_SPRITE_SIDE ** 2)
        assert(type(window) is pygame.Surface)

        x_sprite = 0
        y_sprite = 0
        for elem in maze_list:
            x_pos_pixel = x_sprite * cste.TAILLE_SPRITE
            y_pos_pixel = y_sprite * cste.TAILLE_SPRITE
            elem.draw_tile(window, x_pos_pixel, y_pos_pixel)
            x_sprite += 1
            if x_sprite == cste.NB_SPRITE_SIDE:
                x_sprite = 0
                y_sprite += 1
        pygame.display.flip()

    @staticmethod
    def display_text_below_maze(window, text, text_size=12):
        """
        To display texts under the maze surface.
        :param window: (pygame.Surface) main window.
        :param text: (str) text to display.
        :param text_size: (int)
        """
        assert(type(text) is str)
        assert(type(window) is pygame.Surface)

        text_font = pygame.font.SysFont("Calibri", text_size)
        text_rect = pygame.Rect(10, cste.MAZE_SIDE_SIZE + 25,
                                cste.MAZE_SIDE_SIZE,
                                cste.WINDOW_HEIGHT - cste.MAZE_SIDE_SIZE)

        # blit a black surface to erase previous text
        window.blit(pygame.Surface((cste.WINDOW_WIDTH,
                                    cste.WINDOW_HEIGHT - cste.MAZE_SIDE_SIZE)),
                                  (0, cste.MAZE_SIDE_SIZE))
        x, y = text_rect.topleft
        for line in text.splitlines():
            x, y = window.blit(text_font.render(line, True, (255, 255, 255)),
                               (x, y)).bottomleft

    @staticmethod
    def display_text_maze_right_side(window, text, text_size=12):
        """
        To display texts on right of the maze surface.
        :param window: (pygame.Surface) main window.
        :param text: (str) text to display.
        :param text_size: (int)
        """
        assert(type(text) is str)
        assert(type(window) is pygame.Surface)

        text_font = pygame.font.SysFont("Calibri", text_size)
        text_rect = pygame.Rect(cste.MAZE_SIDE_SIZE + 10,
                                cste.MAZE_SIDE_SIZE / 4,
                                cste.WINDOW_WIDTH - cste.MAZE_SIDE_SIZE,
                                cste.MAZE_SIDE_SIZE / 4)

        # blit a black surface to erase previous text
        window.blit(pygame.Surface((cste.WINDOW_WIDTH - cste.MAZE_SIDE_SIZE,
                                    cste.MAZE_SIDE_SIZE / 4)),
                                  (cste.MAZE_SIDE_SIZE + 10,
                                   cste.MAZE_SIDE_SIZE / 4))

        x, y = text_rect.topleft
        for line in text.splitlines():
            x, y = window.blit(text_font.render(line, True, (255, 255, 255)),
                               (x, y)).bottomleft

    @staticmethod
    def display_game_rules(window):
        """
        Displays the game rules under the maze.
        :param window: (pygame.Surface) main window.
        """
        assert (type(window) is pygame.Surface)

        rules_text = (f"Welcome !\nMac Gyver is lost in a maze... "
                      f"Could you help him to escape ?\n"
                      f"A guardian is watching over the maze exit...\n"
                      f"Look for items which could help Mac Gyver : "
                      f"Ether + Tube + (very discreet) Needle\n "
                      f"\n TO PLAY : Use directional keys to move "
                      f"MacGyver in the maze.\n")
        View.display_text_below_maze(window, rules_text)

    @staticmethod
    def impossible_move_msg(code, window):
        """
        Displays (under the maze) a text to explain to the user why he can't
        move to this direction.
        :param code: (int) Corresponding to the reason why the movement is
        impossible (1 = maze edge ; 2 = wall).
        :param window: (pygame.Surface) main window.
        """
        assert (type(code) is int and (code == 1 or code == 2))
        assert (type(window) is pygame.Surface)

        if code == 1:
            impos_mv_text = ("/!!!\\ You are going to fall out the maze... "
                             "teleporting is not possible /!!!\\\n"
                             "Please try a different direction...\n")
        elif code == 2:
            impos_mv_text = ("/!!!\\ You are going to bang into a wall... "
                             "and crossing walls is not possible /!!!\\\n"
                             "Please try a different direction...\n")
        View.display_text_below_maze(window, impos_mv_text)

    @staticmethod
    def display_items_counter(nb_items, window):
        """
        Displays (on the right) the number of items founded.
        :param nb_items: (int)
        :param window: (pygame.Surface) main window.
        """
        assert(type(nb_items) is int
               and nb_items in range(0, len(cste.ITEMS_CHAR_LIST) + 1))
        assert (type(window) is pygame.Surface)

        View.display_text_maze_right_side(window,
                                          f"Founded items :\n{nb_items} of 3.")

    @staticmethod
    def display_picture_maze_right_side(window, picture):
        """
        Displays (on the right) an anesthetic picture when all items
        has been founded.
        :param window: (pygame.Surface) main window.
        :param picture: (pygame.Surface) picture to blit to window.
        """
        assert (type(window) is pygame.Surface
                and type(picture) is pygame.Surface)

        window.blit(picture, (cste.MAZE_SIDE_SIZE + 25,
                              (cste.MAZE_SIDE_SIZE / 4) * 2))

    @staticmethod
    def end_of_game_msg(code, window):
        """
        Displays (under the maze) the game result (loose or win) text.
        :param code: (int) Corresponding to the game result
        (0 = loose ; 1 = win).
        :param window: (pygame.Surface) main window.
        """
        assert (type(code) is int and (code == 0 or code == 1))
        assert (type(window) is pygame.Surface)

        if code == 0:
            end_of_game_text = ("You loose !\nYou have met the Guardian but\n"
                                "you did not found the 3 items ☹\n "
                                "\n Press any key to play again...")
        elif code == 1:
            end_of_game_text = ("Well Done !!! ☺\n"
                                "You have slept the guardian using\n"
                                "an anesthetic made with the 3 items !\n"
                                "MacGyver is escaping the maze...\n "
                                "\n Press any key to play again...")

        View.display_text_below_maze(window, end_of_game_text, 18)
