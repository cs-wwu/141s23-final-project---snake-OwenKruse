"""
This module implements the snake class.
"""

from gui import Gui
from position import Position
from typing import List


class Snake:
    """This is the Snake.

    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """

    def __init__(self):
        self.positions: List[Position] = [
            Position(10, 10),
            Position(10, 11),
            Position(10, 12),
            Position(10, 13),
            Position(10, 14),
        ]

    def draw(self, gui):
        gui.draw_text("o", self.positions[0].xpos, self.positions[0].ypos, "GREEN", "BLACK")
        for i in range(1, len(self.positions)):
            gui.draw_text("*", self.positions[i].xpos, self.positions[i].ypos, "YELLOW", "BLACK")

    def move(self):
        for i in range(len(self.positions) - 1, 0, -1):
            self.positions[i].xpos = self.positions[i - 1].xpos
            self.positions[i].ypos = self.positions[i - 1].ypos

    def move_up(self):
        self.move()
        self.positions[0].ypos -= 1

    def move_down(self):
        self.move()
        self.positions[0].ypos += 1

    def move_left(self):
        self.move()
        self.positions[0].xpos -= 1

    def move_right(self):
        self.move()
        self.positions[0].xpos += 1

    def grow(self):
        self.positions.append(Position(self.positions[-1].xpos, self.positions[-1].ypos))

    def get_head(self):
        return self.positions[0]

    def get_tail(self):
        return self.positions[1:]

    def get_positions(self):
        return self.positions

    def get_length(self):
        return len(self.positions)

    def get_position(self, index):
        return self.positions[index]

    def hit_tail(self):
        for i in range(1, len(self.positions)):
            if self.positions[0].xpos == self.positions[i].xpos and self.positions[0].ypos == self.positions[i].ypos:
                return True
        return False
