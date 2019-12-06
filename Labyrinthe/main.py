# coding: utf-8

import pygame as Pg
import configparser as cp
import Labyrinthe.Package.Mazes as Maze
import Labyrinthe.Package.Options as Opt
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character


def in_progress_main():
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """

    watchman_settings = Opt.SettingsCharacter()
    watchman_settings = watchman_settings.data_file
    mc_gyver_settings = Opt.SettingsCharacter()
    mc_gyver_settings = mc_gyver_settings.data_file
    window_settings = Opt.SettingsWindow()
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
        for event in Pg.event.get():
            if event.type == Pg.QUIT:
                launched = False
        mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        Pg.display.update()
    Pg.quit()


def message(text, area, surface):
    pop_font = Pg.font.Font("./Package/Fonts/AGENCYR.TTF", 20)
    pop_area, pop_rect = custom_message(text, pop_font)
    pop_rect.center = 320, 240
    area.set_on_window(surface, pop_area, pop_rect)


def custom_message(text, font):
    text_area = font.render(text, True, (255, 255, 255))
    return text_area, text_area.get_rect()


def main():
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    Pg.init()
    Pg.display.set_caption("Aidez MacGyver à s'échapper !")
    mc_gyver_x = 1
    mc_gyver_y = 1
    window_x = 640
    window_y = 480
    window_base = Wd.Window(window_x, window_y)
    mc_gyver = Character.Characters("Mac Gyver", "./Package/Pictures/MacGyver.png", mc_gyver_x, mc_gyver_y)
    watchman = Character.Characters("WatchMan", "./Package/Pictures/Gardien.png", 300, 200)
    mc_gyver_avatar = mc_gyver.load_character_picture()
    watchman_avatar = watchman.load_character_picture()
    surface = window_base.display_window()
    launched = True
    while launched:
        for event in Pg.event.get():
            if event.type == Pg.QUIT:
                launched = False
        mc_gyver.start_move_avatar(event)
        Wd.color_window(surface)
        mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        if mc_gyver.posy > window_y - 50 or mc_gyver.posy < 0:
            message("Aie !!!! un mur !!!", window_base, surface)
        if mc_gyver.posx > window_x - 50 or mc_gyver.posx < 0:
            message("Aie !!!! un mur !!!", window_base, surface)
        Pg.display.update()
    Pg.quit()

    # This following block have to be fix first before implementation
    # the_maze = Maze.Maze()
    # event = the_maze.run_instance()
    # mc_gyver.move_avatar(event)
    # mc_gyver.set_avatar(mc_gyver_avatar, surface)
    # watchman.set_avatar(watchman_avatar, surface)
    # Pg.display.update()


if __name__ == "__main__":
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    main()
