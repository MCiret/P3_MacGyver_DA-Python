from Model.item import Item
import pictures_manager as pm


class Needle(Item):
    """
    One of the items Tiles that user has to find.
    """

    def __init__(self):
        super().__init__(pm.PictureManager.get_class_picture("Needle"))

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "NN"

    # Allows the list.count(Needle())
    def __eq__(self, other):
        return isinstance(other, Needle)
