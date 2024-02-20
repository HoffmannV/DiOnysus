from tkinter import *
from global_variables import *


def create_main_window():
    root = Tk()
    root.title("DyOnysus")
    root.config(bg=darker)

    # Create Frame widget
    left_frame = Frame(root, width=200, height=800, bg=darker)
    left_frame.grid(row=0, column=0, padx=5, pady=5)

    # Create a frame in the left frame for listing the added games
    game_bar = Frame(left_frame, width=180, height=708, bg=dark, highlightthickness=0)
    game_bar.grid(row=2, column=0, padx=0, pady=5)

    # Add a button to the left bottom of the left frame
    add_game_button = Button(left_frame, text="Add", bg=darker, fg=white, font='Helvetica 12')
    add_game_button.grid(row=3, column=0, padx=0, pady=0, sticky="W")

    # Add a button to the right bottom of the left frame
    remove_game_button = Button(left_frame, text="Remove", bg=darker, fg=white, font='Helvetica 12')
    remove_game_button.grid(row=3, column=0, padx=0, pady=0, sticky="E")

    # Create label above the tool_bar
    Label(left_frame, text="Owned Games", bg=darker, fg=white, font='Helvetica 16 bold') \
        .grid(row=1, column=0, padx=5, pady=5)

    right_frame = Frame(root, width=1200, height=790, bg=dark)
    right_frame.grid(row=0, column=1, padx=(0, 5), pady=5)

    return root
