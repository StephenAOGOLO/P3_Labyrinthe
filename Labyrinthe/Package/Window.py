import pygame as pg

pg.init()
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
        self.rgb_colors = BACKGROUND

    def display_window(self):
        """

        :return:
        """
        displayed_window = pg.display.set_mode((self.width, self.height))
        return displayed_window


def color_window(window, color=BACKGROUND):
    """

    :param window:
    :param color:
    :return:
    """
    colored_window = window.fill(color)
    return colored_window
