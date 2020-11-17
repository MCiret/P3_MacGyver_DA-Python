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

ASCII_TO_PICTURE_DICT = {
    '█': "Wall", # value = picture
    '░': "Hallway",
    'M': "MacGyver",
    'G': "Guardian",
    'E': "Ether",
    'T': "Tube",
    'N': "Needle"
}

ITEMS_LIST = ["Ether", "Tube", "Needle"]

MAZE_NB_TILES_PER_SIDE = 15

USER_INPUT_CMD = {'north': -15, 'n': -15,
                  'south': 15, 's': 15,
                  'east': -1, 'e': -1,
                  'west': 1, 'w': 1,
                  'quit': 0, 'q': 0}
