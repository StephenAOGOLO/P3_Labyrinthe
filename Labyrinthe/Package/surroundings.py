"""
Welcome to the surroundings module, 'surroundings.py'.
This module is used to create each piece of wall into the game.
It contains only one class with two methods.
"""
import pygame as pg


class SurroundingsSprite(pg.sprite.Sprite):
    """
    This class is a concrete class of Sprite which is the base class.
    This class manage each piece of wall as pygame sprite's.
    """
    def __init__(self, color=(0, 0, 0), width=50, height=50):
        super(SurroundingsSprite, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_position(self, var_x, var_y):
        """
        This method is called to set the instance on the window.
        The parameters are integers.
        :param var_x:
        :param var_y:
        :return:
        """
        self.rect.x = var_x
        self.rect.y = var_y

    def set_image(self, filename=None):
        """
        This method is use to change the picture of the instance.
        :param filename:
        :return:
        """
        if filename is not None:
            self.image = pg.image.load(filename)
