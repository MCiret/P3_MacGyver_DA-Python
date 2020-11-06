"""
Game : Help Mac Gyver to escape from the maze...
Author : Marie Ciret
Date : 15/10/20
Move M.G. using keyboard to find the required 3 items to sleep the guardian.
The maze is load from a text file in a list.
Each time the game is started, the 3 items are randomly placed..
"""

import mg_game_constants
from random import sample


def maze_file_loading(file_name):
    """
    :param file_name: (str) file containing the maze to be loaded drawn with ascii characters
    :return: (list) each character (str) extracted one by one :
                - full square "██" (U+2588) <=> wall = 2 char
                - light shade (grey) square "░░" (U+2591) <=> hallway = 2 char
            /!\ squares could be black or white according to color theme settings /!\
                - "MG" <=> Mac Gyver = 2 char
                - "GD" <=> Guardian = 2 char
    """
    assert(type(file_name) is str)

    maze_list = []
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            line = line.strip('\n')
            for char in line:
                maze_list.append(char)
    return maze_list


def maze_display(maze_list, real_maze_view=True):
    """
    :param maze_list: (list) (str ou int) representing the maze (see maze_file_loading() docstring above)
    :param real_maze_view: (bool) True (default) for displaying the maze as he really looks (i.e str characters doubled
    to represent each maze square). Actually, it is not a good practice to recreate lists to transform the maze each
    time it is displayed..
    :return: (None) Display the maze
    """
    assert(type(maze_list) is list)
    assert(type(real_maze_view) is bool)

    reduce_bool = (len(maze_list) == mg_game_constants.MAZE_NB_SQUARE_PER_SIDE**2)

    print("Let's have a look at the maze below :")

    for i, elem in enumerate(maze_list):
        if reduce_bool:
            if (i+1) % mg_game_constants.MAZE_NB_SQUARE_PER_SIDE == 0:
                if real_maze_view and type(elem) == int:
                    print(maze_int_square_to_real_square(elem))
                else:
                    print(elem)
            else:
                if real_maze_view and type(elem) == int:
                    print(maze_int_square_to_real_square(elem), end="")
                else:
                    print(elem, end="")
        else:
            if (i+1) % (mg_game_constants.MAZE_NB_SQUARE_PER_SIDE*2) == 0:
                if real_maze_view and type(elem) == int:
                    print(maze_int_square_to_real_square(elem))
                else:
                    print(elem)
            else:
                if real_maze_view and type(elem) == int:
                    print(maze_int_square_to_real_square(elem), end="")
                else:
                    print(elem, end="")


def maze_int_square_to_real_square(int_square):
    """
    :param int_square: (int) one maze square represented by an integer
    :return: (str) the real maze square corresponding to the :param int_square (i.e int -> str and doubled)
    """
    assert(type(int_square) is int)

    res_str_char = ""
    if int_square == 0:
        res_str_char = "░░"
    elif int_square == 1:
        res_str_char = "██"
    elif int_square == 2:
        res_str_char = "MG"
    elif int_square == 3:
        res_str_char = "GD"
    elif int_square == 4:
        res_str_char = "EE"
    elif int_square == 5:
        res_str_char = "NN"
    elif int_square == 6:
        res_str_char = "TT"
    return res_str_char


def one_element_in_two_list(entire_list):
    """
    Remove one element in two in the entire_list (in this program this is an easier way to handle the maze then..)
    :param entire_list: (list)
    :return: (list) one in two element of the :param entire_list
    """
    assert(type(entire_list) is list)

    del entire_list[1::2]
    return entire_list


