from Model.character import Character
import pictures_manager as pm


class Guardian(Character):
    """
    Fixed tile in the maze. User has to move MacGyver tile to reach this
    Guardian tile.
    """

    def __init__(self):
        super().__init__()
        self.picture = pm.PictureManager.get_class_picture("Guardian")

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "GD"

    # Allows the list.index/count(Guardian())
    def __eq__(self, other):
        return isinstance(other, Guardian)
