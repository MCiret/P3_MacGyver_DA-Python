from .tile import Tile


class Item(Tile):
    """
    Base class of Ether, Tube and Needle classes. Each Item is instanced once
    and randomly put in the maze. User has to find them all before reaching
    Guardian tile.
    """
    pass
