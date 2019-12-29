"""
Welcome to the surroundings module, 'surroundings.py'.
This module is used to create each piece of wall into the game.
It contains only one class with two methods.
"""
import pygame as pg


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
