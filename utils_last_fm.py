import os
import requests
import time
import pandas as pd
import ast
from dotenv import load_dotenv

load_dotenv()

def get_top_tags_lastfm(artist, track):
    # Desde .env carga las variables
    api_key_lastfm = os.getenv('API_KEY_LASTFM')
    
    # Tags más populares de la pista
    url = f'https://ws.audioscrobbler.com/2.0/?method=track.getTopTags&api_key={api_key_lastfm}&artist={artist}&track={track}&format=json'

    response = requests.get(url)
    if response.status_code == 200:

        tags = response.json()
        if 'toptags' in tags and tags['toptags']['tag']:
            # Top son solo las primeras 4 tags
            top_tags = tags['toptags']['tag'][:4]  
            return [tag['name'] for tag in top_tags]
        else:
            return []  
    else:
        raise Exception(f'Error: {response.status_code} - {response.text}')  
    

def get_top_tracks_lastfm(genre):
    
    # Load the API key from environment variables
    api_key_lastfm = os.getenv('API_KEY_LASTFM')
    if not api_key_lastfm:
        raise ValueError("The Last.fm API key is not set in the environment variables.")
    
    # Initialize an empty list for tracks
    top_tracks = []
    
    # URL to get the top tracks for the specified genre
    url = f'https://ws.audioscrobbler.com/2.0/?method=tag.getTopTracks&tag={genre}&api_key={api_key_lastfm}&format=json&page=1'
    
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        tracks = response.json()
        
        if 'tracks' in tracks and tracks['tracks']['track']:
            # Get the first 50 tracks
            for track in tracks['tracks']['track'][50:100]:
                time.sleep(2)  
                top_tracks.append((track['name'], genre, track['artist']['name']))
            return top_tracks  # Return the list of top tracks
        else:
            print("No tracks found.")
            return None  # Return None if no tracks found
    else:
        print(f'Error querying the API: {response.status_code} - {response.text}')
        return None  # Exit on error
    

def get_all_top_tracks(genres):
    all_top_tracks = []
    for genre in genres:
        tracks = get_top_tracks_lastfm(genre)
        if tracks:  # Only add if tracks were found
            all_top_tracks.extend(tracks)  # Agregar los tracks encontrados a la lista total
    return all_top_tracks
