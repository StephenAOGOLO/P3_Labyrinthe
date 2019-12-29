"""hello"""
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

    def set_element(self, image, area):
        """

        :param image:
        :param area:
        :return:
        """
        element_set = area.blit(image, (self.posx, self.posy))
        return element_set


class SurroundingsSprite(pg.sprite.Sprite):
    """
    hello
    """
    def __init__(self, color=(0, 0, 0), width=50, height=50):
        super(SurroundingsSprite, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_position(self, var_x, var_y):
        """

        :param var_x:
        :param var_y:
        :return:
        """
        self.rect.x = var_x
        self.rect.y = var_y

    def set_image(self, filename=None):
        """

        :param filename:
        :return:
        """
        if filename is not None:
            self.image = pg.image.load(filename)
