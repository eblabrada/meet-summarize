import os
import whisper
from pydub import AudioSegment
from pydub.utils import make_chunks

class Transcriber:
  def __init__(self, model = 'base'):
    self.model = whisper.load_model(model)

  def transcribe_block(self, block, block_id: int) -> str:
    block_filename = f"_temp_{block_id}.wav"
    block.export(block_filename, format="wav")

    audio = whisper.load_audio(block_filename)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio, n_mels=self.model.dims.n_mels).to(self.model.device)

    # _, probs = self.model.detect_language(mel)
    # # print(f"Detected language: {max(probs, key=probs.get)}")

    options = whisper.DecodingOptions(language='en', temperature=0.4, fp16=False)
    result = whisper.decode(self.model, mel, options)

    os.remove(block_filename)
    return result.text + "\n"

  def transcribe(self, audio_path: str, block_length: int = 20000) -> str:
    audio = AudioSegment.from_mp3(audio_path)
    blocks = make_chunks(audio, block_length)

    result = ''
    for id, block in enumerate(blocks):
      current_transcript = self.transcribe_block(block, id)
      result += current_transcript

    return result.strip()
  
# transcriber = Transcriber()

# print(transcriber.transcribe('news_report.mp3'))