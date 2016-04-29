#!/usr/bin/env python3

'''
Ricardo Avila
April 26, 2016
'''

import os
import pylast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Retrieve authentication keys stored in os environment variables:

# Last.fm API keys, username and password
LASTFM_API_KEY = os.environ['LASTFM_KEY']
LASTFM_API_SECRET = os.environ['LASTFM_SECRET']
LASTFM_USERNAME = os.environ['LASTFM_USER']
LASTFM_PASSWORD_HASH = os.environ['LASTFM_HASH']

# Spotify API keys
SPOTIFY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']

# Last.fm authentication:
lastfm_network = pylast.LastFMNetwork(
    api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET,
    username=LASTFM_USERNAME, password_hash=LASTFM_PASSWORD_HASH)

# Spotify authentication:
client_credentials = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)
sp.trace = False


# Get the top tracks played by the user from Last.fm
# Returns a list of dictionaries containing track attributes.
def get_top_tracks(username, number):
    # Create an empty list to store tracks
    top_tracks = []
    response = lastfm_network.get_user(
        username).get_top_tracks(limit=number)
    for (track, user_playcount) in response:
        artist = pylast.Track.get_artist(track)
        title = pylast.Track.get_title(track)
        # Make a dictionary and append to list
        top_tracks.append({'artist': str(artist), 'title': str(title),
                          'user_playcount': user_playcount})
    return(top_tracks)


# Search for tracks in Spotify and add their ID to the respective dictionary
def get_spotify_id(tracks):
    for track in tracks:
        # Print status
        print("Searching Spotify for: ", track['title'], "by", track['artist'])
        # Search using artist and title string
        results = sp.search("artist:" + track['artist'] +
                            " track:" + track['title'], limit=1)
        for i in results['tracks']['items']:
            print("-> Found:", i['name'])
            # Add track ID as a new item in dictionary
            track['tid'] = i['uri']


# Search Spotify for audio features given a list of track IDs
def get_audio_features(tracks):
    # Iterate through list of dictionaries and create a list of track IDs
    tids = [track['tid'] for track in tracks]
    print("\nTrack IDs:", tids, "\n")
    # Search for audio features using track ID list
    # The response output is a list of dictionaries
    response = sp.audio_features(tids)
    # Features from the response that we want to store in the main dictionary:
    feats = ("acousticness", "liveness", "key", "valence", "loudness",
             "speechiness", "time_signature", "danceability", "energy",
             "tempo")
    for track in tracks:
        # Match response dictionary to current track dictionary
        curr_dict = response[tracks.index(track)]
        # Make a new response dictionary using only the chosen keys
        new_dict = dict([(key, curr_dict[key]) for key in feats])
        # Append new features dictionary to main track dictionary
        track.update(new_dict)


# Fetch a given number of top tracks for a user
my_top_tracks = get_top_tracks(LASTFM_USERNAME, 5)
print("My top Tracks:", my_top_tracks, "\n")
# Get IDs
get_spotify_id(my_top_tracks)
# Get audio features
get_audio_features(my_top_tracks)
# Print final list contents in JSON format, for readability
print("Final data structure:")
print(json.dumps(my_top_tracks, indent=2))
