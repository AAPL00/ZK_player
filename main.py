import os
from mutagen import File

"""Obtener todos los archivos de audio de un directorio"""
def read_folder(path) :
    
    """extenciones de audio válidas para el programa"""
    valid_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
    
    """lista con todos los archivos de audio"""
    songs = []
    
    """itera sobre los archivos de la carpeta"""
    for file in os.listdir(path) :
        
        """crea una cadena con la ruta completa del archivo"""
        complete_path = os.path.join(path, file)
        
        """si el archivo es un objeto de tipo file y posee una extención válida"""
        if os.path.isfile(complete_path) and os.path.splitext(file)[1].lower() in valid_extensions:
            
            """obtiene el título de la canción, si existe lo convierte a string sino toma el nombre del archivo"""
            title = File(complete_path).get("TIT2")
            if title :
                title = str(title)
            else :
                title = os.path.splitext(os.path.basename(file))[0]
        
        """agrega cada canción a la lista con formato de diccionario de dos llaves path y title"""
        songs.append({"path" : complete_path, "title": title})

    return songs

"""agrupar las canciones de acuerdo a una función dada"""
def group_by(songs_list, method) :
    
    """lo agruparemos con un diccionario"""
    group = {}
    
    """recorre la lista de canciones"""
    for song in songs_list :
        
        """obtiene el valor de la canción de acuerdo a la clasificación dada"""
        key = method(song)
        
        """si el valor de la canción de acuerdo a la clasificación no se encontraba en el diccionario crea una nueva lista para esa llave"""
        if key not in group :
            group[key] = []

        """agrega el título de la canción a la lista de la llave correspondiente"""    
        group[key].append(song["title"])
    
    return group

"""obtener artista de la canción"""
def get_artist(song) :
    audio = File(song["path"])
    return str(audio.get("TPE1", "Desconocido"))

"""obtener álbum de la canción"""
def get_album(song) :
    audio = File(song["path"])
    return str(audio.get("TALB", "Sin Álbum"))