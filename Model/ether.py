from Model.item import Item


class Ether(Item):
    def __repr__(self):
        return "EE"

    # Allows the list.count(Ether())
    def __eq__(self, other):
        return isinstance(other, Ether)
