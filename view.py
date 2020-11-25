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
            x_pos_pixel = x_sprite * cste.SPRITE_SIZE
            y_pos_pixel = y_sprite * cste.SPRITE_SIZE
            elem.draw_tile(window, x_pos_pixel, y_pos_pixel)
            x_sprite += 1
            if x_sprite == cste.NB_SPRITE_SIDE:
                x_sprite = 0
                y_sprite += 1
        pygame.display.flip()

    @staticmethod
    def display_text_below_maze(window, text, text_size=12, text_color=(255, 255, 255)):
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
            x, y = window.blit(text_font.render(line, True, text_color),
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
            impos_move_text = ("/!!!\\ You are going to fall out the maze... "
                               "teleporting is not possible /!!!\\\n"
                               "Please try a different direction...\n")
        elif code == 2:
            impos_move_text = ("/!!!\\ You are going to bang into a wall... "
                               "cwall crossing is not possible /!!!\\\n"
                               "Please try a different direction...\n")
        View.display_text_below_maze(window, impos_move_text,
                                     text_size=16, text_color=(255, 0, 0))

    @staticmethod
    def display_items_counter(found_items_list, window):
        """
        Displays (on the right) the number of found items.
        :param found_items_list: (list) Found items (str)
        :param window: (pygame.Surface) main window.
        """
        assert(type(found_items_list) is list
               and len(found_items_list) in range(0, len(cste.ITEMS_PICTURES_PATH_DICT) + 1))
        assert (type(window) is pygame.Surface)

        found_items_text = ""
        for elem in found_items_list:
            found_items_text += "  - " + elem + "\n"

        View.display_text_maze_right_side(window,
                  f"Mac Gyver has found\n"
                  f"{len(found_items_list)} of "
                  f"{len(cste.ITEMS_PICTURES_PATH_DICT)} items :\n"
                  f"\n \n{found_items_text}", text_size=14)

    @staticmethod
    def display_all_items_found_picture(window, picture):
        """
        Displays (on the right) an anesthetic picture when all items
        has been found.
        :param window: (pygame.Surface) main window.
        :param picture: (pygame.Surface) picture to blit to window.
        """
        assert (type(window) is pygame.Surface
                and type(picture) is pygame.Surface)

        window.blit(picture, (cste.MAZE_SIDE_SIZE + 25,
                              (cste.MAZE_SIDE_SIZE / 4) * 2.5))

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
