from Model.tile import Tile
import pictures_manager as pm


class Hallway(Tile):
    """
    Pathway (i.e not a wall) in the maze.
    """

    def __init__(self):
        super().__init__()
        self.picture = pm.PictureManager.get_class_picture("Hallway")

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "░░"
