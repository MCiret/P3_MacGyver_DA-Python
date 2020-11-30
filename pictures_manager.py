import constantes as cste
import pygame


class PictureManager:
    """
    To manage all the pictures used in the program.
    Pictures are loaded once in a class attribute dictionary.
    """

    LOADED_PICTURES_DICT = {}

    @classmethod
    def picture_dict_filling(cls):
        for str_key in cste.PICTURES_PATH_DICT:
            cls.LOADED_PICTURES_DICT[str_key] = \
                pygame.image.load(cste.PICTURES_PATH_DICT[str_key])

    @classmethod
    def get_class_picture(cls, class_name):
        assert(type(class_name) is str)

        return cls.LOADED_PICTURES_DICT[class_name]
