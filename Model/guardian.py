from Model.character import Character


class Guardian(Character):
    """
    Fixed tile in the maze. User has to move MacGyver tile to reach this
    Guardian tile.
    """

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "GD"

    # Allows the list.index/count(Guardian())
    def __eq__(self, other):
        return isinstance(other, Guardian)
