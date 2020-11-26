from Model.tile import Tile


class Hallway(Tile):
    """
    Pathway (i.e not a wall) in the maze.
    """

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "░░"
