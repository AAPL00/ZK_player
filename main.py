import os
from mutagen import File

def read_folder(path) :
    valid_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
    songs = []
    for file in os.listdir(path) :
        complete_path = os.path.join(path, file)
        if os.path.isfile(complete_path) and os.path.splitext(file)[1].lower() in valid_extensions:
            title = File(complete_path).get("TIT2")
            if title :
                title = str(title)
            else :
                title = os.path.splitext(os.path.basename(file))[0]
        songs.append({"path" : complete_path, "title": title})
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