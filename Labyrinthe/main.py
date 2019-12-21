# coding: utf-8

import pygame as pg
import configparser as cp
import random as rd
import Labyrinthe.Package.Mazes as Maze
import Labyrinthe.Package.Options as Opt
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character
import Labyrinthe.Package.Surroundings as Sd
import Labyrinthe.Package.Objects as Obj





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
    # mc_gyver_sprite.add_to_group(sprite_char_group)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        # mc_gyver.start_move_avatar(event)
        Wd.color_window(surface)
        brown_block.initialize_landscape(brown_block_picture, surface, window_base)
        # mc_gyver.set_avatar(mc_gyver_avatar, surface)
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


def remove_track(move_status, last_position, window_displayed):
    # remove_status = False
    # the_track = pg.sprite.Group()
    track_sprite = Character.CharactersSprite()
    if move_status:
        track_sprite.set_position(last_position[0], last_position[1])
        track_sprite.set_image("./Package/Pictures/Above_MacGyver/pyramid_sample.png")
        # the_track = pg.sprite.Group()
        # the_track.draw(window_displayed)
        # remove_status = True
        print("MOUVEMENT !!!!!!")
        return track_sprite
    else:
        return track_sprite


def game_over(status, window, window_displayed):
    if status is True:
        window.picture = pg.image.load("./Package/Pictures/Messages/mission_passed_200x65.png")
    if status is False:
        window.picture = pg.image.load("./Package/Pictures/Messages/wasted.jpg")
    window.set_background_on(window_displayed, 300, 250)
    pg.display.update()
    pg.time.wait(5000)


def set_objects(window_displayed):
    """

    :param window_displayed:
    :return:
    """
    list_sprites = []
    list_forbidden = [15, 32, 49, 48, 127]
    list_index = [index for index, element in enumerate(Sd.matrix_maze_2) if element is False]
    for element in list_forbidden:
        list_index.remove(element)
    three_random_index = rd.sample(list_index, k=3)
    dico_objects = {"Needle": three_random_index[0], "Tube": three_random_index[1], "Ether": three_random_index[2]}
    y = 0
    x = 0
    end_window = 850
    objects_group = pg.sprite.Group()
    while (y and x) < end_window:
        for key, value in dico_objects.items():
            y = 0
            x = 0
            for e, element in enumerate(Sd.matrix_maze_2):
                if x == end_window:
                    x = 0
                    y += 50
                if element is False and e == value:
                    object_sprite = Obj.ObjectSprite(key)
                    object_sprite.set_position(x, y)
                    print(object_sprite.rect)
                    object_sprite.set_image("./Package/Pictures/Objects/sarcophagus_50x50.png")
                    objects_group.add(object_sprite)
                    list_sprites.append(object_sprite)
                    break
                x += 50
        break
    objects_group.draw(window_displayed)
    return list_sprites


def initialize_game():

    list_parameters = []
    # WINDOW PARAMETERS
    window_settings = Opt.SettingsWindow()
    window = Wd.Window(int(window_settings.data_file["window_width"]), int(window_settings.data_file["window_height"]))
    limit_window_x = int(window_settings.data_file["limit_x"])
    limit_window_y = int(window_settings.data_file["limit_y"])
    window_size = int(window_settings.data_file["window_size"])
    clock_settings = Opt.SettingsWindow()
    fps = int(clock_settings.data_file["fps"])
    # MAC GYVER PARAMETERS
    mc_gyver_settings = Opt.SettingsCharacter()
    mc_gyver_sprite = Character.CharactersSprite()
    mc_gyver_sprite.set_position(int(mc_gyver_settings.data_file["startx"]), int(mc_gyver_settings.data_file["starty"]))
    mc_gyver_sprite.set_image(str(mc_gyver_settings.data_file["path_picture"]))
    # WATCHMAN PARAMETERS
    watchman_settings = Opt.SettingsCharacter()
    watchman_sprite = Character.CharactersSprite()
    watchman_sprite.set_position(int(watchman_settings.data_file["startx"]), int(watchman_settings.data_file["starty"]))
    watchman_sprite.set_image(watchman_settings.data_file["path_picture"])

    list_parameters.append(window)
    list_parameters.append(limit_window_x)
    list_parameters.append(limit_window_y)
    list_parameters.append(window_size)
    list_parameters.append(fps)
    list_parameters.append(mc_gyver_sprite)
    list_parameters.append(watchman_sprite)

    return list_parameters


