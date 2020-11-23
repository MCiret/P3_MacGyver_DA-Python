import constantes as cste
import pygame
from pygame import *
pygame.init()


class View:
    @staticmethod
    def maze_display_terminal(maze_list):
        """
        Display the maze with ascii character (using the __repr__() method overriding)
        :param maze_list: (list) maze tiles (class)
        """
        for i, elem in enumerate(maze_list):
            if (i + 1) % cste.NB_SPRITE_SIDE == 0:
                print(elem)

            else:
                print(elem, end="")

    @staticmethod
    def maze_display(maze_list, window):
        """
        Graphical display of maze
        :param maze_list: (list) maze tiles (class)
        :param window: (pygame.Surface) an initialized pygame window (sized, title, icon)
        """
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
        text_font = pygame.font.SysFont("Calibri", text_size)
        text_rect = pygame.Rect(10, cste.MAZE_SIDE_SIZE + 25, cste.MAZE_SIDE_SIZE,
                                cste.WINDOW_HEIGHT - cste.MAZE_SIDE_SIZE)
        # blit a black surface to erase previous text
        window.blit(pygame.Surface((cste.WINDOW_WIDTH, cste.WINDOW_HEIGHT - cste.MAZE_SIDE_SIZE)), (0, cste.MAZE_SIDE_SIZE))
        x, y = text_rect.topleft
        for line in text.splitlines():
            x, y = window.blit(text_font.render(line, True, (255, 255, 255)), (x, y)).bottomleft

    @staticmethod
    def display_text_maze_right_side(window, text, text_size=12):
        text_font = pygame.font.SysFont("Calibri", text_size)
        text_rect = pygame.Rect(cste.MAZE_SIDE_SIZE + 10, cste.MAZE_SIDE_SIZE / 4,
                                cste.WINDOW_WIDTH - cste.MAZE_SIDE_SIZE, cste.MAZE_SIDE_SIZE / 4)
        # blit a black surface to erase previous text
        window.blit(pygame.Surface((cste.WINDOW_WIDTH - cste.MAZE_SIDE_SIZE, cste.MAZE_SIDE_SIZE / 4)),
                    (cste.MAZE_SIDE_SIZE + 10, cste.MAZE_SIDE_SIZE / 4))
        x, y = text_rect.topleft
        for line in text.splitlines():
            x, y = window.blit(text_font.render(line, True, (255, 255, 255)), (x, y)).bottomleft

    @staticmethod
    def display_game_rules(window):
        """
        :return: (None) Displays the game rules
        """

        rules_text = (f"Welcome !\nMac Gyver is lost in a maze... Could you help him to escape ?\n"
                      f"A guardian is watching over the maze exit...\n"
                      f"Look for items which could help Mac Gyver : Ether + Tube + (very discreet) Needle\n "
                      f"\n TO PLAY : Use directional keys to move MacGyver in the maze.\n")
        View.display_text_below_maze(window, rules_text)

    @staticmethod
    def impossible_move_msg(code, window):
        """
        :param code: (int) Corresponding to the reason why the movement is impossible (1 = maze edge ; 2 = wall)
        :return: (None) Display the message
        """
        assert (type(code) is int or code == 1 or code == 2)

        if code == 1:
            impos_mv_text = ("/!!!\\ You are going to fall out the maze... teleporting is not possible /!!!\\\n"
                             "Please try a different direction...\n")
        elif code == 2:
            impos_mv_text = ("/!!!\\ You are going to bang into a wall... and crossing walls is not possible /!!!\\\n"
                             "Please try a different direction...\n")
        View.display_text_below_maze(window, impos_mv_text)

    @staticmethod
    def display_items_counter(nb_items, window):
        """
        :param nb_items:
        :return:
        """
        assert(type(nb_items) is int)

        View.display_text_maze_right_side(window, f"Founded items :\n{nb_items} of 3.")

    @staticmethod
    def display_anesthetic_made_picture(window, picture):
        window.blit(picture, (cste.MAZE_SIDE_SIZE + 25, (cste.MAZE_SIDE_SIZE / 4) * 2))

    @staticmethod
    def end_of_game_msg(code, window):
        """
        :param code: (int) Corresponding to the game outcoming (0 = loose ; 1 = win)
        :return: (None) Only display
        """
        assert (type(code) is int and (code == 0 or code == 1))

        if code == 0:
            end_of_game_text = ("You loose !\nYou have met the Guardian but\nyou did not found the 3 items ☹\n "
                                "\n Press any key to play again...")
        elif code == 1:
            end_of_game_text = ("Well Done !!! ☺\nYou have slept the guardian using\nan anesthetic "
                                "made with the 3 items founded !\n MacGyver is escaping the maze...\n "
                                "\n Press any key to play again...")
        View.display_text_below_maze(window, end_of_game_text, 18)
