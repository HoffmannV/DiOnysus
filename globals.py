import time

import requests
import base64

# Colorpalette
dark = "#393E46"
darker = "#222831"
white = "#EEEEEE"
blue = "#00ADB5"


# get Raw Image Data
def get_raw_image_data(path_to_image):
    with open(path_to_image, "rb") as image_file:
        return base64.b64encode(image_file.read())


# clear the passed window
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


# API Interactions
client_id = "ig7yr29ur3437psfzw181j3h34d5aj"


def twitch_validate(auth_token):
    url = 'https://id.twitch.tv/oauth2/validate'
    headers = {
        'Authorization': 'OAuth {0}'.format(auth_token)
    }
    return requests.get(url, headers=headers)


def twitch_get_new_token(client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    return requests.post('{0}?client_id={1}&client_secret={2}&grant_type=client_credentials'
                         .format(url, client_id, client_secret))


def search_for_games(game_name, auth_token="mabnruzp2fehpsxtvvcq5issge2na1"):
    url = 'https://api.igdb.com/v4/games'

    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {auth_token}'
    }

    params = {
        'fields': '*; search "{0}"; where category != 3;'.format(game_name),
        'limit': '20'
    }

    game_ids = ""
    game_platforms = []
    games = requests.post(url, params=params, headers=headers)

    for i in range(len(games.json())):
        if 'platforms' in games.json()[i].keys():
            for platform in games.json()[i]['platforms']:
                game_platforms.append(platform)
        if i == 0 and len(games.json()) != 1:
            game_ids += f"({games.json()[i]['id']}, "
        elif i == 0 and len(games.json()) == 1:
            game_ids = f"{games.json()[i]['id']}"
        elif i == len(games.json()) - 1:
            game_ids += f"{games.json()[i]['id']})"
        else:
            game_ids += f"{games.json()[i]['id']}, "

    url = 'https://api.igdb.com/v4/covers'
    params = {
        'fields': 'url, game; where game = {0}'.format(game_ids),
        'limit': '10'
    }
    covers = requests.post(url, params=params, headers=headers)

    url = 'https://api.igdb.com/v4/genres'

    params = {
        'fields': 'name',
        'limit': '50'
    }
    genres = requests.post(url, params=params, headers=headers)
    genres_dict = {}
    for genre in genres.json():
        genres_dict[genre['id']] = genre['name']

    url = 'https://api.igdb.com/v4/platforms'
    params = {
        'fields': 'name, abbreviation; where id = {0}'.format(game_ids),
        'limit': '50'
    }
    platforms = requests.post(url, params=params, headers=headers)
    print(platforms.json())

    platforms_dict = {}
    for platform in platforms.json():
        if 'abbreviation' in platform.keys():
            platforms_dict[platform['id']] = platform['abbreviation']
        else:
            platforms_dict[platform['id']] = platform['name']

    result = []
    for i in range(len(games.json())):
        result.append({})
        result[i]['name'] = games.json()[i]['name']
        if 'first_release_date' in games.json()[i].keys():
            result[i]['first_release_date'] = games.json()[i]['first_release_date']
        else:
            result[i]['first_release_date'] = 0
        if 'genres' in games.json()[i].keys():
            result[i]['genres'] = ""
            for genre in games.json()[i]['genres']:
                if result[i]['genres'] == "":
                    result[i]['genres'] += genres_dict.get(genre)
                elif genres_dict.get(genre) == "None":
                    continue
                else:
                    result[i]['genres'] += f", {genres_dict.get(genre)}"
        else:
            result[i]['genres'] = "Not available"
        result[i]['platforms'] = "Not available"
        if 'platforms' in games.json()[i].keys():
            for platform in games.json()[i]['platforms']:
                if result[i]['platforms'] == "":
                    result[i]['platforms'] += platforms_dict.get(platform)
                elif platforms_dict.get(platform) == "None":
                    continue
                else:
                    result[i]['platforms'] += f", {platforms_dict.get(platform)}"
        if 'summary' in games.json()[i].keys():
            result[i]['summary'] = games.json()[i]['summary']
        else:
            result[i]['summary'] = "Not available"
        result[i]['image_url'] = "Not available"
        if games.json()[i]['id']:
            for cover in covers.json():
                if games.json()[i]['id'] == cover['game']:
                    result[i]['image_url'] = cover['url']

    return result

def sanitize_ids(id_string):
    pass