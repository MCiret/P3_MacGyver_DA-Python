from Model.item import Item
import pictures_manager as pm


class Ether(Item):
    """
    One of the items Tiles that user has to find.
    """

    def __init__(self):
        super().__init__()
        self.picture = pm.PictureManager.get_class_picture("Ether")

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "EE"

    # Allows the list.count(Ether())
    def __eq__(self, other):
        return isinstance(other, Ether)
