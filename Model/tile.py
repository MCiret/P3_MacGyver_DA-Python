import pictures_manager as pm


class Tile:
    """
    A tile = a room in the maze. It is the base class for all different
    elements forming the maze (characters, walls, hallways and items).
    """

    def __init__(self):
        self.picture = ""

    def draw_tile(self, window, x, y):
        """
        Blit tile picture to the main pygame window.
        :param window: (pygame.Surface)
        :param x: (int) position coordinate
        :param y: (int) position coordinate
        """
        window.blit(self.picture, (x, y))

