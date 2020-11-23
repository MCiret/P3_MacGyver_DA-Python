import pygame


class Tile:
    """
    Maze = 15x15 <=> 225 tiles
    """

    def __init__(self, picture=None):
        self.picture = picture

    def draw_tile(self, window, x, y):
        pict_pos = self.picture.get_rect()
        pict_pos = pict_pos.move(x, y)
        window.blit(self.picture, pict_pos)
