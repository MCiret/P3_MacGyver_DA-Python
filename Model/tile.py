import pygame


class Tile:
    """
    A tile = a room in the maze. It is the base class for all different
    elements forming the maze (characters, walls, hallways and items).
    """

    def __init__(self, picture=None):
        """
        :param picture: (pygame.Surface) picture representing each room in the
        maze. This picture side size (pixel) should be the same than
        SPRITE_SIZE in constantes.py.
        """
        self.picture = picture

    def draw_tile(self, window, x, y):
        """
        Blits tile picture to the main pygame window.
        :param window: (pygame.Surface)
        :param x: (int) position coordinate
        :param y: (int) position coordinate
        """
        pict_pos = self.picture.get_rect()
        pict_pos = pict_pos.move(x, y)
        window.blit(self.picture, pict_pos)
