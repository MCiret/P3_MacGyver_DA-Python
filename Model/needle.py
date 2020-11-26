from Model.item import Item


class Needle(Item):
    """
    One of the items Tiles that user has to find.
    """

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "NN"

    # Allows the list.count(Needle())
    def __eq__(self, other):
        return isinstance(other, Needle)
