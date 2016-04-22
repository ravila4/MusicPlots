#!/usr/bin/env python3

'''
 Ricardo Avila
 April 15, 2016
 Practice API calls to Spotify
'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os

# Access API keys  stored in os environment variables.
CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']

# Authorization
client_credentials = SpotifyClientCredentials(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)
sp.trace = False

# Create an empty list to store Spotify song IDs
tids = []

# Search for songs by an artist and append their ID to the list
results = sp.search("Bitter Ruin Pushin' Out the Light", limit=1)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
    tids.append(t['uri'])

print(tids)

# Search for audio features for each song in the ID list
# This creates a list of dictionaries 
song_list = sp.audio_features(tids)

for song in song_list:
    # Print response in JSON format
    print(json.dumps(song, indent=4))
    
    # Print specific values from the dictionary
    print("acousticness =", song['acousticness'])
    print("liveness =", song["liveness"])
    print("key = ", song["key"])
    print("valence =", song["valence"])
    print("loudness =", song["loudness"])
    print("speechiness =", song["speechiness"])
    print("time signature =", song["time_signature"])
    print("danceability =", song["danceability"])
    print("energy =", song["energy"])
    print("tempo =", song["tempo"])

