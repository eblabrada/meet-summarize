from pydub import AudioSegment
import os

def cortar_audio_en_fragmentos(path_audio, duracion_segmento=30):
    """
    Corta un archivo de audio en fragmentos de duración fija (por defecto 30 segundos).

    Args:
        path_audio (str): Ruta al archivo de audio de entrada.
        duracion_segmento (int): Duración en segundos de cada fragmento (por defecto 30).

    Returns:
        List[str]: Lista de rutas a los archivos de audio generados.
    """

    # Cargar el audio desde el archivo
    audio = AudioSegment.from_file(path_audio)

    # Convertimos la duración del segmento a milisegundos (porque pydub trabaja en ms)
    duracion_ms = duracion_segmento * 1000
    duracion_total = len(audio)

    # Nombre base y extensión
    nombre_base = os.path.splitext(os.path.basename(path_audio))[0]
    print (nombre_base)
    extension = os.path.splitext(path_audio)[1].lower()
    carpeta_salida = os.path.join("data", f"{nombre_base}_fragmentos")

    # Crear carpeta de salida si no existe
    os.makedirs(carpeta_salida, exist_ok=True)

    # Lista para guardar los nombres de los fragmentos
    fragmentos = []

    # Cortar el audio en fragmentos
    for i in range(0, duracion_total, duracion_ms):
        fragmento = audio[i:i + duracion_ms]
        nombre_fragmento = os.path.join(carpeta_salida, f"{nombre_base}_parte{i // duracion_ms + 1}{extension}")
        fragmento.export(nombre_fragmento, format=extension[1:])  # quitar el punto de la extensión
        fragmentos.append(nombre_fragmento)
        print(f"Fragmento creado: {nombre_fragmento}")

    return fragmentos


print (cortar_audio_en_fragmentos("data/news_report.mp3"))