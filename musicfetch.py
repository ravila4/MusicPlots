#!/usr/bin/env python3

'''
 Ricardo Avila
 April 26, 2016
 musicfetch.py
 --------------
 Makes API calls to Last.fm and Spotify to get a list of
 top songs and their audio features, and saves the data to a JSON file.
'''

import os
import pylast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

'''
 Last.fm and Spotify require a set of keys to make API calls
 these may be input directly, or passed as os environment variables.
'''

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


# Gets the top tracks played by the user from Last.fm in a given time period
# Possible time periods: overall, 7day, 1month, 3month, 6month, 12month
# Returns a list of dictionaries containing artist, title, and user playcount.
def get_user_top_tracks(username, number, time_period):
    # Create an empty list to store tracks
    top_tracks = []
    response = lastfm_network.get_user(
        username).get_top_tracks(period=time_period, limit=number)
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
        # Set the initial value of the track id to not available
        track['tid'] = "n/a"
        # Search using artist and title string
        results = sp.search("artist:" + track['artist'] +
                            " track:" + track['title'], limit=1)
        for i in results['tracks']['items']:
            print("-> Found:", i['name'])
            # Add ID to dictionary
            track['tid'] = i['uri']
        if track['tid'] == "n/a":
            print("X- Not found.")


# Search Spotify for audio features given a list of track IDs
def get_audio_features(tracks):
    # Create a list of track IDs from the keys in the dictionary
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
        try:
            # Match response dictionary to current track dictionary
            curr_dict = response[tracks.index(track)]
            # Make a new response dictionary using only the chosen keys
            new_dict = dict([(key, curr_dict[key]) for key in feats])
            # Append new dictionary to main track dictionary
            track.update(new_dict)
        except:
            # There is no track ID, so no audio features could be fetched
            pass


# Fetch user's top tracks
my_top_tracks = get_user_top_tracks(LASTFM_USERNAME, 100, "overall")
# Get Spotify IDs
get_spotify_id(my_top_tracks)
# Get audio features
get_audio_features(my_top_tracks)

# Print final contents in JSON format, for readability
print("Final data structure:\n")
print(json.dumps(my_top_tracks, indent=2))

# Write JSON data to file
with open("my_top_tracks.txt", "w") as outfile:
    json.dump(my_top_tracks, outfile)
