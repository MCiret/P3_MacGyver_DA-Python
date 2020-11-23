import constantes as cste
from model import Model
from view import View
from Model.tile import Tile
from Model.item import Item
from Model.guardian import Guardian
from Model.mac_gyver import MacGyver
from Model.hallway import Hallway
import pygame
from pygame import *
pygame.init()


class Control:
    @staticmethod
    def initialize_game(empty_list):
        """
        1) Reads the text file and loads corresponding classes in the :param empty_list (side effect).
        2) Creates a maze hallways indexes list (Model class attribute).
        3) 3 different indexes are randomly chosen in the hallways and directly used to place the 3 items
        4) Returns the maze hallways indexes list to a later usage when MG is moved..
        :param empty_list: (list)
        :return: (pygame.Surface) a pygame sized window with title and icon

        """
        window = Model.initialize_pygame_window()
        Model.maze_load_from_file(empty_list)
        # Actually, from this point empty_list is no longer empty. It has been filled by side effect..
        Model.hallway_index_dict(empty_list)
        Model.add_items(Model.rand_items_pos(), empty_list)
        return window

    @staticmethod
    def user_input_to_int(user_cmd_entry):
        """
        :param user_cmd_entry: (str) The command entered by user (to move or to quit)
        :return: (int) A number corresponding to :param user_cmd_entry :
        - If a move is asked, this number is add/subtract from the current MacGyver index in maze list :
                -1 = w / west ; +1 = e / east ; -15 = n / north ; +15 = s / south
        - If quit is asked : 0
        """
        assert(type(user_cmd_entry) is str)

        return cste.USER_INPUT_CMD[user_cmd_entry]

    @staticmethod
    def is_move_possible(mg_pos_id, move_code, built_maze_list, window):
        """
        If the movement is not possible (wall or maze edge), a message is displayed and False is returned.
        Else, True is returned.
        :param mg_pos_id: (int) the current MG index in the maze list
        :param move_code: (int) Number will be added/subtracted to the current MG index to move him as user asked
        :param built_maze_list: (list) maze (class)
        :return: (bool) True if the movement is possible
        """
        assert (type(mg_pos_id) is int)
        assert (type(move_code) is int and move_code in (-1, 1, -15, 15))

        if Model.is_out_of_maze(move_code, mg_pos_id):
            View.impossible_move_msg(1, window)
            return False
        else:
            if Model.is_wall(mg_pos_id + move_code):
                View.impossible_move_msg(2, window)
                return False
            else:
                return True

    @staticmethod
    def calculate_dest_id(mg_pos_id, asked_move_nb):
        """
        :param mg_pos_id: (int) the current MG index in the maze list
        :param asked_move_nb: (int) Number will be added/subtracted to the current MG index to move him as user asked
        :return: (int) the new MG index in the maze list
        """
        assert(type(mg_pos_id) is int)
        assert(type(asked_move_nb) is int and asked_move_nb in (-1, 1, -15, 15))

        return mg_pos_id + asked_move_nb

    @staticmethod
    def move_mg(built_maze_list, move_nb, window):
        """
        :param built_maze_list: (list) maze (class)
        :param move_nb: (int) Number add/subtract to the current MG index (obtained from user_input_to_int())
        """
        assert(type(built_maze_list) is list and len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)
        assert(type(move_nb) is int)

        # get the current MG position in maze
        curr_mg_id = built_maze_list.index(MacGyver())
        if Control.is_move_possible(curr_mg_id, move_nb, built_maze_list, window):
            dest_maze_id = Control.calculate_dest_id(curr_mg_id, move_nb)
            if isinstance(built_maze_list[dest_maze_id], Item) or isinstance(built_maze_list[dest_maze_id], Guardian):
                built_maze_list[dest_maze_id] = built_maze_list[curr_mg_id]
                for char_key in cste.ASCII_TO_CLASS_DICT:
                    if cste.ASCII_TO_CLASS_DICT[char_key] == "Hallway":
                        hallway_picture_key = char_key
                built_maze_list[curr_mg_id] = Hallway(Model.PICTURES_DICT[hallway_picture_key])
            else:
                tmp_mg_instance = built_maze_list[curr_mg_id]
                tmp_dest_instance = built_maze_list[Control.calculate_dest_id(curr_mg_id, move_nb)]
                built_maze_list[dest_maze_id] = tmp_mg_instance
                built_maze_list[curr_mg_id] = tmp_dest_instance

    @staticmethod
    def check_items(built_maze_list, window):
        """
        :param built_maze_list:
        :return:
        """
        View.display_items_counter(len(cste.ITEMS_CHAR_LIST) - Model.how_many_items_in_maze(built_maze_list), window)

        if Model.how_many_items_in_maze(built_maze_list) == 0:
            anesthetic_item = Tile(Model.PICTURES_DICT['A'])
            View.display_anesthetic_made_picture(window, anesthetic_item.picture)

    @staticmethod
    def is_game_failure(built_maze_list):
        """
        Called only if MG has reached the guardian tile (end of while is_guardian() loop in game_playing())
        :param built_maze_list: (list) maze (int)
        :return: (bool) True
        """
        assert(type(built_maze_list) is list and len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)

        return Model.how_many_items_in_maze(built_maze_list)

    @staticmethod
    def game_playing():

        run = True
        while run:
            maze_list = []
            window = Control.initialize_game(maze_list)
            View.display_game_rules(window)
            View.maze_display_terminal(maze_list)
            View.maze_display(maze_list, window)
            game_playing = True
            game_ending = False
            while game_playing:
                pygame.time.Clock().tick(30)  # to limit loop speed
                for user_event in pygame.event.get():
                    if user_event.type == QUIT:
                        run = False
                        game_playing = False
                    elif user_event.type == KEYDOWN:
                        View.display_game_rules(window)
                        if user_event.key == K_DOWN:
                            user_nb_move = Control.user_input_to_int("south")
                            Control.move_mg(maze_list, user_nb_move, window)
                        elif user_event.key == K_UP:
                            user_nb_move = Control.user_input_to_int("north")
                            Control.move_mg(maze_list, user_nb_move, window)
                        elif user_event.key == K_RIGHT:
                            user_nb_move = Control.user_input_to_int("east")
                            Control.move_mg(maze_list, user_nb_move, window)
                        elif user_event.key == K_LEFT:
                            user_nb_move = Control.user_input_to_int("west")
                            Control.move_mg(maze_list, user_nb_move, window)
                # View.maze_display_terminal(built_maze_list)
                View.maze_display(maze_list, window)
                Control.check_items(maze_list, window)
                pygame.display.flip()
                if Model.is_mg_in_guardian_tile(maze_list):
                    game_playing = False
                    game_ending = True

            while game_ending:
                pygame.time.Clock().tick(30)  # to limit loop speed
                if Control.is_game_failure(maze_list) > 0:
                    # MG has not got the 3 items required to win :
                    View.end_of_game_msg(0, window)
                else:
                    # MG has got the 3 items required to win :
                    View.end_of_game_msg(1, window)
                pygame.display.flip()
                for user_event in pygame.event.get():
                    if user_event.type == QUIT:
                        run = False
                        game_playing = False
                        game_ending = False
                    elif user_event.type == KEYDOWN:
                        game_playing = True
                        game_ending = False



