import Model.constantes


class View:
    @staticmethod
    def maze_display(maze_list):
        """
        Display the maze with ascii character (using the __repr__() method overriding)
        :param maze_list: (list) maze rooms (class)
        """
        for i, elem in enumerate(maze_list):
            if (i+1) % Model.constantes.MAZE_NB_ROOMS_PER_SIDE == 0:
                print(elem)

            else:
                print(elem, end="")

    @staticmethod
    def user_input_to_int():
        """
        :return: (int) A number corresponding to the user's asked move
        If a move is asked : -1 = w / west ; +1 = e / east ; -15 = n / north ; +15 = s / south
        If quit is asked : 0
        """
        i = 1
        str_cmd_info = "("
        for elem in Model.constantes.USER_MOVE_CMD:
            if i % 2 == 0:
                str_cmd_info += elem + ", "
                i += 1
            else:
                str_cmd_info += elem + " = "
                i += 1
        for elem in Model.constantes.USER_QUIT_CMD:
            if elem == Model.constantes.USER_QUIT_CMD[len(Model.constantes.USER_QUIT_CMD)-1]:  # last element
                str_cmd_info += elem + ")"
            else:
                str_cmd_info += elem + " = "

        return input(f"Which direction Mac Gyver should go in the maze ?\n{str_cmd_info} --> ")
