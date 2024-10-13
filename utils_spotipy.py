import spotipy
import pandas as pd
import numpy as np
import time
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()  

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Spotify API 
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


#Initialize SpotiPy with user credentials
SP = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))


def get_track_details_spotify(name_string,sp=sp):
    result= SP.search(q=f'{name_string}', limit=1)
    track=result['tracks']['items'][0]

    return {
        'id': track['id'],
        'name': track['name'],
        'album': track['album']['name'],
        'popularity': track['popularity'],
        'artists': [artist['name'] for artist in track['artists']],
        'release_date': track['album']['release_date'],
    }

def get_track_analysis_spotify(id):
    """
    Fetch the audio features for a given track id.

    Parameters
    ----------
    id : str
        The Spotify track ID.
    sp : SpotifyClientCredentials
        Spotify client credentials object.

    Returns
    -------
    dict
        Audio features of the track.
    """

    result= SP.audio_features(id)[0]
    return {
        'danceability': result['danceability'],
        'energy':result['energy'],
        'key': result['key'],
        'loudness': result['loudness'],
        'mode': result['mode'],
        'speechiness':result['speechiness'],
        'acousticness': result['acousticness'],
        'instrumentalness': result['instrumentalness'],
        'liveness': result['liveness'],
        'valence': result['valence'],
        'tempo': result['tempo'],
        'duration': result['duration_ms']
    }

def create_track_complete_analysis_spotify(df):

    # if there's a csv file, we can use it as starting point.
    if "id" not in df.columns:
        df["id"] = np.nan

    # Lista de diccionarios de cada canción 

    for i in range(len(df)):
        if pd.isna(df.loc[i,"id"]):
            try:
                song = df.loc[i,"Title"] + " " + df.loc[i,"Artist"]

                # Info de la canción
                track_details = get_track_details_spotify(song)
                id = track_details['id']  # id de la canción que usamos para analysis
                
                # Llamamos a las funciones de genre y analysis
                track_genre = get_track_analysis_spotify(id)
                
                # Añadimos toda la info en el df
                df.loc[i, "id"] = track_details['id']
                df.loc[i,'title_spotify'] = track_details['name']
                df.loc[i,"album"] = track_details['album']
                df.loc[i,'sp_popularity'] = track_details['popularity']
                df.loc[i,"colab"] = ("Y" if len(track_details['artists']) > 1 else "N")
                df.loc[i,"release_date"] = track_details['release_date']
                df.loc[i,"danceability"] = track_genre['danceability']
                df.loc[i,'energy'] = track_genre['energy']
                df.loc[i,'loudness'] = track_genre['loudness']
                df.loc[i,'speechiness'] = track_genre['speechiness']
                df.loc[i,'acousticness'] = track_genre['acousticness']
                df.loc[i,'instrumentalness'] = track_genre['instrumentalness']
                df.loc[i,'liveness'] = track_genre['liveness']
                df.loc[i,'valence'] = track_genre['valence']
                df.loc[i,'key'] = track_genre['key']
                df.loc[i,'mode'] = track_genre['mode']
                df.loc[i,'tempo'] = track_genre['tempo']
                df.loc[i,'duration']= track_genre['duration']
            
                df.to_csv("spotify.csv", index=False)
                time.sleep(3)

            except Exception as e:
                print(f"Error obteniendo detalles para '{song}': {e}")

    # Convertir la lista de diccionarios en un DataFrame
    return df