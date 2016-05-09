# Music Plots

Final project for CS 1310.

Consists of a few scripts using Python and the matplotlib module for visualizing music data from the the Last.fm and Spotify APIs. The data is fetched using the python script <musicfetch.py> and 


## Goals

The goal of these visualizations is to explore trends in the audio features of music tracks. The Last.fm API is useful because it allows a user to keep track of the music he/she listens to across various devices. Spotify is useful because their music recommendation system uses algorithms to fingerprint and classify music tracks acording to several audio features.

Some of these features are:

- Danceability - How suitable a track is for dancing.

- Energy - A perceptual measure of intensity and powerful activity released throughout the track.

- Speechiness - The presence of spoken words in a track.

- Liveness - The presence of an audience in the recording.

- Acousticness - The likelihood a recording was created by solely acoustic means.

- Valence - The musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g., happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).


Using these abstractions, we can create various plots that help us understand the relationships between the avoustic features of tracks, and also get a feel for the 


## Requirements

Python modules used in the visualizations:

- matplotlib
- numpy
- json (for reading and storing data)
- ipywidgets (ipython notebook
- mpld3

