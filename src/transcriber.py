import os
import whisper

def transcribe(dir, model='base', save_text=False):
    files = sorted([
        f for f in os.listdir(dir)
        if f.lower().endswith(('.mp3', '.wav', '.m4a', '.flac', '.ogg'))
    ])

    print(f"Cargando modelo Whisper: {model}...")
    model = whisper.load_model(model)

    for i, name in enumerate(files):
        fpath = os.path.join(dir, name)
        print(f"[{i+1}/{len(files)}] Transcribiendo: {name}...")
        current = model.transcribe(fpath, fp16=False)
        text = current["text"]

        with open(f"{name.split('.')[0] + "_transcribe"}.txt", "w", encoding="utf-8") as f:
            f.write(text.strip())

# transcribe('data/')