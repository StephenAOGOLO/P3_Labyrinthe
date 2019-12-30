"""
Welcome to the window module, 'window.py'.
This class handles the graphical creation and the display of the window which contains the game.
It is composed of one class, four methods and one function.
"""
# -*- coding: utf-8 -*-
import pygame as pg


class Window:
    """
    This class manage pygame window.
    """

    def __init__(self, width, height):
        """
        the instance needs dimension to be created.
        :param width:
        :param height:
        """
        self.width = width
        self.height = height
        self.picture = pg.image.load("./Package/Pictures/wall/pyramid_floor.png")

    def display_window(self):
        """
        This method displays the window with the dimension given during creation.
        :return:
        """
        displayed_window = pg.display.set_mode((self.width, self.height))
        return displayed_window

    def set_background_on(self, window, var_x, var_y):
        """
        This method is called to set the floor of the maze.
        :param window:
        :param var_x:
        :param var_y:
        :return:
        """
        picture_set = window.blit(self.picture, (var_x, var_y))
        return picture_set

    def game_over(self, status, window_displayed):
        """
        This method displays 'mission passed' after win or 'wasted' after lose.
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

