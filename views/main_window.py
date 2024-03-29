from tkinter import *
from contollers.main_controller import add_game
from globals import *
from views.add_game_window import add_game_window


def create_main_window():
    root = Tk()
    root.title("DiOnysus")
    root.config(bg=darker)

    return root


def draw_main_window(root):
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    left_frame = Frame(root, width=220, height=800, bg=darker)
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

    left_frame.columnconfigure(0, weight=1)
    left_frame.rowconfigure(1, weight=1)

    # Create label above the tool_bar
    Label(left_frame, text="Owned Games", bg=darker, fg=white, font='Helvetica 16 bold') \
        .grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=NSEW)

    # Create a frame in the left frame for listing the added games
    game_bar = Frame(left_frame, width=200, height=708, bg=dark, highlightthickness=0)
    game_bar.grid(row=1, column=0, columnspan=2, padx=0, pady=5, sticky=NSEW)

    # Add a button to the left bottom of the left frame
    add_game_button = Button(left_frame, text="Add", bg=darker, command=lambda: add_game(root), fg=white,
                             font='Helvetica 12')
    add_game_button.grid(row=2, column=0, padx=0, pady=(8, 2), sticky=W)

    # Add a button to the right bottom of the left frame
    remove_game_button = Button(left_frame, text="Remove", bg=darker, command=lambda: remove_game(root), fg=white,
                                font='Helvetica 12')
    remove_game_button.grid(row=2, column=1, padx=0, pady=(8, 2), sticky=E)

    right_frame = Frame(root, width=1230, height=790, bg=dark)
    right_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky=NSEW)

    return root


def remove_game(root):
    pass
