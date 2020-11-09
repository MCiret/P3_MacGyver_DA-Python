from Model.constantes import MAZE_NB_ROOMS_PER_SIDE


class View:
    @staticmethod
    def maze_display(maze_list):
        """
        Display the maze with ascii character (using the __repr__() method overriding)
        :param maze_list: (list) maze rooms (class)
        """
        for i, elem in enumerate(maze_list):
            if (i+1) % MAZE_NB_ROOMS_PER_SIDE == 0:
                print(elem)

            else:
                print(elem, end="")