# def double_list_elements(reduced_maze_list):
#     """
#     This function creates a new maze list and do not modify the current maze list (it is used only for more
#     humanly displaying during a game...)
#     :param reduced_maze_list: (list)
#     :return: (list) a new maze where each element is doubled to get back the "real" original maze form
#     """
#     res_entire_list = []
#     for elem in reduced_maze_list:
#         if elem == "M":  # Mac Gyver
#             res_entire_list.append(elem)
#             res_entire_list.append("G")
#         elif elem == "G":  # GuarDian
#             res_entire_list.append(elem)
#             res_entire_list.append("D")
#         else:
#             res_entire_list.append(elem)
#             res_entire_list.append(elem)
#     return res_entire_list


def char_to_int_maze_list(maze_char_list):
    """
    :param maze_char_list: (list) maze (str)
    :return: (list) maze built with int corresponding to the character :
                - Hallway = "░" = 0
                - Wall = "█" = 1
                - Mac Gyver = "M" or "MG" = 2
                - Guardian = "G" or "GD" = 3
                - Ether = "E" or "EE" = 4
                - Needle = "N" or "NN" = 5
                - Tube = "T" or "TT" = 6
    """
    assert(type(maze_char_list) is list)

    reduce_maze_bool = (len(maze_char_list) == mg_game_constants.MAZE_NB_SQUARE_PER_SIDE**2)

    for i, elem in enumerate(maze_char_list):
        if elem == "█":  # if it is a wall square
            maze_char_list[i] = 1
        elif elem == "░":  # if it is a hallway square
            maze_char_list[i] = 0
        elif elem == "M":  # if it the square where Mac Gyver is
            maze_char_list[i] = 2
        elif elem == "G":  # if it the square where the Guardian is
            if reduce_maze_bool:
                maze_char_list[i] = 3
            elif [i + 1] == "D":
                maze_char_list[i] = 3
            else:
                maze_char_list[i] = 2
        elif elem == "D":  # if it the square where the Ether bottle is
            maze_char_list[i] = 3
        elif elem == "E":  # if it the square where the Ether bottle is
            maze_char_list[i] = 4
        elif elem == "N":  # if it the square where the Needle is
            maze_char_list[i] = 5
        elif elem == "T":  # if it the square where the plastic Tube is
            maze_char_list[i] = 6
    return maze_char_list


# def int_to_char_maze_list(maze_int_list):
#     """
#     This function creates a new maze list and do not modify the current maze list (it is used only for more
#     humanly displaying during a game...)
#     :param maze_int_list: (list) maze built with int (see char_to_int_maze_list() docstring above)
#     :return: (list) a new maze built with char corresponding to the int :
#                 - 0 = Hallway = "░"
#                 - 1 = Wall = "█"
#                 - 2 = Mac Gyver = "M" or "MG"
#                 - 3 = Guardian = "G" or "GD"
#                 - 4 = Ether = "E" or "EE"
#                 - 5 = Needle = "N" or "NN"
#                 - 6 = Tube = "T" or "TT"
#     """
#     reduce_maze_bool = (len(maze_int_list) == mg_game_constants.MAZE_NB_SQUARE_PER_SIDE ** 2)
#     fake_char_maze_list = []
#     for i, elem in enumerate(maze_int_list):
#         if elem == 1:  # if it is a wall square
#             fake_char_maze_list.append("█")
#         elif elem == 0:  # if it is a hallway square
#             fake_char_maze_list.append("░")
#         elif elem == 2:  # if it the square where Mac Gyver is
#             if reduce_maze_bool:
#                 fake_char_maze_list.append("M")
#             elif fake_char_maze_list[i+1] == 2:
#                 fake_char_maze_list.append("M")
#             else:
#                 fake_char_maze_list.append("G")
#         elif elem == 3:  # if it the square where the Guardian is
#             if reduce_maze_bool:
#                 fake_char_maze_list.append("G")
#             elif fake_char_maze_list[i+1] == 3:
#                 fake_char_maze_list.append("G")
#             else:
#                 fake_char_maze_list.append("D")
#         elif elem == 4:  # if it the square where the Ether bottle is
#             fake_char_maze_list.append("E")
#         elif elem == 5:  # if it the square where the Needle is
#             fake_char_maze_list.append("N")
#         elif elem == 6:  # if it the square where the plastic Tube is
#             fake_char_maze_list.append("T")
#
#     return fake_char_maze_list


