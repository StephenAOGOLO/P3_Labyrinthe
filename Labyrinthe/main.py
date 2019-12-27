# coding: utf-8
import pygame as pg
import logging as lg
import Labyrinthe.Package.Mazes as Maze
import Labyrinthe.Package.Options as Opt
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character
import Labyrinthe.Package.Objects as Obj

lg.basicConfig(level=lg.WARNING)


def browsing_maze(sprite, sprite_group, sprite_name="sprite"):
    """

    :param sprite:
    :param sprite_group:
    :param sprite_name:
    :return:
    """
    blocks_hit_list = pg.sprite.spritecollide(sprite, sprite_group, False)
    lg.info("*\nEvent of the sprite : {}\n*".format(sprite_name))
    for index, block in enumerate(blocks_hit_list):
        lg.info(index, block)
        if block:
            return False
        else:
            return True
    lg.info("***")
    lg.info("*" * 100)
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
        track_sprite.set_image("./Package/Pictures/wall/pyramid_sample.png")
        lg.info("MOUVEMENT !!!!!!")
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
        window.picture = pg.image.load("./Package/Pictures/Messages/mission_passed.png")
    if status is False:
        window.picture = pg.image.load("./Package/Pictures/Messages/wasted.jpg")
    window.set_background_on(window_displayed, 200, 200)
    pg.display.update()
    pg.time.wait(5000)


def initialize_game():
    """

    :return:
    """
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
    dict_parameters = {}
    # WINDOW PARAMETERS
    window_settings = Opt.SettingsWindow()
    window_width = int(window_settings.data_file["window_width"])
    window_height = int(window_settings.data_file["window_height"])
    limit_window_x = int(window_settings.data_file["limit_x"])
    limit_window_y = int(window_settings.data_file["limit_y"])
    window_size = int(window_settings.data_file["window_size"])
    window = Wd.Window(window_width, window_height)
    clock_settings = Opt.SettingsWindow()
    fps = int(clock_settings.data_file["fps"])
    window_displayed = window.display_window()
    window.set_background_on(window_displayed, 0, 0)
    # MAC GYVER PARAMETERS
    mc_gyver_settings = Opt.SettingsCharacter()
    mc_gyver_sprite = Character.CharactersSprite()
    mc_gyver_sprite.set_image(str(mc_gyver_settings.data_file["path_picture"]))
    list_ghost = set_ghost_sprite(mc_gyver_sprite)
    # WATCHMAN PARAMETERS
    watchman_settings = Opt.SettingsCharacter()
    watchman_sprite = Character.CharactersSprite()
    watchman_sprite.set_image(watchman_settings.data_file["path_picture"])
    # GROUPS PARAMETERS
    list_groups = needed_groups_for(mc_gyver_sprite, watchman_sprite)
    # MAZE PARAMETERS
    the_maze = Maze.Maze(window_size)
    walls_group = the_maze.initialize_maze(window_displayed)
    Character.set_in_maze(the_maze, mc_gyver_sprite, watchman_sprite)
    # OBJECTS PARAMETERS
    list_objects = Obj.set_objects(window_displayed)
    dict_parameters["window"] = window
    dict_parameters["limit_window_x"] = limit_window_x
    dict_parameters["limit_window_y"] = limit_window_y
    dict_parameters["fps"] = fps
    dict_parameters["mc_gyver_sprite"] = mc_gyver_sprite
    dict_parameters["watchman_sprite"] = watchman_sprite
    dict_parameters["window_displayed"] = window_displayed
    dict_parameters["list_ghost"] = list_ghost
    dict_parameters["walls_group"] = walls_group
    dict_parameters["list_objects"] = list_objects
    dict_parameters["list_groups"] = list_groups
    return dict_parameters


def set_ghost_sprite(the_sprite):
    """
    Create ghosts sprite around the referenced sprite.
    Add all the ghosts sprite and the group into the list to return.
    :param the_sprite:
    :return:
    """
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


def attitude(player_sprite, list_ghost_status, boss_sprite, sprite_char_group, event, list_objects):
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


def needed_groups_for(mc_gyver_sprite, watchman_sprite):
    """

    :return:
    """
    list_group = []
    for group in range(0, 3):
        group = pg.sprite.Group()
        list_group.append(group)
    watchman_sprite.add_to_group(list_group[0])
    mc_gyver_sprite.add_to_group(list_group[1])
    watchman_sprite.add_to_group(list_group[2])
    return list_group


def main_test():
    """

    :return:
    """
    global game_state
    pg.init()
    clock = pg.time.Clock()
    dict_parameters = initialize_game()
    window = dict_parameters["window"]
    fps = dict_parameters["fps"]
    mc_gyver_sprite = dict_parameters["mc_gyver_sprite"]
    watchman_sprite = dict_parameters["watchman_sprite"]
    window_displayed = dict_parameters["window_displayed"]
    list_ghost = dict_parameters["list_ghost"]
    walls_group = dict_parameters["walls_group"]
    list_objects = dict_parameters["list_objects"]
    list_groups = dict_parameters["list_groups"]
    char_group = list_groups[0]
    mc_gyver_group = list_groups[1]
    watchman_group = list_groups[2]
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
            ghost_reset = reset_ghost_sprite(list_ghost, mc_gyver_sprite)
            ghost_state = handle_collision(ghost_reset, walls_group)
            game_state = attitude(mc_gyver_sprite, ghost_state, watchman_sprite, char_group, event, list_objects)
            draw_characters(char_group, mc_gyver_group, watchman_group, window_displayed)
            if game_state[0] is True:
                launched = False
                break
        clock.tick(fps)
        pg.display.update()
    game_over(game_state[1], window, window_displayed)
    pg.quit()


if __name__ == "__main__":
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """
    # Pure version of main()
    main_test()

