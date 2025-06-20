from pydub import AudioSegment
import os

def cut_audio(audio_path, segment_len=30):
    # Cargar el audio desde el archivo
    audio = AudioSegment.from_file(audio_path)

    # Convertimos la duración del segmento a milisegundos (porque pydub trabaja en ms)
    len_ms = segment_len * 1000
    total = len(audio)

    name = os.path.splitext(os.path.basename(audio_path))[0]
    extension = os.path.splitext(audio_path)[1].lower()
    output = os.path.join("data")

    os.makedirs(output, exist_ok=True)

    fragmentos = []
    for i in range(0, total, len_ms):
        fragmento = audio[i:i + len_ms]
        nombre_fragmento = os.path.join(output, f"{name}_part{i // len_ms + 1}{extension}")
        fragmento.export(nombre_fragmento, format=extension[1:])  # quitar el punto de la extensión
        fragmentos.append(nombre_fragmento)
        print(f"Fragmento creado: {nombre_fragmento}")

    return fragmentos

# cut_audio('data/news_report.wav')