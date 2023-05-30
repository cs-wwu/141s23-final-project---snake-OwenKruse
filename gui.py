"""
This module provides a class to draw text graphics to the screen.
The class is called Gui. Creating a Gui object causes the screen to
clear and go into full screen drawing mode. You may use methods on the
Gui class to clear the screen and draw text to the screen. The text is
drawn in an offscreen buffer. Calling refresh shows the elements that
have been drawn all at once.

The class also provides a way to get user input from the keyboard.

Drawing beyond the edges of the screen will cause an exception be thrown.
"""

import curses
import signal
import sys
from typing import Tuple


def swap(x1, y1, x2, y2) -> Tuple[int, int, int, int]:
    return x2, y2, x1, y1

def handle_sigint(gui):
    """Handle control C by quitting gracefully."""
    def handler(signum, frame):
        gui.quit()
        sys.exit(-1)
    signal.signal(signal.SIGINT, handler)

class Gui:
    """A class to draw text graphics on the screen using the curses library."""

    def __init__(self) -> None:
        """Create a Gui object that takes over the screen."""
        self.screen = curses.initscr()
        self.pad = curses.newpad(curses.LINES, curses.COLS)
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.pad.nodelay(True)
        self.pad.keypad(True)
        self.logdata = []
        self.last_color_index = 1
        self.color_pairs = dict()
        self.logbuf = []

        handle_sigint(self)

    def quit(self) -> None:
        """Quit Gui mode and return screen to normal, also print logs."""
        curses.nocbreak()
        self.pad.keypad(False)
        curses.echo()
        curses.endwin()
        for s in self.logbuf:
            print(s)

    def get_width(self) -> int:
        """Return the width of the screen in number of columns."""
        return curses.COLS

    def get_height(self) -> int:
        """Return the height of the screen in number of rows."""
        return curses.LINES

    def get_keypress(self) -> str:
        """Return the key that was pressed.

        For example, if "q" is impressed, it will return the string "q".
        If one of the arrow keys was pressed, return "KEY_LEFT", "KEY_UP"m
        "KEY_RIGHT" or "KEY_DOWN" respectively.
        """
        c = self.pad.getch()
        if c >= 0 and c <= 255:
            return chr(c)
        elif c == curses.KEY_LEFT:
            return "KEY_LEFT"
        elif c == curses.KEY_RIGHT:
            return "KEY_RIGHT"
        elif c == curses.KEY_DOWN:
            return "KEY_DOWN"
        elif c == curses.KEY_UP:
            return "KEY_UP"
        else:
            return ""

    def draw_text(self, s: str, x: int, y: int, fore_color: str,
            back_color: str) -> None:
        """Draw the text given by the string s at the location x and y.

        This method draws the string with the given colors. The text is
        drawn in an offscreen buffer. Use the refresh() method to show the
        text.

        Drawing off the edge of the screen will cause an error to be thrown.
        """
        if x < 0 or x >= self.get_width() or y < 0 or y >= self.get_height():
            raise RuntimeError("Gui.draw_text: x=%d, y=%d is out of bounds" %
                               (x, y))

        color_key = fore_color + ":" + back_color
        if color_key in self.color_pairs:
            color_index = self.color_pairs[color_key]
        else:
            color_pair = curses.init_pair(self.last_color_index, self.get_color(fore_color),
                self.get_color(back_color))
            self.color_pairs[color_key] = self.last_color_index
            color_index = self.last_color_index
            self.last_color_index += 1

        # Must handle the lower right corner specially
        if x == self.get_width() - 1 and y == self.get_height() - 1:
            self.pad.insstr(y, x, s, curses.color_pair(color_index))
        else:
            self.pad.addstr(y, x, s, curses.color_pair(color_index))

    def get_color(self, color: str) -> int:
        """Helper function to get color indices from strings."""
        if color == "BLACK":
            return curses.COLOR_BLACK
        elif color == "RED":
            return curses.COLOR_RED
        elif color == "GREEN":
            return curses.COLOR_GREEN
        elif color == "YELLOW":
            return curses.COLOR_YELLOW
        elif color == "BLUE":
            return curses.COLOR_BLUE
        elif color == "MAGENTA":
            return curses.COLOR_MAGENTA
        elif color == "CYAN":
            return curses.COLOR_CYAN
        elif color == "WHITE":
            return curses.COLOR_WHITE
        else:
            return curses.COLOR_WHITE

    def draw_line(self, c: str, x1: int, y1: int, x2: int, y2: int,
            fore_color: str, back_color: str) -> None:
        """Draw a line from x1, y1 to x2, y2 with the given character.

        This method draws the string with the given colors. The text is
        drawn in an offscreen buffer. Use the refresh() method to show the
        text.

        Drawing off the edge of the screen will cause an exception to be thrown.
        """
        if x1 == x2:
            # draw vertical line
            if y1 > y2:
                x1, y1, x2, y2 = swap(x1, y1, x2, y2)
            for y in range(y1, y2 + 1):
                self.draw_text(c, x1, y, fore_color, back_color)
        else:
            # draw horizontal or general line
            if x1 > x2:
                x1, y1, x2, y2 = swap(x1, y1, x2, y2)

            dx = x2 - x1
            dy = y2 - y1
            for x in range(x1, x2 + 1):
                y = round(y1 + dy * (x - x1) / dx)
                self.draw_text(c, x, y, fore_color, back_color)

    def clear(self) -> None:
        """Clear the screen."""
        self.pad.erase()

    def refresh(self) -> None:
        """Display contents of the offscreen buffer."""
        self.pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)

    def log(self, s) -> None:
        self.logbuf.append(s)

    def print_log(self) -> None:
        for s in self.logbuf:
            print(s)

if __name__ == '__main__':
    import sys
    import time

    g = Gui()
    try:
        for i in range(30):
            g.clear()
            g.draw_text("foo",  i, 10, "CYAN", "WHITE")
            g.draw_line('$', 10, 10, 40, 15, "GREEN", "RED")
            g.draw_line("=", 0, 0,
                g.get_width() - 1, g.get_height() - 1, "GREEN", "BLACK")
            c = g.get_keypress()
            if c == 'q':
                break
            g.refresh()
            time.sleep(0.1)
    except Exception as e:
        g.quit()
        raise e
        sys.exit(-1)

    g.quit()
