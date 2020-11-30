from Model.item import Item
import pictures_manager as pm


class Tube(Item):
    """
    One of the items Tiles that user has to find.
    """

    def __init__(self):
        super().__init__()
        self.picture = pm.PictureManager.get_class_picture("Tube")

    def __repr__(self):
        """
        To print the maze with ascii characters.
        """
        return "TT"

    # Allows the list.count(Tube())
    def __eq__(self, other):
        return isinstance(other, Tube)
