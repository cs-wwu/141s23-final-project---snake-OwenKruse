"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List

from gui import Gui
from position import Position


def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y() == position.get_y():
            return True
    return False


class Apple:
    """The apple's location is randomly generated."""

    def __init__(self, gui):
        width = gui.get_width()
        height = gui.get_height()
        self.position = Position(random.randint(1, width - 2), random.randint(1, height - 2))

    def draw(self, gui):
        gui.draw_text("@", self.position.get_x(), self.position.get_y(), "RED", "BLACK")

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def move(self, gui, snake):
        width = gui.get_width()
        height = gui.get_height()
        # Make sure the apple does not move where the snake is.
        while collides(self.position, snake.get_positions()):
            self.position = Position(random.randint(1, width - 2), random.randint(1, height - 2))

    def get_x(self):
        return self.position.get_x()

    def get_y(self):
        return self.position.get_y()