def set_ghost_sprite(the_sprite):

    # Create ghosts sprite around the referenced sprite
    list_ghost = []
    top_ghost = Character.CharactersSprite()
    bottom_ghost = Character.CharactersSprite()
    left_ghost = Character.CharactersSprite()
    right_ghost = Character.CharactersSprite()
    top_ghost.set_position(the_sprite.rect.x, the_sprite.rect.y-50)
    bottom_ghost.set_position(the_sprite.rect.x, the_sprite.rect.y+50)
    left_ghost.set_position(the_sprite.rect.x-50, the_sprite.rect.y)
    right_ghost.set_position(the_sprite.rect.x+50, the_sprite.rect.y)
    ghost_group = pg.sprite.Group()
    ghost_group.add(top_ghost, bottom_ghost, right_ghost, left_ghost)
    # Add all the ghosts sprite and the group into the list to return
    list_ghost.append(top_ghost)
    list_ghost.append(bottom_ghost)
    list_ghost.append(right_ghost)
    list_ghost.append(left_ghost)
    list_ghost.append(ghost_group)
    return list_ghost


def reset_ghost_sprite(list_ghost, the_sprite):

    new_list = []
    top_ghost = list_ghost[0]
    bottom_ghost = list_ghost[1]
    right_ghost = list_ghost[2]
    left_ghost = list_ghost[3]
    ghost_group = list_ghost[4]
    top_ghost.set_position(the_sprite.rect.x, the_sprite.rect.y - 50)
    bottom_ghost.set_position(the_sprite.rect.x, the_sprite.rect.y + 50)
    left_ghost.set_position(the_sprite.rect.x - 50, the_sprite.rect.y)
    right_ghost.set_position(the_sprite.rect.x + 50, the_sprite.rect.y)
    pg.sprite.Group.update(ghost_group)
    new_list.append(top_ghost)
    new_list.append(right_ghost)
    new_list.append(bottom_ghost)
    new_list.append(left_ghost)
    return new_list


def handle_collision(list_ghost, walls_group):
    #top_ghost = list_ghost[0]
    #bottom_ghost = list_ghost[1]
    #right_ghost = list_ghost[2]
    #left_ghost = list_ghost[3]
    #ghost_group = list_ghost[4]
    list_ghost_status = []
    list_ghost_name = ["top_ghost", "right_ghost", "bottom_ghost", "left_ghost"]
    for index, ghost in enumerate(list_ghost):
        collision_status = browsing_maze(ghost, walls_group, list_ghost_name[index])
        list_ghost_status.append(collision_status)
    # top_collision_status = browsing_maze(top_ghost, walls_group, "top_ghost")
    # right_collision_status = browsing_maze(right_ghost, walls_group, "right_ghost")
    # bottom_collision_status = browsing_maze(bottom_ghost, walls_group, "bottom_ghost")
    # left_collision_status = browsing_maze(left_ghost, walls_group, "left_ghost")
    # list_ghost_status = [top_collision_status, right_collision_status,
    #                      bottom_collision_status, left_collision_status]
    return list_ghost_status


def mac_gyver_behaviour(player_sprite, list_ghost_status, boss_sprite, sprite_char_group, event, window_displayed, list_objects):

    last_position = [player_sprite.rect.x, player_sprite.rect.y]
    move_status = player_sprite.start_move_avatar(event, list_ghost_status)
    player_sprite.standstill_avatar(move_status, event)
    track_sprite = remove_track(move_status, last_position, window_displayed)
    player_sprite.be_collided(list_objects)
    sprite_char_group.add(track_sprite)
    list_end_game_status = player_sprite.prepared_objects_for(boss_sprite)
    return list_end_game_status



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


