
import musicbrainzngs as mb
import os
import time
from dotenv import load_dotenv
import requests

load_dotenv()

# Obtener los valores del archivo .env
app_name = os.getenv('APP_NAME')
app_version = os.getenv('APP_VERSION')  # Esta es la versión de tu aplicación
contact_info = os.getenv('CONTACT_INFO')

mb.set_useragent(app_name, app_version, contact_info)

def get_track_mbid_acous_brainz(song_name, artist_name):
    time.sleep(2)  # Pausa para no exceder el límite de solicitudes
    try:
        # Realizar la búsqueda con campos específicos
        resultados = mb.search_recordings(recording=song_name, artist=artist_name, limit=5, strict=True)  # Aumentamos el límite para buscar más coincidencias
        
        # Filtrar resultados para obtener el que coincide exactamente con el artista
        for resultado in resultados['recording-list']:
            for artist_credit in resultado['artist-credit']:
                if (artist_credit['artist']['name'].lower() == artist_name.lower() and 
                    resultado['title'].lower() == song_name.lower()):
                    return resultado['id'] 
        
        print(f"No se encontraron resultados exactos para '{song_name}' por '{artist_name}'.")
        return None
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
    

def get_mbid_lista(canciones):
    mbids_list = []
    for cancion in canciones:
        mbid = get_track_mbid_acous_brainz(cancion[0],cancion[2])
        if mbid:
            mbids_list.append(mbid)  
        else:
            print(f"No se encontró el MBID para '{cancion}'.")

    return mbids_list

def get_high_level_data(mbid):
    try:
        url = f"https://acousticbrainz.org/api/v1/{mbid}/high-level"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
    

def get_high_level_data_for_multiple_ids(mbid_list):
    results = []  
    
    for mbid in mbid_list:
        data = get_high_level_data(mbid) 

        if data is not None:
            results.append(data) 
        
        time.sleep(2) 
    
    return results 