# def maze_hallway_index_list(reduced_maze_int_list):
#     """
#     :param reduced_maze_int_list: (list) int representing the maze (see char_to_int_maze_list() docstring above)
#     :return: (list) index of the maze hallway squares (maze_int_list value == 0)
#     """
#     res_maze_hallway_index_list = []
#     for i, elem in enumerate(reduced_maze_int_list):
#         if elem == 0:
#             res_maze_hallway_index_list.append(i)
#     return res_maze_hallway_index_list


# def items_random_location(maze_hallway_id_list):
#     """
#     :param maze_hallway_id_list: (list) index (int) of the hallway squares in the maze
#     :return: (dict) item initial letter (str):(int) item index location in the maze (randomly chosen using sample())
#     """
#     res_items_dict = {}
#     for k in mg_game_constants.ITEMS_NAMES_DICT:
#         res_items_dict[k] = 0
#     for elem, key in zip(sample(maze_hallway_id_list, k=3), res_items_dict):
#         res_items_dict[key] = elem
#     return res_items_dict


# def store_items_all_info_dict(items_id_dict):
#     """
#     :param items_id_dict: (dict) item initial letter (str):(int) item index location in the maze
#     :return: (dict) item initial lettre (str):(dict)
#              {loc_id (str):(int) item square index, int_tag (str):(int) 4 (Ether), 5 (Needle) or 6 (Tube)}
#     """
#     for k in items_id_dict:
#         if k == "E":
#             items_id_dict[k] = {"loc_id": items_id_dict[k], "int_tag": 4}
#         elif k == "N":
#             items_id_dict[k] = {"loc_id": items_id_dict[k], "int_tag": 5}
#         elif k == "T":
#             items_id_dict[k] = {"loc_id": items_id_dict[k], "int_tag": 6}
#     return items_id_dict


def place_items_maze(reduced_maze_int_list):
    """
    :param reduced_maze_int_list: (list) maze (int) ("reduced" means 1 square = 1 character))
    :return: (list) maze (int) where the 3 items are placed
    """
    assert(type(reduced_maze_int_list) is list)

    maze_hallway_list = [i for i, x in enumerate(reduced_maze_int_list) if x == 0]
    items_rand_id_list = sample(maze_hallway_list, k=3)
    for idx, item_int in zip(items_rand_id_list, mg_game_constants.ITEMS_INT_DICT.values()):
        reduced_maze_int_list[idx] = item_int
    return reduced_maze_int_list


def display_game_rules(maze_list):
    """
    :param maze_list: (list) maze (int)
    :return: (None) Only some displaying
    """
    assert(type(maze_list) is list)

    print(f"Welcome in this game !\nMac Gyver (MG) is lost in a maze... Could you help him to escape ?\n"
          f"The only way to escape from the maze is reaching and neutralizing the Guardian (GD).\n"
          f"For that you have to gather 3 items which are hidden in different rooms in the maze :\n"
          f"- Ether bottle (EE)\n- Tube (plastic)(TT)\n- Needle(NN)\n=> Mac Gyver should be able to make something...\n"
          f"Have fun !!")
    maze_display(maze_list)


def ask_user_move_input():
    """
    Display the valid commands to move Mac Gyver and to quit the game
    :return: (str) User entry
    """
    i = 1
    str_cmd_info = "("
    for elem in mg_game_constants.USER_MOVE_CMD:
        if i % 2 == 0:
            str_cmd_info += elem + ", "
            i += 1
        else:
            str_cmd_info += elem + " = "
            i += 1
    for elem in mg_game_constants.USER_QUIT_CMD:
        if elem == mg_game_constants.USER_QUIT_CMD[len(mg_game_constants.USER_QUIT_CMD)-1]:  # last element
            str_cmd_info += elem + ")"
        else:
            str_cmd_info += elem + " = "

    return input(f"Which direction Mac Gyver should go in the maze ?\n{str_cmd_info} --> ")


