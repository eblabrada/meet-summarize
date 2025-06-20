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

    result = []
    for i in range(0, total, len_ms):
        fragment = audio[i:i + len_ms]
        fragment_name = os.path.join(output, f"{name}_part{i // len_ms + 1}{extension}")
        fragment.export(fragment_name, format=extension[1:])  # quitar el punto de la extensión
        result.append(fragment_name)
        print(f"Fragmento creado: {fragment_name}")

    return result

# cut_audio('data/news_report.wav')