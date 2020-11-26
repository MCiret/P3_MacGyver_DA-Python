from Model.character import Character


class MacGyver(Character):
    """
    Tile moved by user in the maze.
    """

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "MG"

    # Allows the list.index(MacGyver())
    def __eq__(self, other):
        return isinstance(other, MacGyver)
