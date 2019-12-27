import pygame as pg


matrix_maze_2 = [
    True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True,
    True, False, False, True, False, False, False, True, False, False, False, False, False, False, True, False, True,
    True, True, False, False, False, True, False, False, False, True, True, True, True, True, False, False, True,
    True, False, False, True, True, True, True, True, False, True, True, True, False, False, False, True, True,
    True, False, True, True, False, False, False, False, False, False, False, True, False, True, True, False, True,
    True, False, False, True, False, True, True, True, True, True, False, True, False, True, False, False, True,
    True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, True,
    True, False, False, True, False, True, False, True, False, True, False, True, True, True, False, False, True,
    True, False, True, True, False, True, False, True, True, True, False, True, False, True, True, False, True,
    True, False, False, True, False, True, False, False, False, False, False, True, False, True, True, False, True,
    True, True, False, True, False, True, True, True, True, True, True, True, False, True, True, False, True,
    True, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, True,
    True, False, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True,
    True, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, True,
    True, True, True, True, False, False, True, False, False, True, False, True, True, True, False, True, True,
    True, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, True,
    True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
    ]


class SurroundingsElement:
    """
    Building in progress...
    """
    def __init__(self, name, file_png, posx, posy):
        """

        :param name:
        :param file_png:
        :param posx:
        :param posy:
        """
        self.name = name
        self.picture = file_png
        self.posx = posx
        self.posy = posy

    def load_element_picture(self):
        """

        :return:
        """
        picture_element = pg.image.load(self.picture)
        return picture_element

    def set_element(self, element, window):
        """

        :param element:
        :param window:
        :return:
        """
        element_set = window.blit(element, (self.posx, self.posy))
        return element_set

    def initialize_landscape(self, element, surface, window):
        """

        :param element:
        :param surface:
        :param window:
        :return:
        """
        for y in range(10, window.height - 10, 21):
            for x in range(10, window.width - 10, 20):
                landscape = surface.blit(element, (x, y))
                # print("x = {}\ny = {}\n".format(x, y))
        return landscape


class SurroundigsSprite(pg.sprite.Sprite):
    def __init__(self, color=(0, 0, 0), width=50, height=50):
        super(SurroundigsSprite, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, filename=None):
        if filename is not None:
            self.image = pg.image.load(filename)
            #self.rect = self.image.get_rect()


def sort_wall(list_pictures, group):
    for element in list_pictures:
        if element == "b":
            pass


def landscape(list_pictures, group):
    for x in range(0, 750, 50):
        for element in list_pictures:
            pass


if __name__ == "__main__":
    import Labyrinthe.Package.Window as Wd
    pg.init()
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
    window = Wd.Window(770, 770)
    window_displayed = window.display_window()
    clock = pg.time.Clock()
    fps = 60
    walls_group = pg.sprite.Group()
    list_bool = [True, False]
    y = 0
    x = 0
    end_window = 750
    window.set_background_on(window_displayed, 0, 0)
    while (y and x) < end_window:
        for element in matrix_maze:
            if x == end_window:
                x = 0
                y += 50
            if element:
                wall = SurroundigsSprite()
                wall.set_position(x, y)
                wall.set_image("./Pictures/Wall/big_brown_block.png")
                walls_group.add(wall)
                walls_group.draw(window_displayed)
            else:
                pass
            x += 50
    print(walls_group.sprites())
    print(len(walls_group))
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        clock.tick(fps)
        pg.display.update()
    pg.quit()
