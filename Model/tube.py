from Model.item import Item


class Tube(Item):
    def __repr__(self):
        return "TT"

    # Allows the list.count(Tube())
    def __eq__(self, other):
        return isinstance(other, Tube)
