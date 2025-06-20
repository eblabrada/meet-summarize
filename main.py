from src.fireworks_models import FireworksModel
from src.meeting_processor import MeetingProcessor
from dotenv import load_dotenv
from src.transcriber import transcribe
from src.audio_cutter import cut_audio

import os

load_dotenv()
API_KEY = os.getenv('API_KEY', ' ')

llm = FireworksModel(model_name="accounts/fireworks/models/llama-v3p1-8b-instruct", api_key=API_KEY)
processor = MeetingProcessor(llm)

transcription = transcribe(".")

processor.set_transcript(transcription)

print("🔹 Resumen:")
print(processor.summarize_meeting())
print("\n🔹 Hablantes:")
print(processor.identify_speakers())
print("\n🔹 Planilla:")
print(processor.fill_form("Nombre del proyecto, Fecha, Participantes y Propuestas clave"))
print("\n🔹 Pregunta directa:")
print(processor.ask_question("¿Qué dijo Marta?"))
