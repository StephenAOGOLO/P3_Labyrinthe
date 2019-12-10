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
        self.picture = pg.image.load("./Pictures/Wall/block_background.png")

    def display_window(self):
        """

        :return:
        """
        displayed_window = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        return displayed_window

    def __repr__(self):
        """
        Show the feature of a window
        :return:message
        """
        message = "*****\nType: {}\nwidth = {}\nheight = {}\n" \
                  "color (RGB) = {}\n*****".format(type(self), self.width, self.height, self.rgb_colors)
        return message

    def set_on_window(self, window, element1, element2):
        """
        This function need to be fix. There is no attribute used into this funtion.
        :param window:
        :param element1:
        :param element2:
        :return:
        """
        return window.blit(element1, element2)

    def load_element_picture(self,):
        """

        :return:
        """
        avatar = pg.image.load(self.picture)
        return avatar

    def set_background_on(self, window, x, y):
        picture_set = window.blit(self.picture, (x, y))
        return picture_set


def color_window(window, color=BACKGROUND):
    """

    :param window:
    :param color:
    :return:
    """
    colored_window = window.fill(color)
    return colored_window


