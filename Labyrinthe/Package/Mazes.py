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

    def initialize_maze(self, window_displayed):

        x = 0
        y = 0
        walls_group = pg.sprite.Group()
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
                if not element:
                    pass
                x += 50
            break
        return walls_group


if __name__ == "__main__":
    import Labyrinthe.Package.Window as Wd
    import pygame as pg
    import Labyrinthe.Package.Characters as Characters
    import Labyrinthe.Package.Surroundings as Sd
    pg.init()
    window_size = 850
    window_x = window_size
    window_y = window_size
    window = Wd.Window(window_x, window_y)
    window_displayed = window.display_window()
    a_sprite_char = Characters.CharactersSprite((255,255,255))
    a_sprite_char.set_position(20, 20)
    a_sprite_char.set_image("./Pictures/MacGyver.png")

    char_group = pg.sprite.Group()
    char_group.add(a_sprite_char)
    a_sprite_surrounding = Sd.SurroundigsSprite()
    a_sprite_char.set_image("./Pictures/Gardien.png")
    a_sprite_surrounding.set_position(0,0)
    surrounding_group = pg.sprite.Group()
    surrounding_group.add(a_sprite_surrounding)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
            window.set_background_on(window_displayed, 0, 0)
            char_group.draw(window_displayed)
            surrounding_group.draw(window_displayed)
            a_sprite_char.s
            pg.display.update()
    pg.quit()









