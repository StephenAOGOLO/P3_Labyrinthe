# coding: utf-8

import pygame as pg
import random as rd
import Labyrinthe.Package.Mazes as Maze
import Labyrinthe.Package.Options as Opt
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character
import Labyrinthe.Package.Surroundings as Sd
import Labyrinthe.Package.Objects as Obj


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
    """

    :param sprite:
    :param sprite_group:
    :param sprite_name:
    :return:
    """
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


def remove_track(move_status, last_position):
    """

    :param move_status:
    :param last_position:
    :return:
    """
    track_sprite = Character.CharactersSprite()
    if move_status:
        track_sprite.set_position(last_position[0], last_position[1])
        track_sprite.set_image("./Package/Pictures/Above_MacGyver/pyramid_sample.png")
        print("MOUVEMENT !!!!!!")
        return track_sprite
    else:
        return track_sprite


def game_over(status, window, window_displayed):
    """

    :param status:
    :param window:
    :param window_displayed:
    :return:
    """
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
                    object_settings = Opt.SettingsObject()
                    object_sprite = Obj.ObjectSprite(key)
                    object_sprite.set_position(x, y)
                    print(object_sprite.rect)
                    object_sprite.set_image(str(object_settings.data_file["path_picture"]))
                    objects_group.add(object_sprite)
                    list_sprites.append(object_sprite)
                    break
                x += 50
        break
    objects_group.draw(window_displayed)
    return list_sprites


def initialize_game():
    """

    :return:
    """
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
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
    """

    :param the_sprite:
    :return:
    """
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
    """

    :param list_ghost:
    :param the_sprite:
    :return:
    """
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
    """

    :param list_ghost:
    :param walls_group:
    :return:
    """
    list_ghost_status = []
    list_ghost_name = ["top_ghost", "right_ghost", "bottom_ghost", "left_ghost"]
    for index, ghost in enumerate(list_ghost):
        collision_status = browsing_maze(ghost, walls_group, list_ghost_name[index])
        list_ghost_status.append(collision_status)
    return list_ghost_status


def mac_gyver_behaviour(player_sprite, list_ghost_status, boss_sprite, sprite_char_group, event, list_objects):
    """

    :param player_sprite:
    :param list_ghost_status:
    :param boss_sprite:
    :param sprite_char_group:
    :param event:
    :param list_objects:
    :return:
    """
    last_position = [player_sprite.rect.x, player_sprite.rect.y]
    move_status = player_sprite.start_move_avatar(event, list_ghost_status)
    player_sprite.standstill_avatar(event)
    track_sprite = remove_track(move_status, last_position)
    player_sprite.be_collided(list_objects)
    sprite_char_group.add(track_sprite)
    list_end_game_status = player_sprite.prepared_objects_for(boss_sprite)
    return list_end_game_status


def draw_characters(sprite_char_group, mc_gyver_group, watchman_group, window_displayed):
    """

    :param sprite_char_group:
    :param mc_gyver_group:
    :param watchman_group:
    :param window_displayed:
    :return:
    """
    sprite_char_group.draw(window_displayed)
    mc_gyver_group.draw(window_displayed)
    watchman_group.draw(window_displayed)
    Obj.update_dashboard(window_displayed)
    return True


def needed_groups():
    list_group =[]
    for group in range(0,3):
        group = pg.sprite.Group()
        list_group.append(group)
    return list_group


def main_test():
    """

    :return:
    """
    pg.init()
    clock = pg.time.Clock()
    list_parameters = initialize_game()
    window = list_parameters[0]
    limit_window_x = list_parameters[1]
    limit_window_y = list_parameters[2]
    window_size = list_parameters[3]
    fps = list_parameters[4]
    mc_gyver_sprite = list_parameters[5]
    watchman_sprite = list_parameters[6]
    list_groups = needed_groups()
    sprite_char_group = list_groups[0]
    mc_gyver_group = list_groups[1]
    watchman_group = list_groups[2]
    window_displayed = window.display_window()
    window.set_background_on(window_displayed, 0, 0)
    list_ghost = set_ghost_sprite(mc_gyver_sprite)
    the_maze = Maze.Maze(window_size)
    walls_group = the_maze.initialize_maze(window_displayed)
    list_objects = set_objects(window_displayed)
    watchman_sprite.add_to_group(sprite_char_group)
    mc_gyver_group.add(mc_gyver_sprite)
    watchman_group.add(watchman_group)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
            list_ghost_reset = reset_ghost_sprite(list_ghost, mc_gyver_sprite)
            list_ghost_status = handle_collision(list_ghost_reset, walls_group)
            list_end_game_status = mac_gyver_behaviour(mc_gyver_sprite, list_ghost_status, watchman_sprite,
                                                       sprite_char_group, event, list_objects)
            draw_characters(sprite_char_group, mc_gyver_group, watchman_group, window_displayed)
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

