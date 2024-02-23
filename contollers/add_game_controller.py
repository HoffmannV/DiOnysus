import time
import urllib.request

from globals import clear_window, search_for_games
from views import main_window
from views import add_game_window


def return_to_main(window):
    clear_window(window)
    main_window.draw_main_window(window)


def search_for_game(window, game_name):
    raw_results = search_for_games(game_name)
    results = []
    for result in raw_results:
        results.append(result['name'])

    add_game_window.add_game_window(window, results, found_data=raw_results, search_keyword=game_name)


def game_selected_clicked(window, search_results, selected_game, raw_search_data, search_keyword):
    game_data = {}

    for game in raw_search_data:
        if game['name'] == selected_game:
            game_data['name'] = game['name']
            game_data['release_date'] = time.gmtime(game['first_release_date'])
            game_data['genres'] = game['genres']
            game_data['platforms'] = game['platforms']
            # game_data['image'] = game['image_url']
            game_data['summary'] = game['summary']
            break

    add_game_window.add_game_window(window, search_results=search_results, game_info=game_data,
                                    found_data=raw_search_data, search_keyword=search_keyword)
