import requests
import time
from flask import Flask, request
from pprint import pprint

app = Flask(__name__)

@app.route('/test/<test>')
def default(test):
    return "Testing Flask App" + test

@app.route('/get_song')
def getSongInfo():
    ACCESS_TOKEN = 'BQBmbDSI0qoZPlKNv6JN_A_BKl-zWlh92kRBmBUFVYg0e4D3SQ3R1hfhRvBQNYxH53oPCXT_MJ7AOXCWvHDEOmfPOs5BDnUh1sHwZKDka7_1MWNcwAFtjCpt0pEgOKHUb8uiidFumVqESwZo6CO6OSZ9QKgnbDSXhUmyHl2kZw'
    current_track_id = None
    current_track_info = get_current_track(ACCESS_TOKEN)
    if current_track_info['id'] != current_track_id:
        # pprint(current_track_info,indent=4)
        current_track_id = current_track_info['id']
        return current_track_info
    
def get_current_track(access_token):
    SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }

    return current_track_info




if __name__ == '__main__':
    app.run(debug=True)