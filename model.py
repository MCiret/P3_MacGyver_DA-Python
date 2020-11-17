from random import sample
import constantes as cste
from Model.wall import Wall
from Model.hallway import Hallway
from Model.mac_gyver import MacGyver
from Model.guardian import Guardian
from Model.needle import Needle
from Model.ether import Ether
from Model.tube import Tube


class Model:
    GAME_STARTING_MAZE_HALLWAYS_INDEX_LIST = []

    @staticmethod
    def maze_load_from_file(empty_maze_list):
        """
        The :param empty_maze_list filled with class instances corresponding to each ascii character in the text file loaded
        """
        with open("Resources/Maze_lvl1.txt", encoding="utf-8") as f:
            for line in f:
                line = line.strip('\n')
                # In the loaded text file, the each maze tile is a doubled ascii character.
                # => For the list filling, one in two tiles are kept :
                keep_char = True
                for char in line:
                    if keep_char:
                        empty_maze_list.append(globals()[cste.ASCII_TO_CLASS_DICT[char]]())
                        keep_char = False
                    else:
                        keep_char = True

    @classmethod
    def hallway_index_list(cls, built_maze_list):
        """
        :param built_maze_list: (list) maze tiles (class) builded using the load_from_file() above
        :return: (list) index (int) of hallways tiles in the maze which includes Guardian and MacGyver tile index
        which has been placed in the maze in method maze_load_from_file(). However, the 3 items are not yet placed
        in the maze.
        """
        assert(type(built_maze_list) is list and len(built_maze_list) == cste.MAZE_NB_TILES_PER_SIDE**2)

        cls.GAME_STARTING_MAZE_HALLWAYS_INDEX_LIST = [idx for idx, tile in enumerate(built_maze_list)
                                                      if (type(tile) == Hallway
                                                          or type(tile) == Guardian
                                                          or type(tile) == MacGyver)
                                                      ]

    @staticmethod
    def rand_items_pos():
        """
        :return: (list) 3 different indexes randomly chosen among the maze hallways indexes list
        """
        return sample(Model.GAME_STARTING_MAZE_HALLWAYS_INDEX_LIST, k=3)

    @staticmethod
    def is_wall(maze_square_id):
        """
        :param maze_square_id: (int) one maze square index
        :return: (bool) True if :param maze_square_id correspond to a wall
        """
        assert(type(maze_square_id) is int)
        return maze_square_id not in Model.GAME_STARTING_MAZE_HALLWAYS_INDEX_LIST

    @staticmethod
    def is_out_of_maze(move_cmd, mg_current_pos_id):
        """
        :param move_cmd: (int) Number will be added/subtracted to the current MG index to move him as user asked
        :param mg_current_pos_id: (int) the current MG position/index in the maze
        :return: (bool) True if the :param mg_pos corresponds to a maze edge
                and if the :param move_cmd is the same direction
        """
        assert(type(move_cmd) is int)
        assert(type(mg_current_pos_id) is int)

        if move_cmd == -15:  # north move <=> -15 squares
            return mg_current_pos_id < (cste.MAZE_NB_TILES_PER_SIDE-1)  # MG is on the northern edge of the maze
        elif move_cmd == 15:  # south move <=> +15 squares
            return mg_current_pos_id > (cste.MAZE_NB_TILES_PER_SIDE**2) - 1 - cste.MAZE_NB_TILES_PER_SIDE  # MG is on the southern edge of the maze
        elif move_cmd == -1:  # west move <=> -1 square
            return mg_current_pos_id % 15 == 0  # MG is on the western edge of the maze
        elif move_cmd == 1:  # east move <=> +1 square
            return (mg_current_pos_id+1) % 15 == 0  # MG is on the eastern edge of the maze

    @staticmethod
    def is_mg_in_guardian_tile(built_maze_list):
        """
        :param built_maze_list: (list) maze (class)
        :return: (bool) True if user has reached the guardian's tile
        """
        assert(type(built_maze_list) is list and len(built_maze_list) == cste.MAZE_NB_TILES_PER_SIDE**2)

        return built_maze_list.count(Guardian()) == 0

    @staticmethod
    def is_there_items_in_maze(built_maze_list):
        """
        :param built_maze_list: (list) maze (int)
        :return: (bool) True if there it at least one item remaining in the maze
        """
        assert(type(built_maze_list) is list and len(built_maze_list) == cste.MAZE_NB_TILES_PER_SIDE**2)

        for item in (item_class for item_class in (globals()[item_str]() for item_str in cste.ITEMS_LIST)):
            if built_maze_list.count(item) != 0:
                return True

        return False
