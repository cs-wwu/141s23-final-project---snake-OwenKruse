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

    def __init__(self):
        pass

    def draw(self, gui):
        pass
