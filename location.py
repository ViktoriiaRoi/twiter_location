'''
This module triggers a get request to Twitter API
Find name and location of user friends
'''
import requests

BASE_URL = 'https://api.twitter.com/'

def main(username: str, bearer_token: str) -> dict:
    '''
    Return a dict where is information about user's friends:
    key - username of friend
    value - location of friend
    '''

    search_url = f'{BASE_URL}1.1/friends/list.json'

    search_headers = {
        'Authorization': 'Bearer ' + bearer_token
    }
    search_params = {
        'screen_name': username,
        'count': 200
    }

    response = requests.get(search_url, headers= search_headers, params=search_params)
    if response.status_code != 200:
        return None

    json_response = response.json()
    users_info = json_response['users']

    friends_location = {}
    for user in users_info:
        loc = user['location']
        if loc:
            friends_location[user['name']] = loc

    return friends_location
