from globals import clear_window
from views import main_window


def return_to_main(window):
    clear_window(window)
    main_window.draw_main_window(window)
