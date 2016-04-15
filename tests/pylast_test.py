#!/usr/bin/env python3

import pylast

# Authentication:

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm

API_KEY = "137465300856b0ecd99ed0372adc2d45"
API_SECRET = "54f02ffb4e8362c82192b141c8f5cb3b"

lastfm_username = "Aeneas42"
lastfm_password_hash = pylast.md5("pg5G#f7e#KuyKD")

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
        musicbrainzid = pylast.Track.get_mbid(track)
        musicbrainz_ids.append(str(musicbrainzid))
        overall_playcount = pylast.Track.get_playcount(track)
        overall_playcounts.append(overall_playcount)
        listener_count = pylast.Track.get_listener_count(track)
        listener_counts.append(listener_count)
        my_playcounts.append(user_playcount)


# Define empty lists to hold the values
artists = []
songs = []
my_playcounts = []
musicbrainz_ids = []
overall_playcounts = []
listener_counts = []

get_top_tracks(lastfm_username, 50)

print("artists = ", artists, "\n")
print("song titles = ", songs, "\n")
print("my playcounts = ", my_playcounts, "\n")
print("musicbrainz IDs = ", musicbrainz_ids, "\n")
print("overall playcounts = ", overall_playcounts, "\n")
print("listener counts = ", listener_counts, "\n")
