from tkinter import Frame, Entry, Button, N, S, E, W, PhotoImage, Label, Text, END
from contollers.add_game_controller import *
from globals import *


def add_game_window(parent_window, search_results=None, game_info=None, found_data=None, search_keyword=""):
    if found_data is None:
        found_data = {}
    if search_results is None:
        search_results = []
    if game_info is None:
        game_info = {}

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
    left_frame.grid_rowconfigure(3, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)

    Label(left_frame, text="Search for a game:", font="Helvetica 18 bold", bg=dark, fg=white)\
        .grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N+E+W)

    search_bar = Entry(left_frame, bg=blue, width=28, font='Helvetica 17')
    search_bar.insert(0, search_keyword)
    search_bar.grid(row=1, column=0, padx=10, pady=5, sticky=N+W+E)

    # Search button positioned in the left column calls the controller to search the database for game
    # that was entered in the search bar left to it
    search_button = Button(left_frame, image=search_icon, bg=blue, command=lambda: search_for_game(parent_window, search_bar.get()))
    search_button.image = search_icon
    search_button.grid(row=1, column=1, padx=(0, 10), pady=5, sticky=N+W+E)

    Label(left_frame, text="Results:", font="Helvetica 18 bold", bg=dark, fg=white)\
        .grid(row=2, column=0, columnspan=2, padx=8, pady=10, sticky=N+W)

    search_result_frame = Frame(left_frame, width=200, height=600, bg=white)
    search_result_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10), sticky=N+W+E+S)

    search_result_frame.columnconfigure(0, weight=1)
    row_counter = 0
    for result in search_results:
        Button(search_result_frame, text=result, cursor="hand2", font="Helvetica 14",
               command=lambda r=result: game_selected_clicked(parent_window, search_results, r, found_data, search_keyword))\
            .grid(row=row_counter, column=0, padx=0, pady=0, sticky=N+W+E)
        row_counter += 1

    # Creating a right frame it will contain the data about the selected game
    right_frame = Frame(parent_window, width=960, height=800, bg=dark)
    right_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky=N+S+E+W)

    right_frame.grid_rowconfigure(0, weight=1)
    right_frame.grid_columnconfigure(1, weight=1)

    game_info_frame = Frame(right_frame, width=910, height=740, bg=darker)
    game_info_frame.grid(row=0, columnspan=2, padx=10, pady=(10, 0), sticky=N+E+S+W)

    game_info_frame.grid_rowconfigure(6, weight=1)
    game_info_frame.grid_columnconfigure(0, weight=1)
    if game_info:
        label_title_name = Label(game_info_frame, text="Name:", font="Helvetica 16 bold", bg=darker, fg=white)
        label_title_name.grid(row=0, column=0, padx=20, pady=(20, 10), sticky=N+W)

        label_name = Label(game_info_frame, text=game_info["name"], font="Helvetica 16", bg=darker, fg=white)
        label_name.grid(row=1, column=0, padx=20, pady=(0, 10), sticky=N + W)

        label_release_year = Label(game_info_frame, text="Release: {0}".format(time.strftime('%Y-%m-%d', game_info["release_date"])), font="Helvetica 12 bold", bg=darker, fg=white)
        label_release_year.grid(row=2, column=0, padx=20, pady=(0, 10), sticky=N + W)

        label_genres = Label(game_info_frame, text="Genres: {0}".format(game_info["genres"]), font="Helvetica 12 bold", bg=darker, fg=white)
        label_genres.grid(row=3, column=0, padx=20, pady=(0, 10), sticky=N + W)

        label_platforms = Label(game_info_frame, text="Platforms: {0}".format(game_info["platforms"]), font="Helvetica 12 bold", bg=darker, fg=white)
        label_platforms.grid(row=4, column=0, padx=20, pady=(0, 10), sticky=N + W)

        # image_data = base64.b64decode(game_info['image'])
        # game_image = PhotoImage(data=image_data)

        # image goes here with row=0, column=1, rowspan=6 atm just a placeholder Frame
        image_frame = Frame(game_info_frame, bg=white, width=400, height=400)
        image_frame.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky=N+E+W)

        #Label(image_frame, image=game_image)

        frame_details = Frame(game_info_frame, bg=dark, width=890)
        frame_details.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=N + W + S + E)

        frame_details.grid_columnconfigure(0, weight=1)

        label_details = Label(frame_details, text="Summary:", font="Helvetica 14 bold", bg=dark, fg=white)
        label_details.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=N + W)

        text_details = Text(frame_details, font="Helvetica 12", bg=dark, fg=white)
        text_details.insert(END, game_info["summary"])
        text_details.grid()

    # Button to return to the main_menu
    back_to_main_button = Button(right_frame, text="Back", command=lambda: return_to_main(parent_window),
                                 fg=white, bg=darker, font='Helvetica 12')
    back_to_main_button.grid(row=1, column=0, padx=10, pady=(0, 10), sticky=S+W)

    # Button to add games
    # Note: No implementation yet. Only returns to the main menu
    back_to_main_button = Button(right_frame, text="Add Game", command=lambda: return_to_main(parent_window),
                                 fg=white, bg=darker, font='Helvetica 12')
    back_to_main_button.grid(row=1, column=1, padx=10, pady=10, sticky=E+S)

