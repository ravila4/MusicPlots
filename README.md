# Music Plots

Consists of a few scripts using Python's matplotlib module for visualizing music data from the the Last.fm and Spotify APIs. The data was fetched using the python script <musicfetch.py> and saved to a text file using the JSON format.

## Goals

The goal of these visualizations is to explore trends in the audio features of music tracks, this has useful applications in creating intelligent music services. The Last.fm service allows a user to keep track of the music he/she listens to across various devices, and stores several statistics about the user's listening habits. Spotify is useful because its music recommendation system uses algorithms to fingerprint and classify music tracks acording to several audio features.

Some of these audio features are:

- Danceability - How suitable a track is for dancing.
- Energy - A perceptual measure of intensity and powerful activity released throughout the track.
- Speechiness - The presence of spoken words in a track.
- Liveness - The presence of an audience in the recording.
- Acousticness - The likelihood a recording was created by solely acoustic means.
- Valence - The musical positiveness conveyed by a track (how "happy" or "sad" it sounds).

Using this data, we can create visualizations to answer questions such as:
- Is there a relationship between the energy and acousticness of music tracks?
- Does the user have have a bias towards a certain type of music, such as higher valence (happier) songs?
  
## Screenshots

A bar chart to display the user's most listened tracks:

![Bar Chart](https://cloud.githubusercontent.com/assets/9020496/15120591/109e7002-15dc-11e6-8233-66aed5f05ecb.png)

Sample scatter plot generated using interactive widgets:

![Interactive Plot](https://cloud.githubusercontent.com/assets/9020496/15120590/10784dfa-15dc-11e6-91dd-fdc38674f967.png)


## Requirements

The data was fetched using Python modules for the Last.fm and Spotify web APIs:

- [spotipy](https://github.com/plamere/spotipy.git)
- [pylast](https://github.com/pylast/pylast.git)

Python modules used in the visualizations:

- matplotlib
- numpy
- json (for reading and storing data)
- [ipywidgets](https://github.com/ipython/ipywidgets.git)

Using the interactive widgets requires the Jupyter (IPython) notebook: http://jupyter.org/


## Future Work

It would be interesting to make a network graph of the artists, showing how they are similar to each other.
The data could be used to create a desktop application that generates smart playlists.
