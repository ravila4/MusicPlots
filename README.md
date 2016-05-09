# Music Plots

Consists of a few scripts using Python's matplotlib module for visualizing music data from the the Last.fm and Spotify APIs. The data was fetched using the python script "musicfetch.py" and saved to a text file.

## Goals

The goal of these visualizations is to explore trends in the audio features of music tracks, this has useful applications in creating intelligent and personalized music services. The Last.fm API is used because it allows a user to keep track of the music he/she listens to across various devices, and stores several statistics about the user's listening habits. Spotify is useful because its music recommendation system uses algorithms to fingerprint and classify music tracks according to several audio features.

Some of these audio features are:

- Danceability - How suitable a track is for dancing.
- Energy - A perceptual measure of intensity and powerful activity released throughout the track.
- Speechiness - The presence of spoken words in a track.
- Liveness - The presence of an audience in the recording.
- Acousticness - The likelihood a recording was created by solely acoustic means.
- Valence - The musical positiveness conveyed by a track (how "happy" or "sad" it sounds).

Using this data, we can create visualizations to answer questions such as "Is there a relationship between the energy and acousticness of music tracks?" or "Does the user have have a bias towards a certain type of music, such as higher valence (happier), or more acoustic songs?" Of course, features such as "danceability", "acousticness" and "valence" are highly complex and abstract, and the results obtained are dependent on the validity of the algorithms used by Spotify to analyze the tracks.
  
## Screenshots

The first plot created is a simple bar chart to display the user's most listened tracks:

![Bar Chart](https://cloud.githubusercontent.com/assets/9020496/15120591/109e7002-15dc-11e6-8233-66aed5f05ecb.png)

To analyze the relationship between the different audio features, an interactive scatter plot is created, which allows the user to change the value of the data plotted on each of the axes, as well as the color of the data points.

Sample scatter plot generated using interactive widgets:

![Interactive Plot](https://cloud.githubusercontent.com/assets/9020496/15120590/10784dfa-15dc-11e6-91dd-fdc38674f967.png)


## Conclusions

Using my data set, several trends are observed from the scatter plots: Higher energy tracks tend to be louder, and less acoustic. Higher valence songs tend to be louder, higher in energy, and higher in danceability, however, 
lower valence songs can be either low or high in any of these values. These results are not objective, and could likely be a result of my own preferences in music. In order to produce generalizable results, we would require a random data set.


## Requirements

Interfaces for the Last.fm and Spotify web APIs:

- [spotipy](https://github.com/plamere/spotipy.git)
- [pylast](https://github.com/pylast/pylast.git)

Modules used in the visualizations:

- matplotlib
- numpy
- json (for reading and storing data)
- [ipywidgets](https://github.com/ipython/ipywidgets.git) - for interactive widgets. Requires the Jupyter (IPython) notebook: http://jupyter.org/


## Future Work

It would be interesting to make a network graph of the artists, using the "similar artists" feature of the Last.fm API. This would allow us to explore how different artists are similar to each other.
The data could be used to create a desktop application that generates smart playlists. It would be interesting to see if better playlists can be generated using a network of similar artists, or by fetching songs with similar audio features.
