import os
from mutagen import File

def read_folder(path) :
    
    """extenciones de audio válidas para el programa"""
    valid_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
    """lista con todos los archivos de audio"""
    audio_files = []
    """itera sobre los archivos de la carpeta para quedarme solo con los válidos y los agrega a audio_files"""
    for file in os.listdir(path) :
        complete_path = os.path.join(path, file)

        if os.path.isfile(complete_path) and os.path.splitext(file)[1].lower() in valid_extensions:
            audio_files.append(complete_path)

    songs = []

    for file in audio_files :
        audio = File(file)
        """el get depende del formato de archivo, pues el campo con el título de la canción cambia en dependencia del formato"""
        title = audio.get("TIT2")
        if title :
            title = str(title)
        else :
            titulo = os.path.splitext(os.path.basename(file))[0]
        
        songs.append({"path" : file, "title": title})

    return songs

def group_by(songs_list, method) :
    group = {}
    for song in songs_list :
        key = method(song)
        if key not in group :
            group[key] = []
        group[key].append(song["title"])
    return group

def get_artist(song) :
    audio = File(song["path"])
    return str(audio.get("TPE1", "Desconocido"))

def get_album(song) :
    audio = File(song["path"])
    return str(audio.get("TALB", "Sin Álbum"))


hola = read_folder("/home/zaki/Music")
print(group_by(hola, get_album))