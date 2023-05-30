"""
This is the main program for the snake game.
"""

import time

from gui import Gui
from room import Room
from snake import Snake
from apple import Apple


def main():
    try:
        # Create the new Gui and start it. This clears the screen
        # and the Gui now controls the screen
        gui = Gui()

        # Create the room, the snake and the apple.
        # You will need to change the constructors later to pass more
        # information to the Snake and Apple constructors
        room = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")
        snake = Snake()
        apple = Apple()

        # The main loop of the game. Use "break" to break out of the loop
        continuePlaying = True
        while continuePlaying:
            # Get a key press from the user
            c = gui.get_keypress()
            # Do something with the key press
            # if c == 'q':
            #     do something if the user wants to quit
            # elif c == "KEY_UP":
            #   do something depending on what was pressed,
            #     e.g. you may want to change the direction of the snake
            # elif c == "KEY_DOWN":
            #     do something else

            # Add your code to move the snake
            # around the screen here.
            # snake.move();

            # The redraw part of the game. First clear the screen
            gui.clear()

            # Redraw everything on the screen into an offscreen buffer,
            # including the room, the Snake and the apple
            room.draw(gui)
            apple.draw(gui)
            snake.draw(gui)

            # When done redrawing all the elements of the screen, refresh will
            # make the new graphic appear on the screen all at once
            gui.refresh()

            # Detect whether the snake ate the apple, or it hit the wall
            # or it hit its own tail here

            # This call makes the program go quiescent for some time, so
            # that it doesn't run so fast. If the value in the call to
            # time.sleep is decreased, the game will speed up.
            time.sleep(0.1)

    except Exception as e:
        # Some error occured, so we catch it, clear the screen,
        # print the log output, and then reraise the Exception
        # This will cause the program to quit and the error will be displayed
        gui.quit()
        raise e

    # Stop the GUI, clearing the screen and restoring the screen
    # back to its original state. Print the saved log output
    gui.quit()

    # The game has ended since we broke out of the main loop
    # Display the user's score here


if __name__ == "__main__":
    main()
