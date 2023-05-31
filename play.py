"""
This is the main program for the snake game.
"""

import time

from gui import Gui
from room import Room
from snake import Snake
from apple import Apple, collides
import wall as Wall



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
        apples = [Apple(gui)]
        walls = []

        # The main loop of the game. Use "break" to break out of the loop
        score = 0
        continuePlaying = True
        lastKey = "KEY_RIGHT"
        initailLength = snake.get_length()
        while continuePlaying:
            # Get a key press from the user
            c = gui.get_keypress()
            # Do something with the key press
            if c == 'q':
                break
            elif c == "KEY_UP" and lastKey != "KEY_DOWN":
                snake.move_up()
                lastKey = c
            elif c == "KEY_DOWN" and lastKey != "KEY_UP":
                snake.move_down()
                lastKey = c
            elif c == "KEY_LEFT" and lastKey != "KEY_RIGHT":
                snake.move_left()
                lastKey = c
            elif c == "KEY_RIGHT" and lastKey != "KEY_LEFT":
                snake.move_right()
                lastKey = c
            else:
                # Move the snake in the direction it was going
                if lastKey == "KEY_UP":
                    snake.move_up()
                elif lastKey == "KEY_DOWN":
                    snake.move_down()
                elif lastKey == "KEY_LEFT":
                    snake.move_left()
                elif lastKey == "KEY_RIGHT":
                    snake.move_right()




            # The redraw part of the game. First clear the screen
            gui.clear()

            # Redraw everything on the screen into an offscreen buffer,
            # including the room, the Snake and the apple
            room.draw(gui)
            for apple in apples:
                apple.draw(gui)
            snake.draw(gui)
            gui.draw_text("Score: " + str(score), 2, gui.get_height() - 2, "WHITE", "BLACK")
            for wall in walls:
                for apple in apples:
                    if collides(apple.get_position(), wall.get_positions()):
                        apple.move(gui, snake)
                wall.draw(gui)

            # When done redrawing all the elements of the screen, refresh will
            # make the new graphic appear on the screen all at once
            gui.refresh()

            # Check if the snake hit a generated wall
            for wall in walls:
                for position in wall.get_positions():
                    if collides(position, snake.get_positions()):
                        continuePlaying = False
                        break



            # Check if the snake ate the apple
            for apple in apples:
                if collides(apple.get_position(), snake.get_positions()):
                    snake.grow()
                    # And move the apple to a new location
                    apple.move(gui, snake)

            # Check if the snake hit the wall
            if snake.get_head().get_x() == 0 or snake.get_head().get_x() == gui.get_width() - 1 or \
                    snake.get_head().get_y() == 0 or snake.get_head().get_y() == gui.get_height() - 1:
                break

            # Check if the snake hit its own tail
            if snake.hit_tail():
                break

            # Check if the snake is about to hit a wall and pause for half a second just like the original game.
            # The snake is about to hit the wall if the snake's head is one space away from the wall and the last key
            # pressed was the key that would move the snake into the wall.
            if (snake.get_head().get_x() == 1 and lastKey == "KEY_LEFT") or \
                    (snake.get_head().get_x() == gui.get_width() - 2 and lastKey == "KEY_RIGHT") or \
                    (snake.get_head().get_y() == 1 and lastKey == "KEY_UP") or \
                    (snake.get_head().get_y() == gui.get_height() - 2 and lastKey == "KEY_DOWN"):
                time.sleep(0.25)

            # For every multiple of 5 points the snake gets, add another apple to the screen
            if score % 5 == 0 and score != 0 and len(apples) < score // 5 + 1:
                apples.append(Apple(gui))
                # Add a wall to the screen every 5 points
                walls.append(Wall.Wall(gui))

            # Set the score to the length of the snake minus the initial length
            score = snake.get_length() - initailLength
            # Pause the game for a bit. The higher the score, the faster the game will go.
            time.sleep(0.1 / (score / 15 + 1))

    except Exception as e:
        # Some error occured, so we catch it, clear the screen,
        # print the log output, and then reraise the Exception
        # This will cause the program to quit and the error will be displayed
        gui.quit()
        raise e
    # Draw an explosion on the screen where the snake died
    gui.draw_text("X", snake.get_head().get_x(), snake.get_head().get_y(), "RED", "BLACK")
    gui.refresh()
    time.sleep(0.5)
    # Stop the GUI, clearing the screen and restoring the screen
    # back to its original state. Print the saved log output
    gui.quit()

    # The game has ended since we broke out of the main loop
    # Display the user's score here
    gui.clear()
    gui.draw_text("Game Over!", gui.get_width() // 2, gui.get_height() // 2, "RED", "BLACK")
    gui.draw_text("Your score was: " + str(score), gui.get_width() // 2, gui.get_height() // 2 + 1, "RED", "BLACK")
    gui.refresh()
    time.sleep(2)


if __name__ == "__main__":
    main()
