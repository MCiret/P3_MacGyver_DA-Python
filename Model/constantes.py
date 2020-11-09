# dict use by model.py to match maze ascii character and class when loading the maze
ASCII_TO_CLASS_DICT = {
    '█': "Wall",
    '░': "Hallway",
    'M': "MacGyver",
    'G': "Guardian",
    'E': "Ether",
    'T': "Tube",
    'N': "Needle"
}

ITEMS_LIST = ["Ether", "Tube", "Needle"]

MAZE_NB_ROOMS_PER_SIDE = 15

USER_MOVE_CMD = ['north', 'n', 'south', 's', 'east', 'e', 'west', 'w']
USER_QUIT_CMD = ['quit', 'q']
