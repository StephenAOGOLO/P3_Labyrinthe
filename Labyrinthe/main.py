# coding: utf-8

import pygame as Pg
import configparser as cp
import Labyrinthe.Package.Mazes as Maze
import Labyrinthe.Package.Options as Opt
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character
import Labyrinthe.Package.Surroundings as Sd


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
    brown_block_settings = Opt.SettingsSurroundings()
    brown_block_settings = brown_block_settings.data_file
    window_base = Wd.Window(int(window_settings.data_file["window_width"]),
                            int(window_settings.data_file["window_height"]))
    mc_gyver = Character.Characters(mc_gyver_settings["name"], mc_gyver_settings["path_picture"],
                                    mc_gyver_settings["startx"], mc_gyver_settings["starty"])
    watchman = Character.Characters(watchman_settings["name"], watchman_settings["path_picture"],
                                    watchman_settings["startx"], watchman_settings["starty"])
    brown_block = Sd.SurroundingsElement(brown_block_settings["name"], brown_block_settings["path_picture"],
                                         brown_block_settings["width"], brown_block_settings["height"])
    mc_gyver_avatar = mc_gyver.load_character_picture()
    watchman_avatar = watchman.load_character_picture()
    brown_block = brown_block.load_element_picture()
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
    clock = Pg.time.Clock()
    fps = 60
    window_x = 640
    window_y = 480
    mc_gyver_x = window_x/2
    mc_gyver_y = window_y/2
    watchman_x = window_x-50
    watchman_y = 20
    # needle_x = 10
    # needle_y = 10
    # tube_x =  10
    # tube_y = watchman_y + 10
    # ether_x = window_x + 10
    # ether_y = window_y + 10
    limit_window_x = window_x - 50
    limit_window_y = window_y - 50
    brown_block_x = 1
    brown_block_y = 1
    window_base = Wd.Window(window_x, window_y)
    mc_gyver = Character.Characters("Mac Gyver", "./Package/Pictures/MacGyver.png", mc_gyver_x, mc_gyver_y)
    watchman = Character.Characters("WatchMan", "./Package/Pictures/Gardien.png", watchman_x, watchman_y)
    # needle = Sd.SurroundingsElement("Needle", "./Package/Pictures/aiguille.png", needle_x, needle_y)
    # tube = Sd.SurroundingsElement("Tube", "./Package/Pictures/tube_plastique.png", tube_x, tube_y)
    # ether = Sd.SurroundingsElement("Ether", "./Package/Pictures/ether.png", ether_x, ether_y)
    brown_block = Sd.SurroundingsElement("Brown_Block", "./Package/Pictures/brown_block.png",
                                         brown_block_x, brown_block_y)
    mc_gyver_avatar = mc_gyver.load_character_picture()
    watchman_avatar = watchman.load_character_picture()
    brown_block_picture = brown_block.load_element_picture()
    # needle_picture = needle.load_element_picture()
    # tube_picture = tube.load_element_picture()
    # ether_picture = ether.load_element_picture()
    surface = window_base.display_window()
    launched = True
    while launched:
        for event in Pg.event.get():
            if event.type == Pg.QUIT:
                launched = False
        mc_gyver.start_move_avatar(event)
        Wd.color_window(surface)
        brown_block.initialize_landscape(brown_block_picture, surface, window_base)
        mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        # needle.set_element(needle_picture, surface)
        # tube.set_element(tube_picture, surface)
        # ether.set_element(ether_picture, surface)
        if mc_gyver.posy > limit_window_y or mc_gyver.posy < 0:
            message("Aie !!!! un mur !!!", window_base, surface)
            mc_gyver.stop_move_avatar(event, limit_window_x, limit_window_y)
        if mc_gyver.posx > limit_window_x or mc_gyver.posx < 0:
            message("Aie !!!! un mur !!!", window_base, surface)
            mc_gyver.stop_move_avatar(event, limit_window_x, limit_window_y)
        clock.tick(fps)
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
