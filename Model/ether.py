from Model.item import Item


class Ether(Item):
    """
    One of the items Tiles that user has to find.
    """

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "EE"

    # Allows the list.count(Ether())
    def __eq__(self, other):
        return isinstance(other, Ether)
