# Wall takes two cordinate pairs and draws a wall between them
from apple import Apple
from gui import Gui
import random
import snake as Snake
import position as Position


class Wall:

    def __init__(self, gui) -> None:
        width = gui.get_width()
        height = gui.get_height()
        # Make sure the wall is a straight line and not bigger than 5
        if random.randint(0, 1) == 0:
            self.x1 = random.randint(1, width - 2)
            self.x2 = self.x1
            self.y1 = random.randint(1, height - 2)
            self.y2 = self.y1 + random.randint(1, 5)
            if self.y2 > height - 2:
                self.y2 = height - 2
        else:
            self.x1 = random.randint(1, width - 2)
            self.x2 = self.x1 + random.randint(1, 5)
            if self.x2 > width - 2:
                self.x2 = width - 2
            self.y1 = random.randint(1, height - 2)
            self.y2 = self.y1

    def draw(self, gui):
        if self.x1 == self.x2:
            for y in range(self.y1, self.y2 + 1):
                gui.draw_text("#", self.x1, y, "WHITE", "BLACK")
        elif self.y1 == self.y2:
            for x in range(self.x1, self.x2 + 1):
                gui.draw_text("#", x, self.y1, "WHITE", "BLACK")
        else:
            print("Error: Wall must be either horizontal or vertical")

    def get_x1(self):
        return self.x1

    def get_y1(self):
        return self.y1

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

    # Checks if the wall collides with the apple
    def collides_with_apple(self, apple: Apple):
        if self.x1 == self.x2:
            for y in range(self.y1, self.y2 + 1):
                if apple.get_x() == self.x1 and apple.get_y() == y:
                    return True
        elif self.y1 == self.y2:
            for x in range(self.x1, self.x2 + 1):
                if apple.get_x() == x and apple.get_y() == self.y1:
                    return True
        return False

    def get_positions(self):
        positions = []
        if self.x1 == self.x2:
            for y in range(self.y1, self.y2 + 1):
                positions.append(Position.Position(self.x1, y))
        elif self.y1 == self.y2:
            for x in range(self.x1, self.x2 + 1):
                positions.append(Position.Position(x, self.y1))
        return positions
