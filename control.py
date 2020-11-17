import constantes as cste
from model import Model
from view import View
from Model.mac_gyver import MacGyver
from Model.hallway import Hallway


class Control:
    @staticmethod
    def initialize_game(empty_list):
        """
        1) Reads the text file and loads corresponding classes in the :param empty_list (side effect).
        2) Creates a maze hallways indexes list (Model class attribute).
        3) 3 different indexes are randomly chosen in the hallways and directly used to place the 3 items
        4) Returns the maze hallways indexes list to a later usage when MG is moved..
        :param empty_list: (list)
        :return: (list) The hallways indexes list

        """
        # PYGAME --> pictures = ....
        Model.maze_load_from_file(empty_list)
        # PYGAME --> Model.maze_load_from_file(empty_list, pictures)
        # Actually, from this point empty_list is no longer empty. It has been filled by side effect..
        Model.hallway_index_list(empty_list)
        Model.add_items(Model.rand_items_pos(), empty_list)

    @staticmethod
    def check_user_input(user_move_entry):
        """
        :return: (bool) True if the :param user_move_cmd is valid (i.e belongs to the dict (see Model/constantes.py))
        """
        assert (type(user_move_entry) is str)

        return user_move_entry in cste.USER_INPUT_CMD.keys()

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
    def is_move_possible(mg_pos_id, move_code):
        """
        If the movement is not possible (wall or maze edge), a message is displayed and False is returned.
        Else, True is returned.
        :param mg_pos_id: (int) the current MG index in the maze list
        :param move_code: (int) Number will be added/subtracted to the current MG index to move him as user asked
        :return: (bool) True if the movement is possible
        """
        assert (type(mg_pos_id) is int)
        assert (type(move_code) is int and move_code in (-1, 1, -15, 15))

        if Model.is_out_of_maze(move_code, mg_pos_id):
            View.impossible_move_msg(1)
            return False
        else:
            if Model.is_wall(mg_pos_id + move_code):
                View.impossible_move_msg(2)
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
    def move_mg(built_maze_list, move_nb):
        """
        :param built_maze_list: (list) maze (class)
        :param move_nb: (int) Number add/subtract to the current MG index (obtained from user_input_to_int())
        """
        assert(type(built_maze_list) is list and len(built_maze_list) == cste.MAZE_NB_TILES_PER_SIDE**2)
        assert(type(move_nb) is int)

        # get the current MG position in maze
        curr_mg_id = built_maze_list.index(MacGyver())
        if Control.is_move_possible(curr_mg_id, move_nb):
            built_maze_list[Control.calculate_dest_id(curr_mg_id, move_nb)] = MacGyver()
            built_maze_list[curr_mg_id] = Hallway()

    @staticmethod
    def is_game_failure(built_maze_list):
        """
        Called only if MG has reached the guardian tile (end of while is_guardian() loop in game_playing())
        :param built_maze_list: (list) maze (int)
        :return: (bool) True
        """
        assert(type(built_maze_list) is list and len(built_maze_list) == cste.MAZE_NB_TILES_PER_SIDE**2)

        return Model.is_there_items_in_maze(built_maze_list)

    @staticmethod
    def game_playing(built_maze_list):
        """
        :param built_maze_list: (list) the maze tiles (class) built
        """
        View.display_game_rules()
        View.maze_display(built_maze_list)
        while not Model.is_mg_in_guardian_tile(built_maze_list):
            user_entry = View.user_input_ask_msg()
            while not Control.check_user_input(user_entry):
                View.wrong_user_entry_msg()
                user_entry = View.user_input_ask_msg()
            int_user_entry = Control.user_input_to_int(user_entry)
            if int_user_entry == 0:
                View.quitting_game_msg()
                quit()
            else:
                Control.move_mg(built_maze_list, int_user_entry)
                View.maze_display(built_maze_list)
        # End of 1st while loop <=> MG has reached the Guardian's tile

        if Control.is_game_failure(built_maze_list):
            # MG has not got the 3 items required to win :
            View.end_of_game_msg(0)
        else:
            # MG has got the 3 items required to win :
            View.end_of_game_msg(1)
