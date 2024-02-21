from tkinter import Frame, Entry, Button, N, S, E, W, PhotoImage, Label
from contollers.add_game_controller import return_to_main
from globals import *


def add_game_window(parent_window):
    # Making the left and right frames resize correctly
    parent_window.rowconfigure(0, weight=1)
    parent_window.columnconfigure(0, weight=1)
    parent_window.columnconfigure(1, weight=1)

    # Loading a image for the search icon
    search_icon = PhotoImage(file='./assets/search_icon.png')

    # Create a frame in the left frame for listing the added games
    left_frame = Frame(parent_window, width=460, height=800, bg=dark)
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)

    # Making the elements in the left frame resize correctly
    left_frame.rowconfigure(3, weight=1)
    left_frame.columnconfigure(0, weight=1)

    Label(left_frame, text="Search for a game:", font="Helvetica 18 bold", bg=dark, fg=white)\
        .grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N+E+W)

    search_bar = Entry(left_frame, bg=blue, width=28, font='Helvetica 17')
    search_bar.grid(row=1, column=0, padx=10, pady=5, sticky=N+W+E)

    search_button = Button(left_frame, image=search_icon, bg=blue)
    search_button.image = search_icon
    search_button.grid(row=1, column=1, padx=(0, 10), pady=5, sticky=N+W+E)

    Label(left_frame, text="Results:", font="Helvetica 18 bold", bg=dark, fg=white)\
        .grid(row=2, column=0, columnspan=2, padx=8, pady=10, sticky=N+W)

    search_result_frame = Frame(left_frame, width=200, height=600, bg=white)
    search_result_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10), sticky=N+W+E+S)

    # Creating a right frame it will contain the data about the selected game
    right_frame = Frame(parent_window, width=960, height=800, bg=dark)
    right_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky=N+S+E+W)

    right_frame.rowconfigure(0, weight=1)
    right_frame.columnconfigure(1, weight=1)

    game_info_frame = Frame(right_frame, width=910, height=740, bg=darker)
    game_info_frame.grid(row=0, columnspan=3, padx=10, pady=(10, 0), sticky=N+E+S+W)

    # Button to return to the main_menu
    back_to_main_button = Button(right_frame, text="Back", command=lambda: return_to_main(parent_window),
                                 fg=white, bg=darker, font='Helvetica 12')
    back_to_main_button.grid(row=1, column=0, padx=10, pady=10, sticky=S+W)

    # Button to add games
    ## Note: No implementation yet only returns to the main menu
    back_to_main_button = Button(right_frame, text="Add Game", command=lambda: return_to_main(parent_window),
                                 fg=white, bg=darker, font='Helvetica 12')
    back_to_main_button.grid(row=1, column=2, padx=10, pady=10, sticky=E+S)

