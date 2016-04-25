#!/usr/bin/env python3

import os
import pylast

# Requires two unique values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm

API_KEY = os.environ['LASTFM_KEY']
API_SECRET = os.environ['LASTFM_SECRET']

# Username and password MD5 hash
lastfm_username = os.environ['LASTFM_USER']
lastfm_password_hash = os.environ['LASTFM_HASH']

# Authentication:
lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY, api_secret=API_SECRET,
    username=lastfm_username, password_hash=lastfm_password_hash)


# Get the top tracks played,
# and append the object's attributes to the appropriate list
def get_top_tracks(username, number):
    top_tracks = lastfm_network.get_user(
        username).get_top_tracks(limit=number)
    for (track, user_playcount) in top_tracks:
        artist = pylast.Track.get_artist(track)
        artists.append(str(artist))
        title = pylast.Track.get_title(track)
        songs.append(str(title))
        overall_playcount = pylast.Track.get_playcount(track)
        overall_playcounts.append(overall_playcount)
        listener_count = pylast.Track.get_listener_count(track)
        listener_counts.append(listener_count)
        my_playcounts.append(user_playcount)


# Define empty lists to hold the values
artists = []
songs = []
my_playcounts = []
overall_playcounts = []
listener_counts = []

get_top_tracks(lastfm_username, 50)

print("artists = ", artists, "\n")
print("song titles = ", songs, "\n")
print("my playcounts = ", my_playcounts, "\n")
print("overall playcounts = ", overall_playcounts, "\n")
print("listener counts = ", listener_counts, "\n")
