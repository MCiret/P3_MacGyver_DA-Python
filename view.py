import constantes as cste


class View:
    @staticmethod
    def maze_display(maze_list):
        """
        Display the maze with ascii character (using the __repr__() method overriding)
        :param maze_list: (list) maze tiles (class)
        """
        for i, elem in enumerate(maze_list):
            if (i+1) % cste.MAZE_NB_TILES_PER_SIDE == 0:
                print(elem)

            else:
                print(elem, end="")

    @staticmethod
    def display_game_rules():
        """
        :return: (None) Displays the game rules
        """
        print(f"Welcome in this game !\nMac Gyver (MG) is lost in a maze... Could you help him to escape ?\n"
              f"The only way to escape from the maze is reaching and neutralizing the Guardian (GD).\n"
              f"For that you have to gather 3 items which are hidden in different tiles in the maze :\n"
              f"- Ether (EE)\n- Tube (plastic) (TT)\n- Needle (NN)\n=> As we know him, Mac Gyver should "
              f"be able to make something...\n"
              f"Have fun !!")

    @staticmethod
    def user_input_ask_msg():
        """
        Asks user to type a command (among the valid list) to move Mac Gyver or to quit the game
        :return: (str) The (not already checked) command entered by user
        """
        i = 1
        str_cmd_info = "("
        for input_cmd_key in cste.USER_INPUT_CMD:
            if i == len(cste.USER_INPUT_CMD):
                str_cmd_info += input_cmd_key + ")"
            elif i % 2 == 0:
                str_cmd_info += input_cmd_key + ", "
                i += 1
            else:
                str_cmd_info += input_cmd_key + " = "
                i += 1

        return input(f"Direction to move MacGyver in the maze ?\n{str_cmd_info} --> ")

    @staticmethod
    def wrong_user_entry_msg():
        """
        :return: (None) Display the message
        """
        print("The command was not found...")

    @staticmethod
    def quitting_game_msg():
        """
        :return: (None) Display the message
        """
        print("You have asked to quit the game...")

    @staticmethod
    def impossible_move_msg(code):
        """
        :param code: (int) Corresponding to the reason why the movement is impossible (1 = maze edge ; 2 = wall)
        :return: (None) Display the message
        """
        assert(type(code) is int or code == 1 or code == 2)

        if code == 1:
            print("------------------------------------------------------------------------------\n"
                  "/!!!\\ You are going to fall out the maze... teleporting is not possible /!!!\\\n"
                  "Please try a different direction...\n"
                  "------------------------------------------------------------------------------")
        elif code == 2:
            print("------------------------------------------------------------------------------------\n"
                  "/!!!\\ You are going to bang into a wall... and crossing walls is not possible /!!!\\\n"
                  "Please try a different direction...\n"
                  "------------------------------------------------------------------------------------")

    @staticmethod
    def end_of_game_msg(code):
        """
        :param code: (int) Corresponding to the game outcoming (0 = loose ; 1 = win)
        :return: (None) Only display
        """
        assert(type(code) is int and (code == 0 or code == 1))

        if code == 0:
            print("You loose ! You have met the Guardian but you did not found the 3 items ☹")
        elif code == 1:
            print("Well Done !!! ☹\nYou have slept the guardian using an anesthetic"
                  "made with the 3 items founded !")
