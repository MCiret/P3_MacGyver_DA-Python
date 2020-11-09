from model import Maze
from View.view import View


def main():
    curr_maze_list = []
    Maze.load_from_file(curr_maze_list)
    Maze.add_items(Maze.rand_items_pos(Maze.hallway_index_list(curr_maze_list)), curr_maze_list)
    View.maze_display(curr_maze_list)
    View.user_input_to_int()


main()
