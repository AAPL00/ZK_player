import os

def read_folder(rute) :
    
    """extenciones de audio válidas para el programa"""
    valid_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
    """lista con todos los archivos de audio"""
    audio_files = []
    """itera sobre los archivos de la carpeta para quedarme solo con los válidos y los agrega a audio_files"""
    for file in os.listdir(rute) :
        complete_rute = os.path.join(rute, file)

        if os.path.isfile(complete_rute) and os.path.splitext(file)[1].lower() in valid_extensions:
            audio_files.append(complete_rute)

    return audio_files