def main_test():
    """

    :return:
    """
    # --------------------------------------------------------------------------------------------------------------
    # OK - IT WORKS
    # window_size = 850
    # window_x = window_size
    # window_y = window_size
    # limit_window_x = window_x - 100
    # limit_window_y = window_y - 100
    # window = Wd.Window(window_x, window_y)
    ## window_settings = Opt.SettingsWindow()
    ## window = Wd.Window(int(window_settings.data_file["window_width"]), int(window_settings.data_file["window_height"]))
    ## limit_window_x = int(window_settings.data_file["limit_x"])
    ## limit_window_y = int(window_settings.data_file["limit_y"])
    ## window_size = int(window_settings.data_file["window_size"])
    # Value to retrun : window, limit_window_x, limit_window_y, window_size
    # --------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------
    # KO - STAY LIKE THIS
    #pg.display.set_caption("Aidez MacGyver à s'échapper !")
    # --------------------------------------------------------------------------------------------------------------
    # window_displayed = window.display_window()
    # window.set_background_on(window_displayed, 0, 0)
    # --------------------------------------------------------------------------------------------------------------
    # OK - IT WORKS
    ## clock_settings = Opt.SettingsWindow()
    #clock = pg.time.Clock()
    # fps = 60
    ## fps = int(clock_settings.data_file["fps"])
    # Value to retrun : fps
    # --------------------------------------------------------------------------------------------------------------
    # OK - IT WORKS
    ## mc_gyver_settings = Opt.SettingsCharacter()
    ## mc_gyver_sprite = Character.CharactersSprite()
    # mc_gyver_sprite.set_position(400, 350)
    ## mc_gyver_sprite.set_position(int(mc_gyver_settings.data_file["startx"]), int(mc_gyver_settings.data_file["starty"]))
    #mc_gyver_sprite.set_image("./Package/Pictures/Above_MacGyver/a_mg_s_t_f.png")
    ## mc_gyver_sprite.set_image(str(mc_gyver_settings.data_file["path_picture"]))
    # Value to retrun : mc_gyver_sprite
    # --------------------------------------------------------------------------------------------------------------
    #top_ghost = Character.CharactersSprite()
    #bottom_ghost = Character.CharactersSprite()
    #left_ghost = Character.CharactersSprite()
    #right_ghost = Character.CharactersSprite()
    #top_ghost.set_position(mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y-50)
    #bottom_ghost.set_position(mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y+50)
    #left_ghost.set_position(mc_gyver_sprite.rect.x-50, mc_gyver_sprite.rect.y)
    #right_ghost.set_position(mc_gyver_sprite.rect.x+50, mc_gyver_sprite.rect.y)
    #ghost_group = pg.sprite.Group()
    #ghost_group.add(top_ghost, bottom_ghost, right_ghost, left_ghost)
    # --------------------------------------------------------------------------------------------------------------
    # OK - IT WORKS
    ## watchman_settings = Opt.SettingsCharacter()
    ## watchman_sprite = Character.CharactersSprite()
    #watchman_sprite.set_position(750, 50)
    ## watchman_sprite.set_position(int(watchman_settings.data_file["startx"]), int(watchman_settings.data_file["starty"]))
    #watchman_sprite.set_image("./Package/Pictures/Above_Watchman/a_w_ss_f.png")
    ## watchman_sprite.set_image(watchman_settings.data_file["path_picture"])
    # Value to retrun : watchman_sprite
    # --------------------------------------------------------------------------------------------------------------
    #top_ghost = Character.CharactersSprite()
    #bottom_ghost = Character.CharactersSprite()
    #left_ghost = Character.CharactersSprite()
    #right_ghost = Character.CharactersSprite()
    #top_ghost.set_position(mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y-50)
    #bottom_ghost.set_position(mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y+50)
    #left_ghost.set_position(mc_gyver_sprite.rect.x-50, mc_gyver_sprite.rect.y)
    #right_ghost.set_position(mc_gyver_sprite.rect.x+50, mc_gyver_sprite.rect.y)
    #ghost_group = pg.sprite.Group()
    #ghost_group.add(top_ghost, bottom_ghost, right_ghost, left_ghost)
    # --------------------------------------------------------------------------------------------------------------
    pg.init()
    list_parameters = initialize_game()
    window = list_parameters[0]
    limit_window_x = list_parameters[1]
    limit_window_y = list_parameters[2]
    window_size = list_parameters[3]
    fps = list_parameters[4]
    mc_gyver_sprite = list_parameters[5]
    watchman_sprite = list_parameters[6]
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
    clock = pg.time.Clock()
    window_displayed = window.display_window()
    window.set_background_on(window_displayed, 0, 0)
    list_ghost = set_ghost_sprite(mc_gyver_sprite)
    top_ghost = list_ghost[0]
    bottom_ghost = list_ghost[1]
    right_ghost = list_ghost[2]
    left_ghost = list_ghost[3]
    ghost_group = list_ghost[4]
    sprite_char_group = pg.sprite.Group()
    watchman_sprite.add_to_group(sprite_char_group)
    the_maze = Maze.Maze(window_size)
    window.set_background_on(window_displayed, 0, 0)
    walls_group = the_maze.initialize_maze(window_displayed)
    list_objects = set_objects(window_displayed)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
            list_ghost_reset = reset_ghost_sprite(list_ghost, mc_gyver_sprite)
            list_ghost_status = handle_collision(list_ghost_reset, walls_group)
            list_end_game_status = mac_gyver_behaviour(mc_gyver_sprite,
            list_ghost_status, watchman_sprite, sprite_char_group, event, window_displayed, list_objects)
            mc_gyver_group = pg.sprite.Group()
            watchman_group = pg.sprite.Group()
            mc_gyver_group.add(mc_gyver_sprite)
            watchman_group.add(watchman_group)
            sprite_char_group.draw(window_displayed)
            mc_gyver_group.draw(window_displayed)
            watchman_group.draw(window_displayed)
            if mc_gyver_sprite.rect.y > limit_window_y or mc_gyver_sprite.rect.y < 100:
                # message("Aie !!!! un mur !!!", window, window_displayed)
                mc_gyver_sprite.stop_move_avatar(event, limit_window_x, limit_window_y)
            if mc_gyver_sprite.rect.x > limit_window_x or mc_gyver_sprite.rect.x < 100:
                # message("Aie !!!! un mur !!!", window, window_displayed)
                mc_gyver_sprite.stop_move_avatar(event, limit_window_x, limit_window_y)
            if list_end_game_status[0] is True:
                launched = False
                break
        clock.tick(fps)
        pg.display.update()
    game_over(list_end_game_status[1], window, window_displayed)
    pg.quit()



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
    mc_gyver_sprite.set_image("./Package/Pictures/Above_MacGyver/a_mg_s_t_f.png")
    watchman_sprite.set_image("./Package/Pictures/Above_Watchman/a_w_ss_f.png")
    sprite_char_group = pg.sprite.Group()
    watchman_sprite.add_to_group(sprite_char_group)
    the_maze = Maze.Maze(window_size)
    window.set_background_on(window_displayed, 0, 0)
    walls_group = the_maze.initialize_maze(window_displayed)
    list_objects = set_objects(window_displayed)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
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
            last_position = [mc_gyver_sprite.rect.x, mc_gyver_sprite.rect.y]
            move_status = mc_gyver_sprite.start_move_avatar(event, list_ghost_status)
            mc_gyver_sprite.standstill_avatar(move_status, event)
            track_sprite = remove_track(move_status, last_position, window_displayed)
            mc_gyver_sprite.be_collided(list_objects)
            list_end_game_status = mc_gyver_sprite.prepared_objects_for(watchman_sprite)
            sprite_char_group.add(track_sprite)
            mc_gyver_group = pg.sprite.Group()
            watchman_group = pg.sprite.Group()
            mc_gyver_group.add(mc_gyver_sprite)
            watchman_group.add(watchman_group)
            sprite_char_group.draw(window_displayed)
            mc_gyver_group.draw(window_displayed)
            watchman_group.draw(window_displayed)
            if mc_gyver_sprite.rect.y > limit_window_y or mc_gyver_sprite.rect.y < 100:
                # message("Aie !!!! un mur !!!", window, window_displayed)
                mc_gyver_sprite.stop_move_avatar(event, limit_window_x, limit_window_y)
            if mc_gyver_sprite.rect.x > limit_window_x or mc_gyver_sprite.rect.x < 100:
                # message("Aie !!!! un mur !!!", window, window_displayed)
                mc_gyver_sprite.stop_move_avatar(event, limit_window_x, limit_window_y)
            if list_end_game_status[0] is True:
                launched = False
                break
        clock.tick(fps)
        pg.display.update()
    game_over(list_end_game_status[1], window, window_displayed)
    pg.quit()


if __name__ == "__main__":
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    # Pure version of main()
    main_test()
    # heavy version of main()
    #main()
