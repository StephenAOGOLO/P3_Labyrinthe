# coding: utf-8

import pygame as pg
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character


def main():
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    window_base = Wd.Window(640, 480)
    mc_gyver = Character.Characters("Mac Gyver", "./Package/Pictures/MacGyver.png", 150, 200)
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
        mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        pg.display.update()
    pg.quit()









if __name__ =="__main__":
    main()