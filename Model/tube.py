from Model.item import Item


class Tube(Item):
    """
    One of the items Tiles that user has to find.
    """

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "TT"

    # Allows the list.count(Tube())
    def __eq__(self, other):
        return isinstance(other, Tube)
