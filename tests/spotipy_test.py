#!/usr/bin/env python3

# Ricardo Avila
# April 15, 2016
# Practice API calls to spotify

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os

# Access API keys in os environment variables.
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
results = sp.search('Amanda Palmer', limit=20)
for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'])
        tids.append(t['uri'])

print(tids)

features = sp.audio_features(tids)
print(json.dumps(features, indent=4))

