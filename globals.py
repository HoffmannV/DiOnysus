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


def get_all_games(auth_token, min_id, max_id):
    url = 'https://api.igdb.com/v4/games'

    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {auth_token}'
    }

    params = {
        'fields': f'*; where id <= {max_id} & id >= {min_id}; sort id asc;',
        'limit': '500'
    }

    return requests.post(url, params=params, headers=headers)
