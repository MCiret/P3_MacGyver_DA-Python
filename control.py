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
    """
    To initialize and use/calculate data according to user inputs.
    Remark : because the program uses pygame module, user inputs are handled
    here (in pygame loops) instead of handled by the view part.
    """
    @staticmethod
    def initialize_game(empty_list):
        """
        1) Creates the main pygame window
        2) Reads the text file and loads corresponding Tile subclasses
        in the :param empty_list (side effect);
        3) Creates a maze hallways indexes list (Model class attribute);
        4) Items are randomly added in the maze list;
        :param empty_list: (list)
        :return: (pygame.Surface) the main pygame window created

        """
        assert(type(empty_list) is list and len(empty_list) == 0)

        # Pygame window has to be created before maze_load_from_file() to
        # enable the loaded picture to be convert
        window = Model.initialize_pygame_window()
        Model.maze_load_from_file(empty_list)
        # From this point empty_list is no longer empty (side effect).
        Model.hallway_index_dict(empty_list)
        Model.add_items(Model.rand_items_pos(), empty_list)
        return window

    @staticmethod
    def str_move_to_int(str_move):
        """
        :param str_move: (str) Direction corresponding to the arrow key pressed
        by user.
        :return: (int) The number to be added/subtracted to the MacGyver
        current index in the maze list.
        """
        assert(type(str_move) is str and str_move in cste.USER_INPUT_CMD)

        return cste.USER_INPUT_CMD[str_move]

    @staticmethod
    def is_move_possible(mg_current_pos_id, move_code, window):
        """
        Each time Mac Gyver moves, checks if it possible (i.e the destination
        is not a wall or maze edge). A text is displayed to inform user.
        :param mg_current_pos_id: (int) the current MG index in the maze list.
        :param move_code: (int) Number to be be added/subtracted to the
        current MG index.
        :param window: (pygame.Surface) main window.
        :return: (bool) True if the movement is possible.
        """
        assert (type(mg_current_pos_id) is int
                and mg_current_pos_id in range(0, cste.NB_SPRITE_SIDE ** 2))
        assert (type(move_code) is int
                and move_code in cste.USER_INPUT_CMD.values())
        assert (type(window) is pygame.Surface)

        if Model.is_out_of_maze(move_code, mg_current_pos_id):
            View.impossible_move_text(1, window)
            return False
        else:
            if Model.is_wall(mg_current_pos_id + move_code):
                View.impossible_move_text(2, window)
                return False
            else:
                return True

    @staticmethod
    def calculate_dest_id(mg_current_pos_id, move_code):
        """
        :param mg_current_pos_id: (int) the current MG index in the maze list.
        :param move_code: (int) Number will be added/subtracted to the
        current MG index to move him as user asked.
        :return: (int) the MG destination index in the maze list.
        """
        assert (type(mg_current_pos_id) is int
                and mg_current_pos_id in range(0, cste.NB_SPRITE_SIDE ** 2))
        assert (type(move_code) is int
                and move_code in cste.USER_INPUT_CMD.values())

        return mg_current_pos_id + move_code

    @staticmethod
    def move_mg(built_maze_list, move_code, window):
        """
        :param built_maze_list: (list) maze tiles (Tile subclasses)
        :param move_code: (int) Number add/subtract to the current MG index to
        move him in the maze list.
        :param window: (pygame.Surface) main window.
        """
        assert(type(built_maze_list) is list
               and len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)
        assert (type(move_code) is int
                and move_code in cste.USER_INPUT_CMD.values())
        assert (type(window) is pygame.Surface)

        # get the current MG position in maze
        curr_mg_id = built_maze_list.index(MacGyver())
        if Control.is_move_possible(curr_mg_id, move_code, window):
            dest_maze_id = Control.calculate_dest_id(curr_mg_id, move_code)

            # If MG goes to item ou guardian tile,
            # a new tile has to be instanced :
            if (isinstance(built_maze_list[dest_maze_id], Item)
                    or isinstance(built_maze_list[dest_maze_id], Guardian)):
                built_maze_list[dest_maze_id] = built_maze_list[curr_mg_id]
                for char_key in cste.MAZE_ASCII_TO_CLASS_DICT:
                    if cste.MAZE_ASCII_TO_CLASS_DICT[char_key] == "Hallway":
                        built_maze_list[curr_mg_id] = \
                            Hallway(Model.MAZE_CHAR_TO_PICTURES_DICT[char_key])

            # Else, just reverses MG and hallway instances in the list :
            else:
                tmp_mg_instance = built_maze_list[curr_mg_id]
                tmp_dest_instance = built_maze_list[
                    Control.calculate_dest_id(curr_mg_id, move_code)]
                built_maze_list[dest_maze_id] = tmp_mg_instance
                built_maze_list[curr_mg_id] = tmp_dest_instance

    @staticmethod
    def check_items(built_maze_list, window):
        """
        Each time Mac Gyver moves, checks how many items have been found and
        update the counter (text) displaying. And if all items have been
        found, an anesthetic picture is displayed.
        :param built_maze_list: (list) maze tiles (Tile subclasses)
        :param window: (pygame.Surface) main window.
        """
        assert (type(built_maze_list) is list
                and len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)
        assert (type(window) is pygame.Surface)

        found_items_list = Model.check_items_in_maze(built_maze_list)

        View.display_items_counter(found_items_list, window)

        if len(found_items_list) == len(cste.ITEMS_PICTURES_PATH_DICT):
            anesthetic_item = Tile(Model.OTHERS_PICTURE_DICT["All found items"])
            View.display_all_items_found_picture(window,
                                                 anesthetic_item.picture)

    @staticmethod
    def is_game_failure(built_maze_list):
        """
        Each time Mac Gyver moves, checks if he has reached the Guardian tile.
        If so, it checks if all items has been found.
        :param built_maze_list: (list) maze (int)
        :return: (bool) True
        """
        assert(type(built_maze_list) is list
               and len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)

        return len(Model.check_items_in_maze(built_maze_list))

    @staticmethod
    def game_playing():
        # MAIN LOOP
        run = True
        while run:
            # Initializes the maze list and creates the pygame main window
            maze_list = []
            window = Control.initialize_game(maze_list)
            View.display_game_rules(window, Model.OTHERS_PICTURE_DICT["Move cmd"])
            View.maze_display(maze_list, window)

            game_playing = True
            game_ending = False
            # RUNNING GAME LOOP (user moves inputs enabled)
            while game_playing:
                pygame.time.Clock().tick(30)  # to limit loop speed
                for user_event in pygame.event.get():
                    if user_event.type == QUIT:
                        run = False
                        game_playing = False
                    elif user_event.type == KEYDOWN:
                        View.display_game_rules(window, Model.OTHERS_PICTURE_DICT["Move cmd"])
                        if user_event.key == K_DOWN:
                            user_nb_move = Control.str_move_to_int("south")
                            Control.move_mg(maze_list, user_nb_move, window)
                        elif user_event.key == K_UP:
                            user_nb_move = Control.str_move_to_int("north")
                            Control.move_mg(maze_list, user_nb_move, window)
                        elif user_event.key == K_RIGHT:
                            user_nb_move = Control.str_move_to_int("east")
                            Control.move_mg(maze_list, user_nb_move, window)
                        elif user_event.key == K_LEFT:
                            user_nb_move = Control.str_move_to_int("west")
                            Control.move_mg(maze_list, user_nb_move, window)
                # View.maze_display_terminal(built_maze_list)
                View.maze_display(maze_list, window)
                Control.check_items(maze_list, window)
                pygame.display.flip()
                if Model.is_mg_in_guardian_tile(maze_list):
                    game_playing = False
                    game_ending = True

            # RESULTS GAME LOOP (user moves inputs disabled)
            while game_ending:
                pygame.time.Clock().tick(30)  # to limit loop speed
                if Control.is_game_failure(maze_list) \
                        < len(cste.ITEMS_PICTURES_PATH_DICT):
                    # MG has not got the 3 items required to win :
                    View.end_of_game_text(0, window)
                else:
                    # MG has got the 3 items required to win :
                    View.end_of_game_text(1, window)
                pygame.display.flip()
                for user_event in pygame.event.get():
                    if user_event.type == QUIT:
                        run = False
                        game_ending = False
                    elif user_event.type == KEYDOWN:
                        game_ending = False
