import constantes as cste
from Model.wall import Wall
from Model.hallway import Hallway
from Model.mac_gyver import MacGyver
from Model.guardian import Guardian
from Model.needle import Needle
from Model.ether import Ether
from Model.tube import Tube
from random import sample
import pygame
from pygame import *
pygame.init()


class Model:
    """
    To load and/or check data.
    """
    MAZE_HALLWAYS_INDEX_DICT = {"all_hallways": [], "guardian_tile": -1,
                                "macgyver_start_tile": -1}
    PICTURES_DICT = {}

    @staticmethod
    def initialize_pygame_window():
        """
        Used to obtain the pygame window before game initializing.
        :return: (pygame.Surface) An initialized pygame main window (size,
        title and icon).
        """
        window = pygame.display.set_mode((cste.WINDOW_WIDTH,
                                          cste.WINDOW_HEIGHT))
        icon = pygame.image.load(cste.ASCII_TO_PICTURE_DICT['M'])
        pygame.display.set_icon(icon)
        pygame.display.set_caption(cste.WINDOW_TITLE)
        return window

    @classmethod
    def load_pictures(cls):
        """
        Filled the class attribute PICTURE_DICT (dict) with pictures
        loaded with pygame.
        Each picture is a Tile() instance attribute.
        """
        if len(Model.PICTURES_DICT) == 0:
            for char_key in cste.ASCII_TO_PICTURE_DICT:
                cls.PICTURES_DICT[char_key] = \
                    pygame.image.load(cste.ASCII_TO_PICTURE_DICT[char_key]).convert()

    @staticmethod
    def maze_load_from_file(empty_maze_list):
        """
        Each ascii characters representing the maze structure is converted to
        Tile's subclasses instance using the globals() dict (all Tile's
        subclasses have to be imported here).
        The :param empty_maze_list: an empty list which will be filled and so
        modified (side effect).
        """
        assert(type(empty_maze_list) is list and len(empty_maze_list) == 0)

        Model.load_pictures()

        with open(cste.MAZE_LVL1, encoding="utf-8") as f:
            for line in f:
                line = line.strip('\n')
                # In the text file, one maze tile is a doubled ascii character.
                # So to fill the list, one in two tiles are kept :
                keep_char = True
                for char in line:
                    if keep_char:
                        tile = globals()[cste.ASCII_TO_CLASS_DICT[char]](Model.PICTURES_DICT[char])
                        empty_maze_list.append(tile)
                        keep_char = False
                    else:
                        keep_char = True

    @classmethod
    def hallway_index_dict(cls, built_maze_list):
        """
        Fills the class attribute MAZE_HALLWAYS_INDEX_DICT (dict) with indexes
        (int) of hallways tiles in the maze including Guardian and MacGyver
        indexes which are also recorded apart using 2 more keys.
        => Their tiles have not to be used for adding the 3 items in the maze.
        :param built_maze_list: (list) maze tiles (Tile subclasses) (filled
        with load_from_file() method (above).
        """
        assert(type(built_maze_list) is list and
               len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)

        for idx, tile in enumerate(built_maze_list):
            if type(tile) == Hallway:
                cls.MAZE_HALLWAYS_INDEX_DICT["all_hallways"].append(idx)
            elif type(tile) == MacGyver:
                cls.MAZE_HALLWAYS_INDEX_DICT["all_hallways"].append(idx)
                cls.MAZE_HALLWAYS_INDEX_DICT["macgyver_start_tile"] = idx
            elif type(tile) == Guardian:
                cls.MAZE_HALLWAYS_INDEX_DICT["all_hallways"].append(idx)
                cls.MAZE_HALLWAYS_INDEX_DICT["guardian_tile"] = idx

    @staticmethod
    def rand_items_pos():
        """
        :return: (list) 3 DIFFERENT indexes randomly chosen among the maze
        hallways indexes list.
        """
        # To not add items in Guardian or MacGyver tiles
        tile_idx_ok_to_place_item = \
            [idx for idx in Model.MAZE_HALLWAYS_INDEX_DICT["all_hallways"]
             if idx != Model.MAZE_HALLWAYS_INDEX_DICT["guardian_tile"]
             and idx != Model.MAZE_HALLWAYS_INDEX_DICT["macgyver_start_tile"]]
        # random method without replacement
        return sample(tile_idx_ok_to_place_item, k=3)

    @staticmethod
    def add_items(rand_items_pos, built_maze_list):
        """
        Item subclasses (Ether, Tube, Needle) are instanced and randomly
        added in the maze list.
        :param built_maze_list: (list) maze tiles (Tile subclasses).
        :param rand_items_pos: (list) indexes (int) to add the 3 items
        in the maze list.
        """
        assert(type(rand_items_pos) is list
               and len(rand_items_pos) == len(cste.ITEMS_CHAR_LIST))
        assert(type(built_maze_list) is list
               and len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)

        for pos, item_char in zip(rand_items_pos, cste.ITEMS_CHAR_LIST):
            built_maze_list[pos] = globals()[cste.ASCII_TO_CLASS_DICT[item_char]](Model.PICTURES_DICT[item_char])

    @staticmethod
    def is_wall(maze_tile_id):
        """
        :param maze_tile_id: (int) a maze tile index.
        :return: (bool) True if :param maze_square_id correspond to a wall.
        """
        assert(type(maze_tile_id) is int
               and maze_tile_id in range(0, cste.NB_SPRITE_SIDE ** 2))
        return maze_tile_id \
            not in Model.MAZE_HALLWAYS_INDEX_DICT["all_hallways"]

    @ staticmethod
    def is_out_of_maze(move_cmd, mg_current_pos_id):
        """
        To avoid moving Mac Gyver out of the maze window.
        :param move_cmd: (int) Number will be added/subtracted to the current
        MG index to move him in the maze list.
        :param mg_current_pos_id: (int) the current MG index in the maze list.
        :return: (bool) True if MG is on one of the 4 side and if the move_cmd
        goes outside.
        """
        assert(type(move_cmd) is int
               and move_cmd in cste.USER_INPUT_CMD.values())
        assert(type(mg_current_pos_id) is int
               and mg_current_pos_id in range(0, cste.NB_SPRITE_SIDE ** 2))

        if move_cmd == -15:  # north
            return mg_current_pos_id < (cste.NB_SPRITE_SIDE - 1)
        elif move_cmd == 15:  # south
            return mg_current_pos_id > (cste.NB_SPRITE_SIDE ** 2) \
                                        - 1 - cste.NB_SPRITE_SIDE
        elif move_cmd == -1:  # west
            return mg_current_pos_id % 15 == 0
        elif move_cmd == 1:  # east
            return (mg_current_pos_id+1) % 15 == 0

    @staticmethod
    def is_mg_in_guardian_tile(built_maze_list):
        """
        Each time Mac Gyver moves, checks if he has met the Guardian.
        :param built_maze_list: (list) maze tiles (Tile subclasses)
        :return: (bool) True if user has reached the guardian tile.
        """
        assert(type(built_maze_list) is list
               and len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)

        return built_maze_list.count(Guardian()) == 0

    @staticmethod
    def how_many_items_in_maze(built_maze_list):
        """
        :param built_maze_list: (list) maze tiles (Tile subclasses)
        :return: (int) Number of items in the maze.
        """
        assert(type(built_maze_list) is list
               and len(built_maze_list) == cste.NB_SPRITE_SIDE ** 2)

        res_nb_items = 0
        for item in (item_class for item_class in
                     (globals()[cste.ASCII_TO_CLASS_DICT[item_char]]()
                      for item_char in cste.ITEMS_CHAR_LIST)):
            res_nb_items += built_maze_list.count(item)

        return res_nb_items
