MAZE_LVL1 = "Resources/Maze_lvl1.txt"
NB_SPRITE_SIDE = 15  # number of tiles per maze side
TAILLE_SPRITE = 30  # number of pixel per tile side
MAZE_SIDE_SIZE = NB_SPRITE_SIDE * TAILLE_SPRITE
WINDOW_WIDTH = MAZE_SIDE_SIZE + 100  # main pygame window pixel width
WINDOW_HEIGHT = MAZE_SIDE_SIZE + 150  # main pygame window pixel eight
WINDOW_TITLE = "Game : Help MacGyver to escape from a maze !"

ASCII_TO_CLASS_DICT = {
    '█': "Wall",
    '░': "Hallway",
    'M': "MacGyver",
    'G': "Guardian",
    'E': "Ether",
    'T': "Tube",
    'N': "Needle"
}

ITEMS_CHAR_LIST = ['E', 'T', 'N']

ASCII_TO_PICTURE_DICT = {
    '█': "Resources/my_tile_wall.png",  # value = path picture
    '░': "Resources/my_tile_hallway.png",
    'M': "Resources/my_tile_macgyver.png",
    'G': "Resources/my_tile_guardian.png",
    'E': "Resources/my_tile_ether.png",
    'T': "Resources/my_tile_plastic_tube.png",
    'N': "Resources/my_tile_needle.png",
    'A': "Resources/my_tile_anesthetic.png"
}

USER_INPUT_CMD = {'north': -15, 'n': -15,
                  'south': 15, 's': 15,
                  'east': 1, 'e': 1,
                  'west': -1, 'w': -1}
