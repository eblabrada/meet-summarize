from typing import List, Optional
from .base_llm import BaseLLM

class MeetingProcessor:
    def __init__(self, llm: BaseLLM):
        """
        :param llm: Una instancia de un modelo de lenguaje que herede de BaseLLM
        """
        self.llm = llm
        self.transcript: Optional[str] = None
        self.history: List[str] = []

    def set_transcript(self, text: str):
        """
        Establece el texto transcrito de la reunión.
        """
        self.transcript = text

    def summarize_meeting(self) -> str:
        """
        Resume la reunión usando el modelo de lenguaje.
        """
        if not self.transcript:
            raise ValueError("No hay transcripción cargada")

        prompt = "Resume brevemente los puntos principales discutidos en la reunión."
        summary = self.llm.ask(prompt=prompt, context=self.transcript, history=self.history)
        self.history.append(prompt)
        return summary

    def identify_speakers(self) -> str:
        """
        Intenta identificar quién habló y qué dijo.
        """
        if not self.transcript:
            raise ValueError("No hay transcripción cargada")

        prompt = "Identifica a los hablantes en la reunión y resume qué dijo cada uno."
        result = self.llm.ask(prompt=prompt, context=self.transcript, history=self.history)
        self.history.append(prompt)
        return result

    def fill_form(self, form_description: str) -> str:
        """
        Rellena una planilla virtual en base a una descripción (por ejemplo, 'nombre del proyecto, fecha, responsables').
        """
        if not self.transcript:
            raise ValueError("No hay transcripción cargada")

        prompt = f"Rellena la siguiente planilla con los datos de la reunión: {form_description}"
        result = self.llm.ask(prompt=prompt, context=self.transcript, history=self.history)
        self.history.append(prompt)
        return result

    def ask_question(self, question: str) -> str:
        """
        Permite hacer preguntas sobre la reunión.
        """
        if not self.transcript:
            raise ValueError("No hay transcripción cargada")

        answer = self.llm.ask(prompt=question, context=self.transcript, history=self.history)
        self.history.append(question)
        return answer

    def reset_history(self):
        """
        Limpia el historial de conversación.
        """
        self.history = []
