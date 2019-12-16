# coding: utf-8

import pygame as pg
import configparser as cp
import Labyrinthe.Package.Mazes as Maze
import Labyrinthe.Package.Options as Opt
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character
import Labyrinthe.Package.Surroundings as Sd


def first_main_off():
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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        pg.display.update()
    pg.quit()


def message(text, area, surface):
    pop_font = pg.font.Font("./Package/Fonts/AGENCYR.TTF", 20)
    pop_area, pop_rect = custom_message(text, pop_font)
    pop_rect.center = 320, 240
    area.set_on_window(surface, pop_area, pop_rect)


def custom_message(text, font):
    text_area = font.render(text, True, (255, 255, 255))
    return text_area, text_area.get_rect()


def second_main_off():
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    pg.init()
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
    clock = pg.time.Clock()
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
    # Adding sprites
    sprite_char_group = pg.sprite.Group()
    mc_gyver_sprite = Character.CharactersSprite()
    mc_gyver_sprite.set_position(1, 1)
    mc_gyver_sprite.set_image("./Package/Pictures/MacGyver.png")
    # sprite_char_group.add(mc_gyver_sprite)
    mc_gyver_sprite.add_to_group(sprite_char_group)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        # mc_gyver.start_move_avatar(event)
        Wd.color_window(surface)
        brown_block.initialize_landscape(brown_block_picture, surface, window_base)
        #mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        # needle.set_element(needle_picture, surface)
        # tube.set_element(tube_picture, surface)
        # ether.set_element(ether_picture, surface)
        sprite_char_group.draw(surface)
        mc_gyver_sprite.start_move_avatar(event)
        if mc_gyver.posy > limit_window_y or mc_gyver.posy < 0:
            message("Aie !!!! un mur !!!", window_base, surface)
            mc_gyver.stop_move_avatar(event, limit_window_x, limit_window_y)
        if mc_gyver.posx > limit_window_x or mc_gyver.posx < 0:
            message("Aie !!!! un mur !!!", window_base, surface)
            mc_gyver.stop_move_avatar(event, limit_window_x, limit_window_y)
        clock.tick(fps)
        pg.display.update()
    pg.quit()

    # This following block have to be fix first before implementation
    # the_maze = Maze.Maze()
    # event = the_maze.run_instance()
    # mc_gyver.move_avatar(event)
    # mc_gyver.set_avatar(mc_gyver_avatar, surface)
    # watchman.set_avatar(watchman_avatar, surface)
    # pg.display.update()


def running_maze(window_displayed):
    """

    :param window_displayed:
    :return:
    """
    y = 0
    x = 0
    end_window = 850
    walls_group = pg.sprite.Group()
    while (y and x) < end_window:
        for element in Sd.matrix_maze_2:
            if x == end_window:
                x = 0
                y += 50
            if element:
                wall = Sd.SurroundigsSprite()
                wall.set_position(x, y)
                wall.set_image("./Package/Pictures/Wall/big_brown_block.png")
                walls_group.add(wall)
                walls_group.draw(window_displayed)
            else:
                pass
            x += 50
        break
    state = True
    return state


def browsing_maze(sprite, sprite_group, sprite_name="sprite"):

    blocks_hit_list = pg.sprite.spritecollide(sprite, sprite_group, False)
    print("*" * 100)
    print("Event of the sprite : {}\n".format(sprite_name))
    print("***")
    for index, block in enumerate(blocks_hit_list):
        print(index, block)
        if block:
            return False
        else:
            return True
    print("***")
    print("*" * 100)
    return True

def draw_all_things(window, window_displayed, the_maze, sprite_char_group):

    window.set_background_on(window_displayed, 0, 0)
    walls_group = the_maze.initialize_maze(window_displayed)
    sprite_char_group.draw(window_displayed)
    return walls_group

def main():
    """

    :return:
    """
    pg.init()
    window_size = 850
    window_x = window_size
    window_y = window_size
    limit_window_x = window_x - 100
    limit_window_y = window_y - 100
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
    window = Wd.Window(window_x, window_y)
    window_displayed = window.display_window()
    window.set_background_on(window_displayed, 0, 0)
    clock = pg.time.Clock()
    fps = 60
    mc_gyver_sprite = Character.CharactersSprite()
    watchman_sprite = Character.CharactersSprite()
    mc_gyver_sprite.set_position(400, 350)
    watchman_sprite.set_position(750, 50)
    top_ghost = Character.CharactersSprite()
    bottom_ghost = Character.CharactersSprite()
    left_ghost = Character.CharactersSprite()
    right_ghost = Character.CharactersSprite()
    top_ghost.set_position(mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y-50)
    bottom_ghost.set_position(mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y+50)
    left_ghost.set_position(mc_gyver_sprite.rect.x-50, mc_gyver_sprite.rect.y)
    right_ghost.set_position(mc_gyver_sprite.rect.x+50, mc_gyver_sprite.rect.y)
    ghost_group = pg.sprite.Group()
    ghost_group.add(top_ghost, bottom_ghost, right_ghost, left_ghost)
    mc_gyver_sprite.set_image("./Package/Pictures/MacGyver.png")
    watchman_sprite.set_image("./Package/Pictures/Gardien.png")
    sprite_char_group = pg.sprite.Group()
    mc_gyver_sprite.add_to_group(sprite_char_group)
    watchman_sprite.add_to_group(sprite_char_group)
    the_maze = Maze.Maze(window_size)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
            window.set_background_on(window_displayed, 0, 0)
            walls_group = the_maze.initialize_maze(window_displayed)
            sprite_char_group.draw(window_displayed)
            top_ghost.set_position(mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y - 50)
            bottom_ghost.set_position(mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y + 50)
            left_ghost.set_position(mc_gyver_sprite.rect.x - 50, mc_gyver_sprite.rect.y)
            right_ghost.set_position(mc_gyver_sprite.rect.x + 50, mc_gyver_sprite.rect.y)
            pg.sprite.Group.update(ghost_group)
            top_collision_status = browsing_maze(top_ghost, walls_group, "top_ghost")
            right_collision_status = browsing_maze(right_ghost, walls_group, "right_ghost")
            bottom_collision_status = browsing_maze(bottom_ghost, walls_group, "bottom_ghost")
            left_collision_status = browsing_maze(left_ghost, walls_group, "left_ghost")
            list_ghost_status = [top_collision_status, right_collision_status,
                                 bottom_collision_status, left_collision_status]
            mc_gyver_sprite.start_move_avatar(event, list_ghost_status)
            if mc_gyver_sprite.rect.y > limit_window_y or mc_gyver_sprite.rect.y < 100:
                message("Aie !!!! un mur !!!", window, window_displayed)
                mc_gyver_sprite.stop_move_avatar(event, limit_window_x, limit_window_y)
            if mc_gyver_sprite.rect.x > limit_window_x or mc_gyver_sprite.rect.x < 100:
                message("Aie !!!! un mur !!!", window, window_displayed)
                mc_gyver_sprite.stop_move_avatar(event, limit_window_x, limit_window_y)
        clock.tick(fps)
        pg.display.update()
    pg.quit()


if __name__ == "__main__":
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    main()
