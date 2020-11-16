import view as v
import control as c


def main():
    curr_maze_list = []
    c.Control.initialize_game(curr_maze_list)
    c.Control.game_playing(curr_maze_list)


main()
