import pygame as pg

STARTX = 150
STARTY = 200


class Characters:
    """
    Building in progress...
    """

    def __init__(self, name, file_png, posx=STARTX, posy=STARTY):
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

    def __repr__(self):
        """
        Show the feature of a character
        :return:message
        """
        message = "*****\nType: {}\nCharacter: {}\npath picture: '{}'\nposition x = {}\nposition y = {}\n*****"\
            .format(type(self), self.name, self.picture, self.posx, self.posy)
        return message

    def display_character(self):
        """

        :return:
        """
        avatar = pg.image.load(self.picture)
        return avatar

    def load_character_picture(self):
        """

        :return:
        """
        avatar = pg.image.load(self.picture)
        return avatar

    def set_avatar(self, avatar, window):
        """

        :param avatar:
        :param window:
        :return:
        """
        avatar_set = window.blit(avatar, (self.posx, self.posy))
        return avatar_set

    def move_avatar_vertical(self, new_x, new_y):
        """

        :param new_x:
        :param new_y:
        :return:
        """
        self.posx = new_x
        self.posy = new_y
        return self.posy
