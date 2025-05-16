import whisper

model = whisper.load_model("base")

audio = whisper.load_audio("news_report.mp3")
audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

result = model.transcribe(
  audio,
  language="en",
  temperature=0.4,
  verbose=True,
  fp16=False
)