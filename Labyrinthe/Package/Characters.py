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

    def start_move_avatar(self, event):
        """

        :param event:
        :return:
        """
        mc_gyver_move_x = 0
        mc_gyver_move_y = 0
        arrow_key = pg.key.get_pressed()
        if event.type == pg.KEYUP:
            pass
        if event.type == pg.KEYDOWN:
            if arrow_key[pg.K_UP]:
                mc_gyver_move_y = -0.1
                mc_gyver_move_x = 0
            elif arrow_key[pg.K_DOWN]:
                mc_gyver_move_y = 0.1
                mc_gyver_move_x = 0
            elif arrow_key[pg.K_RIGHT]:
                mc_gyver_move_x = 0.1
                mc_gyver_move_y = 0
            elif arrow_key[pg.K_LEFT]:
                mc_gyver_move_x = -0.1
                mc_gyver_move_y = 0
        self.posx += mc_gyver_move_x
        self.posy += mc_gyver_move_y

    def stop_move_avatar(self, event, limit_x, limit_y):
        """

        :return:
        """
        arrow_key = pg.key.get_pressed()
        if event.type == pg.KEYDOWN:
            if arrow_key[pg.K_UP]:
                self.posy = 0
            elif arrow_key[pg.K_DOWN]:
                self.posy = limit_y
            elif arrow_key[pg.K_RIGHT]:
                self.posx = limit_x
            elif arrow_key[pg.K_LEFT]:
                self.posx = 0
