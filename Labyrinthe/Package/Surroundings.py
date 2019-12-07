import pygame as pg

class SurroundingsElement:
    """
    Building in progress...
    """
    def __init__(self, name, file_png, posx, posy):
        """

        :param name:
        :param file_png:
        :param posx:
        :param posy:
        """
        self.name = name
        self.picture = file_png
        self.posx = posx
        self.posy = posy

    def load_element_picture(self):
        """

        :return:
        """
        picture_element = pg.image.load(self.picture)
        return picture_element

    def set_element(self, element, window):
        """

        :param avatar:
        :param window:
        :return:
        """
        element_set = window.blit(element, (self.posx, self.posy))
        return element_set