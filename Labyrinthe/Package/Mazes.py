import pygame as pg
import Labyrinthe.Package.Surroundings as Sd


class Maze:
    """
    Building in progress...
    """
    def __init__(self, window_size):
        """
        Building in progress...
        """
        state = True
        self.window_size = window_size
        self.limit_window_x = self.set_limit_window_size(100)
        self.limit_window_y = self.set_limit_window_size(100)
        #self.event = self.run_instance(state)
        #self.stop = self.stop_instance()


    def set_limit_window_size(self, limit):
        """

        :param limit:
        :return:
        """

        return self.window_size - limit


    def run_instance(self, state):
        """

        :param state:
        :return:
        """
        while state:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.stop_instance()
                return event
        pg.QUIT()

    def stop_instance(self):
        """

        :return:
        """
        message = "Instance Maze stopped"
        state = False
        self.run_instance(state)
        print(message)
        return message

    def initialize_maze(self, window_displayed, sprite_player, sprite_boss):

        x = 0
        y = 0
        walls_group = pg.sprite.Group()
        #walls_group.add(sprite_player)
        #walls_group.add(sprite_boss)
        while (y and x) < self.window_size:
            for element in Sd.matrix_maze_2:
                if x == self.window_size:
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
        #browsing_maze(sprite_player, walls_group)
        #blocks_hit_list = pg.sprite.spritecollide(sprite_player, walls_group, False)
        #print("***")
        #for block in blocks_hit_list:
        #    print(block)
        #print("***")
        return walls_group


#def browsing_maze(sprite_player, sprite_group):
#
#    blocks_hit_list = pg.sprite.spritecollide(sprite_player, sprite_group, False)
#    print("***")
#    for block in blocks_hit_list:
#        print(block)
#    print("***")








