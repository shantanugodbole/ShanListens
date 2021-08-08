import tweepy
import requests
import time
# from configparser import ConfigParser

# configur = ConfigParser()
# print (configur.read('config.ini'))
# print ("Sections : ", configur.sections())
# print ("Installation Library : ", configur.get('keys','API_KEY'))

# API_KEY = configur.get('keys', 'API_KEY')
# API_SECRET_KEY = configur.get('keys', 'API_SECRET_KEY')
# ACCESS_TOKEN = configur.get('keys', 'ACCESS_TOKEN')
# ACCESS_TOKEN_SECRET = configur.get('keys', 'ACCESS_TOKEN_SECRET')

API_KEY = "0fRg4S3x3fpavfD2wj84Pc5H3"
API_SECRET_KEY = "EYVJMmTuIzMeIL5LuWciNTY1X2OfjP6jDG6vg2QaxgWhnQ2kxV"
ACCESS_TOKEN = "1407756418569048067-ZbPnVjXxhG4sPyW54IQykd5AljECBi"
ACCESS_TOKEN_SECRET = "6wB29PK9S6SGEeZNksxipkTD4FAtOy3KUyFyZK4ge84Ay"
# print(API_KEY)
# print(API_SECRET_KEY)
# print(ACCESS_TOKEN)
# print(ACCESS_TOKEN_SECRET)
auth = tweepy.auth.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
previousSongName = ""
# Fetching the playing song
while(1):
    response = requests.get("https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=shangod12&api_key=b4a65f0d1469c897f0bbf25cc52bcb80&format=json")
    recentTracks = response.json()
    lastTrack = recentTracks['recenttracks']['track'][0]
    artistName = lastTrack['artist']['#text']
    albumName = lastTrack['album']['#text']
    songName = lastTrack['name']
    if(songName != previousSongName):
        status = "🔊 " + songName + " by " + artistName + "\n"  + "📀 " + albumName
        api.update_status(status)
        previousSongName = songName
    else:
        pass
    time.sleep(200)