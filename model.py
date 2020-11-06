from Model.constantes import ascii_to_class_dict
from Model.tile import Tile
import Model.needle
import Model.ether
import Model.tube
import Model.wall
import Model.hallway
import Model.mac_gyver
import Model.guardian


class Maze:

    @staticmethod
    def load_from_file(maze_list = []):
        with open("Labyrinthe_ascii_OK.txt", encoding="utf-8") as f:
            for line in f:
                line = line.strip('\n')
                for char in line:
                    pass
                    # maze_list.append(instance objet correspondant au caractère ascii chargé)


def main():
    glob_dict = globals()
    for key in glob_dict:
        print(key, ":", glob_dict[key])


main()
