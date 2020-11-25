MAZE_LVL1 = "Resources/Maze_lvl1.txt"
NB_SPRITE_SIDE = 15  # number of tiles per maze side
SPRITE_SIZE = 30  # number of pixel per tile side
MAZE_SIDE_SIZE = NB_SPRITE_SIDE * SPRITE_SIZE
WINDOW_WIDTH = MAZE_SIDE_SIZE + 150  # main pygame window pixel width
WINDOW_HEIGHT = MAZE_SIDE_SIZE + 150  # main pygame window pixel eight
WINDOW_TITLE = "Game : Help MacGyver to escape from a maze !"

# Dict used to load maze instances list from text file.
# To instances from a string : using the dict returned by the built-in
# function globals() (classes have to be imported, see model.py) :
MAZE_ASCII_TO_CLASS_DICT = {'█': "Wall",
                            '░': "Hallway",
                            'M': "MacGyver",
                            'G': "Guardian"}

# Dict used to load maze tiles pictures from
# ascii characters in the loaded text file :
MAZE_ASCII_TO_PICTURE_PATH_DICT = {'█': "Resources/my_tile_wall.png",
                                   '░': "Resources/my_tile_hallway.png",
                                   'M': "Resources/my_tile_macgyver.png",
                                   'G': "Resources/my_tile_guardian.png"}

# Dict used to load maze tiles pictures from
# ascii characters in the loaded text file :
ITEMS_PICTURES_PATH_DICT = {"Ether": "Resources/my_tile_ether.png",
                            "Tube": "Resources/my_tile_plastic_tube.png",
                            "Needle": "Resources/my_tile_needle.png"}

OTHER_PICTURES_PATH_DICT = {"All found items": "Resources/my_tile_anesthetic.png",
                            "Move cmd": "Resources/move_cmd_picture.png"}

USER_INPUT_CMD = {'north': -15, 'n': -15,
                  'south': 15, 's': 15,
                  'east': 1, 'e': 1,
                  'west': -1, 'w': -1}
