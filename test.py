from gui import Gui
import time


def main():
    gui = Gui()
    try:
        gui.clear()
        gui.draw_line("@", 0, 0, gui.get_width() - 1, gui.get_height() - 1,
            "WHITE", "GREEN")
        gui.refresh()

        gui.log("Wait for key")
        while True:
            c = gui.get_keypress()
            gui.log("key=" + str(c))
            if c != "":
                break
            time.sleep(0.1)

    except Exception as e:
        gui.quit()
        raise e
    gui.quit()

if __name__ == "__main__":
    main()
