from Model.character import Character


class Guardian(Character):
    def __repr__(self):
        return "GD"

    # Allows the list.index/count(Guardian())
    def __eq__(self, other):
        return isinstance(other, Guardian)
