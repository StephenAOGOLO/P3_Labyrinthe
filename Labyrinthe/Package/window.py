"""hello"""
# -*- coding: utf-8 -*-
import pygame as pg

BACKGROUND = (128, 128, 0)


class Window:
    """
    Building in progress...
    """

    def __init__(self, width, height):
        """

        :param width:
        :param height:
        """
        self.width = width
        self.height = height
        self.picture = pg.image.load("./Package/Pictures/wall/pyramid_floor.png")

    def display_window(self):
        """

        :return:
        """
        displayed_window = pg.display.set_mode((self.width, self.height))
        return displayed_window

    def load_element_picture(self,):
        """

        :return:
        """
        avatar = pg.image.load(self.picture)
        return avatar

    def set_background_on(self, window, var_x, var_y):
        """

        :param window:
        :param var_x:
        :param var_y:
        :return:
        """
        picture_set = window.blit(self.picture, (var_x, var_y))
        return picture_set

    def game_over(self, status, window_displayed):
        """

        :param status:
        :param window:
        :param window_displayed:
        :return:
        """
        if status is True:
            self.picture = pg.image.load("./Package/Pictures/Messages/mission_passed.png")
        if status is False:
            self.picture = pg.image.load("./Package/Pictures/Messages/wasted.jpg")
        self.set_background_on(window_displayed, 200, 200)
        pg.display.update()
        pg.time.wait(3000)


def color_window(window, color=BACKGROUND):
    """

    :param window:
    :param color:
    :return:
    """
    colored_window = window.fill(color)
    return colored_window
