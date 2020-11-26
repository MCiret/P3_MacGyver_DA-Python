"""
Game : Help Mac Gyver to escape from a maze !
Author : Marie Ciret
Date : 24 Novembre 2020
    Graphical simple 2D game : use arrow keys to moves Mac Gyver in a maze
formed with sprites. MG has to collect items and reach the guardian spot to win
the game.
               ================================================
    The program is object oriented and structured with the design pattern
Model-View-Controller.
               ================================================
- Run : main.py
- Program files : model.py, view.py, control.py, constantes.py.
In Model directory : tile.py, wall.py, hallway.py, character.py, guardian.py,
macgyver.py, item.py, needle.py, tube.py, ether.py.
In Resources directory : Maze_lvl1.txt, my_tile_anesthetic.png,
my_tile_ether.png, my_tile_guardian.png, my_tile_hallway.png,
my_tile_macgyver.png, my_tile_needle.png, my_tile_plastic_tube.png
my_tile_wall.png
- Requirements : python module pygame (2.0.0)
"""

import control as c


def main():
    c.Control.game_playing()


if __name__ == "__main__":
    main()
