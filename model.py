from random import sample
from Model.constantes import ascii_to_class_dict, items_list
from Model.needle import Needle
from Model.ether import Ether
from Model.tube import Tube
from Model.wall import Wall
from Model.hallway import Hallway
from Model.mac_gyver import MacGyver
from Model.guardian import Guardian


class Maze:
    @staticmethod
    def load_from_file(empty_maze_list=[]):
        """
        The :param empty_maze_list filled with class instances corresponding to each ascii character in the text file loaded
        """
        with open("Labyrinthe_ascii_OK.txt", encoding="utf-8") as f:
            for line in f:
                line = line.strip('\n')
                keep_char = True
                for char in line:
                    if keep_char:
                        empty_maze_list.append(globals()[ascii_to_class_dict[char]]())
                        keep_char = False
                    else:
                        keep_char = True

    @staticmethod
    def hallway_index_list(built_maze_list):
        """
        :param built_maze_list: (list) maze rooms (class) builded using the load_from_file() above
        :return: (list) index (int) of hallway rooms in the maze
        """
        return [idx for idx, room in enumerate(built_maze_list) if type(room) == Hallway]

    @staticmethod
    def rand_items_pos(hallway_id_list):
        """
        :param hallway_id_list: (list) maze hallways index (int)
        :return: (list) the 3 items indexes (int) randomly generated
        """
        return sample(hallway_id_list, k=3)

    @staticmethod
    def add_items(rand_items_pos, built_maze_list):
        """
        The :param builded_maze_list modified = 3 Hallway class instances replacing with items classes instances
        :param built_maze_list: (list) maze rooms (class) builded using the load_from_file() above
        :param rand_items_pos: (list) index (int) for placing the 3 items in the maze list
        """
        for pos, item_str in zip(rand_items_pos, items_list):
            print(item_str, " --> ", pos)
            built_maze_list[pos] = globals()[item_str]()


def main():
    curr_maze_list = []
    Maze.load_from_file(curr_maze_list)
    Maze.add_items(Maze.rand_items_pos(Maze.hallway_index_list(curr_maze_list)), curr_maze_list)

    ### Maze displaying ###
    i = 1
    for elem in curr_maze_list:
        if i % 15 == 0:
            print(type(elem))
            i += 1
        else:
            print(type(elem), end="")
            i += 1
    ########################


main()