def check_user_move_entry(user_move_entry):
    """
    :param user_move_entry: (str) User entry
    :return: (bool) True if the :param user_move_cmd is valid (i.e belongs by lists (see mg_game_constants file)
    """
    assert(type(user_move_entry) is str)

    return (user_move_entry in mg_game_constants.USER_MOVE_CMD) or (user_move_entry in mg_game_constants.USER_QUIT_CMD)


def impossible_move_msg(code):
    """
    :param code: (int) Corresponding to the reason why the movement is impossible (1 = maze edge ; 2 = wall)
    :return: (None) Display the message
    """
    assert(type(code) is int or code == 1 or code == 2)

    if code == 1:
        print("----------------------------------------------------------------------------------\n"
              "/!!!\ You are going to fall out the maze... and teleporting is not possible /!!!\\\n"
              "Please try a different direction...\n"
              "----------------------------------------------------------------------------------")
    elif code == 2:
        print("------------------------------------------------------------------------------------\n"
              "/!!!\ You are going to bang into a wall... and crossing walls is not possible /!!!\\\n"
              "Please try a different direction...\n"
              "------------------------------------------------------------------------------------")


def is_wall(maze_list, maze_square_id):
    """
    :param maze_list: (list) maze (int)
    :param maze_square_id: (int) a maze square index
    :return: (bool) True if :param maze_square_id correspond to a wall
    """
    assert(type(maze_list) is list)
    assert(type(maze_square_id) is int)

    return maze_list[maze_square_id] == 1


def is_out_of_maze(move_cmd, mg_pos_id):
    """
    :param move_cmd: (str) MG movement asked by user
    :param mg_pos_id: (int) the current maze index (where MG is)
    :return: (bool) True if the :param mg_pos corresponds to a maze edge
            and if the :param move_cmd is the same direction
    """
    assert(type(move_cmd) is str)
    assert(type(mg_pos_id) is int)

    if move_cmd in ["north", "n"]:  # north move <=> -15 squares
        return mg_pos_id < (mg_game_constants.MAZE_NB_SQUARE_PER_SIDE-1)  # MG is on the northern edge of the maze
    elif move_cmd in ["south", "s"]:  # south move <=> +15 squares
        return mg_pos_id > (mg_game_constants.MAZE_NB_SQUARE_PER_SIDE**2) - 1 - mg_game_constants.MAZE_NB_SQUARE_PER_SIDE  # MG is on the southern edge of the maze
    elif move_cmd in ["west", "w"]:  # west move <=> -1 square
        return mg_pos_id % 15 == 0  # MG is on the western edge of the maze
    elif move_cmd in ["east", "e"]: # east move <=> +1 square
        return (mg_pos_id+1) % 15 == 0  # MG is on the eastern edge of the maze


def calculate_dest_id(mg_pos_id, move_cmd):
    """
    :param mg_pos_id: (int) the current maze index (where MG is)
    :param move_cmd: (str) MG movement asked by user
    :return: (int) the maze square index where MG will move
    """
    assert(type(mg_pos_id) is int)
    assert(type(move_cmd) is str)

    if move_cmd in ["north", "n"]:  # north move <=> -15 squares
        return mg_pos_id - 15
    elif move_cmd in ["south", "s"]:  # south move <=> +15 squares
        return mg_pos_id + 15
    elif move_cmd in ["west", "w"]:  # west move <=> -1 square
        return mg_pos_id - 1
    elif move_cmd in ["east", "e"]: # east move <=> +1 square
        return mg_pos_id + 1


def is_guardian_room(maze_list):
    """
    :param maze_list: (list) maze (int)
    :return: (bool) True if user has moved MG to the guardian's place
    """
    assert(type(maze_list) is list)

    return maze_list.count(3) == 0


