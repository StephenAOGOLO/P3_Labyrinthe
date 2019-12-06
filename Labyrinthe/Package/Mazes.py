import pygame as pg


class Maze:
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        state = True
        self.event = self.run_instance(state)
        self.stop = self.stop_instance()

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
