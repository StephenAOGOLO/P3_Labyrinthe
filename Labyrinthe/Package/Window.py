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

    def __repr__(self):
        """
        Show the feature of a window
        :return:message
        """
        message = "*****\nType: {}\nwidth: '{}'\nheight = {}\ncolor (RGB) = {}\n*****"\
            .format(type(self), self.width, self.height, self.rgb_colors)
        return message


def color_window(window, color=BACKGROUND):
    """

    :param window:
    :param color:
    :return:
    """
    colored_window = window.fill(color)
    return colored_window