def is_there_items_in_maze(maze_list):
    """
    :param maze_list: (list) maze (int)
    :return: (bool) True if there it at least one item remaining in the maze
    """
    assert(type(maze_list) is list)

    for item in mg_game_constants.ITEMS_INT_DICT.values():
        if maze_list.count(item) != 0:
            return True

    return False


def is_game_failure(maze_list):
    """
    Called only if MG has reached the guardian room (end of while is_guardian() loop in playing_game())
    :param maze_list: (list) maze (int)
    :return: (bool) True
    """
    assert(type(maze_list) is list)

    return is_there_items_in_maze(maze_list)


def move_mg(ready_maze_list, move_cmd):
    """
    :param ready_maze_list: (list) ready maze (final version = items + characters placed)
    :param move_cmd: (str) a moving text command entered by the user :
                - "north" ou "n"
                - "south" ou "s"
                - "east" ou "e"
                - "west" ou "w"
    :return: (list) maze modified (or not if is_out_of_maze() or is_wall() return (bool) False)
    """
    assert(type(ready_maze_list) is list)
    assert(type(move_cmd) is str)

    # get the current MG position in maze (remember the Mac Gyver integer = 2)
    curr_mg_id = ready_maze_list.index(2)
    dest_mg_id = calculate_dest_id(curr_mg_id, move_cmd)
    if is_out_of_maze(move_cmd, curr_mg_id):
        impossible_move_msg(1)
    elif is_wall(ready_maze_list, dest_mg_id):
        impossible_move_msg(2)
    else:
        ready_maze_list[curr_mg_id] = 0
        ready_maze_list[dest_mg_id] = 2
    return ready_maze_list


def end_of_game_msg(code):
    """
    :param code: (int) Corresponding to the game outcoming (0 = loose ; 1 = win)
    :return: (None) Only display
    """
    assert(type(code) is int or code == 0 or code == 1)

    if code == 0:
        print("You loose ! You have met the Guardian but you did not found the 3 items ☹")
    elif code == 1:
        print("Well Done !!! ☹\nYou have got the guardian to sleep with the sleeping needle "
              "make with the 3 items founded !")


""" ================= Main ================= """


def initializing_game():
    # Loading the entire maze in a list :
    maze_list = maze_file_loading("Labyrinthe_ascii_OK.txt")
    # Keep one in two square (for future treatments) :
    one_element_in_two_list(maze_list)
    # Turn character into integer (likewise for future treatments) :
    char_to_int_maze_list(maze_list)
    # Extract index of the maze hallway squares :
    # maze_hallway_id_list = maze_hallway_index_list(maze_list)
    # Randomly extract 3 index from the maze hallway index
    # stored in a dict and used to place the 3 items in the maze :
    # items_index_dict = items_random_location(maze_hallway_id_list)
    # items_all_info_dict = store_items_all_info_dict(items_index_dict)
    # Put items in the 3 maze squares randomly chosen :
    place_items_maze(maze_list)
    return maze_list


def playing_game(maze_list):
    """
    :param maze_list:
    :return:
    """
    assert(type(maze_list) is list)

    # Display game rules and the maze :
    display_game_rules(maze_list)

    while not is_guardian_room(maze_list):
        # ask user for entering command :
        curr_user_move_cmd = ask_user_move_input()
        # check that user enter a valid command
        while not check_user_move_entry(curr_user_move_cmd):
            curr_user_move_cmd = ask_user_move_input()

        # User asks for leaving the game :
        if curr_user_move_cmd in mg_game_constants.USER_QUIT_CMD:
            print("You have asked to quit the game...")
            quit()
        # User progresses in the maze :
        else:
            move_mg(maze_list, curr_user_move_cmd)
            maze_display(maze_list)

    if is_game_failure(maze_list):
        end_of_game_msg(0)
    else:
        end_of_game_msg(1)


curr_maze_list = initializing_game()
playing_game(curr_maze_list)



