from Model.character import Character


class MacGyver(Character):
    def __repr__(self):
        return "MG"

    # Allows the list.index(MacGyver())
    def __eq__(self, other):
        return isinstance(other, MacGyver)