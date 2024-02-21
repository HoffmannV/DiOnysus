from tkinter import Frame, Entry, Button, N, S, E, W, PhotoImage, Label
from contollers.add_game_controller import return_to_main
from globals import *


def add_game_window(parent_window):
    search_icon = PhotoImage(file='./assets/search_icon.png')

    # Create a frame in the left frame for listing the added games
    left_frame = Frame(parent_window, width=460, height=800, bg=dark)
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)

    Label(left_frame, text="Search for a game:", font="Helvetica 18 bold", bg=dark, fg=white)\
        .grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N+E+W)

    search_bar = Entry(left_frame, bg=blue, width=28, font='Helvetica 16')
    search_bar.grid(row=1, column=0, padx=10, pady=5, sticky=N+W)

    search_button = Button(left_frame, image=search_icon, bg=blue)
    search_button.image = search_icon
    search_button.grid(row=1, column=1, padx=5, pady=5, sticky=N+E)

    Label(left_frame, text="Results:", font="Helvetica 18 bold", bg=dark, fg=white)\
        .grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky=N+W)

    right_frame = Frame(parent_window, width=960, height=800, bg=dark)
    right_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky=N+S+E+W)

    game_info_frame = Frame(right_frame, width=910, height=740, bg=dark)
    game_info_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N+E+W)

    # Button to return to the main_menu
    back_to_main_button = Button(right_frame, text="Back", command=lambda: return_to_main(parent_window),
                                 fg=white, bg=darker, font='Helvetica 12')
    back_to_main_button.grid(row=1, column=0, padx=5, pady=5, sticky=S+W)

    # Button to add games
    ## Note: No implementation yet only returns to the main menu
    back_to_main_button = Button(right_frame, text="Add Game", command=lambda: return_to_main(parent_window),
                                 fg=white, bg=darker, font='Helvetica 12')
    back_to_main_button.grid(row=1, column=2, padx=5, pady=5, sticky=S+E)

