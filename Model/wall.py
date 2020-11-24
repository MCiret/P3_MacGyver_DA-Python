from Model.tile import Tile


class Wall(Tile):
    """
    A wall in the maze.
    """

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "██"
