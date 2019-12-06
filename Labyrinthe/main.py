# coding: utf-8

import pygame as pg
import configparser as cp
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character


class Settings:
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        self.file_ini = ".\\Package\\settings.ini"
        self.all_sections_file = self.get_all_sections_file_ini()

    def get_data_file_ini(self, section):
        """
        This function picks all data of a specified section from 'settings.ini'.


        :param section:
        :return data:
        """
        data = {}
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        for j in config.options(section):
            data[str(j)] = str(config.get(section, j))
        return data

    def get_option_file_ini(self, section):
        """
        This function picks all options of a specified section from 'settings.ini'.

        :param section:
        :return config.options(section):
        """
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        return config.options(section)

    def get_all_sections_file_ini(self):
        """
        This function picks all sections from 'settings.ini'.

        :return:
        """
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        return config.sections()

    def get_particular_sections(self, pattern):
        list_particular_section = []
        for section in self.all_sections_file:
            if pattern in section:
                list_particular_section.append(section)
        return list_particular_section


class SettingsWindow(Settings):
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("window_")
        self.data_file = self.get_data_file_ini("window_main")
        self.all_sections = self.get_all_sections_file_ini()


class SettingsCharacter(Settings):
    """
    Building in progress...
    """
    CREATION = 0

    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("character_")
        self.characters = self.sort_all_characters()
        if self.CREATION == 0:
            self.data_file = self.get_data_file_ini("character_mac_gyver")
        elif self.CREATION == 1:
            self.data_file = self.get_data_file_ini("character_watchman")

    def __repr__(self):
        """
        Show the feature of a window
        :return:message
        """
        message = "*****\nType: {}\nsections: {}\n*****"\
            .format(type(self), [item for item in self.characters.items()])
        return message

    def sort_all_characters(self):

        dict_characters = {}
        mac_gyver = "mac_gyver"
        watchman = "watchman"
        for section in self.particular_sections:
            if str(section[10:]) == mac_gyver:
                dict_characters[mac_gyver] = self.get_data_file_ini(section)
            elif str(section[10:]) == watchman:
                dict_characters[watchman] = self.get_data_file_ini(section)
        return dict_characters


class SettingsObject(Settings):
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("object_")
        self.data_file = self.get_data_file_ini("window_main")


def in_progress_main():
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """

    watchman_settings = SettingsCharacter()
    watchman_settings = watchman_settings.data_file
    mc_gyver_settings = SettingsCharacter()
    mc_gyver_settings = mc_gyver_settings.data_file
    window_settings = SettingsWindow()
    window_base = Wd.Window(int(window_settings.data_file["window_width"]),
                            int(window_settings.data_file["window_height"]))
    mc_gyver = Character.Characters(mc_gyver_settings["name"], mc_gyver_settings["path_picture"],
                                    mc_gyver_settings["startx"], mc_gyver_settings["starty"])
    watchman = Character.Characters(watchman_settings["name"], watchman_settings["path_picture"],
                                    watchman_settings["startx"], watchman_settings["starty"])
    mc_gyver_avatar = mc_gyver.load_character_picture()
    watchman_avatar = watchman.load_character_picture()
    surface = window_base.display_window()
    Wd.color_window(surface)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        pg.display.update()
    pg.quit()


def main():
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    mc_gyver_x = 150
    mc_gyver_y = 200
    mc_gyver_move_x = 0
    mc_gyver_move_y = 0
    window_base = Wd.Window(640, 480)
    mc_gyver = Character.Characters("Mac Gyver", "./Package/Pictures/MacGyver.png", mc_gyver_x, mc_gyver_y)
    watchman = Character.Characters("WatchMan", "./Package/Pictures/Gardien.png", 300, 200)
    mc_gyver_avatar = mc_gyver.load_character_picture()
    watchman_avatar = watchman.load_character_picture()
    surface = window_base.display_window()
    Wd.color_window(surface)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
            if event.type == pg.KEYDOWN:
                pass
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    mc_gyver_move_y = -5
                    mc_gyver_move_x = 0
                if event.key == pg.K_DOWN:
                    mc_gyver_move_y = 5
                    mc_gyver_move_x = 0
                mc_gyver.posy += mc_gyver_move_y
                mc_gyver.posx += mc_gyver_move_x
                if event.key == pg.K_RIGHT:
                    mc_gyver_move_x = 5
                    mc_gyver_move_y = 0
                if event.key == pg.K_LEFT:
                    mc_gyver_move_x = -5
                    mc_gyver_move_y = 0
                mc_gyver.posx += mc_gyver_move_x
                mc_gyver.posy += mc_gyver_move_y
        mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        pg.display.update()
    pg.quit()


if __name__ == "__main__":
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    main()
