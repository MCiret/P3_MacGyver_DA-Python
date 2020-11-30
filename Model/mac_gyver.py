from Model.character import Character
import pictures_manager as pm


class MacGyver(Character):
    """
    Tile moved by user in the maze.
    """

    def __init__(self):
        super().__init__(pm.PictureManager.get_class_picture("MacGyver"))

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "MG"

    # Allows the list.index(MacGyver())
    def __eq__(self, other):
        return isinstance(other, MacGyver)
