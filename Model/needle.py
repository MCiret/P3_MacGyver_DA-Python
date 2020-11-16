from Model.item import Item


class Needle(Item):
    def __repr__(self):
        return "NN"

    # Allows the list.count(Needle())
    def __eq__(self, other):
        return isinstance(other, Needle)
