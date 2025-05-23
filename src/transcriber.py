import os
import whisper

def transcribir_directorio_a_texto(directorio, modelo='base', save_text=False):
    """
    Transcribe todos los archivos de audio en un directorio usando Whisper.

    Args:
        directorio (str): Ruta al directorio que contiene los archivos de audio.
        modelo (str): Modelo de Whisper a usar. Puede ser: 'tiny', 'base', 'small', 'medium', 'large'.

    Returns:
        str: Texto resultante de concatenar todas las transcripciones.
    """

    archivos = sorted([
        f for f in os.listdir(directorio)
        if f.lower().endswith(('.mp3', '.wav', '.m4a', '.flac', '.ogg'))
    ])

    print(f"Cargando modelo Whisper: {modelo}...")
    model = whisper.load_model(modelo)

    texto_completo = ""

    for i, nombre_archivo in enumerate(archivos):
        path_completo = os.path.join(directorio, nombre_archivo)
        print(f"[{i+1}/{len(archivos)}] Transcribiendo: {nombre_archivo}...")
        resultado = model.transcribe(path_completo)
        texto = resultado["text"]
        texto_completo += f"\n--- Transcripción de {nombre_archivo} ---\n"
        texto_completo += texto.strip() + "\n"

    with open("transcripcion_completa.txt", "w", encoding="utf-8") as f:
        f.write(texto_completo)

    return texto_completo

texto = transcribir_directorio_a_texto("data/news_report_fragmentos", modelo="base")
