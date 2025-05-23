from .base_llm import BaseLLM

class TranscriptQA:
    def __init__(self, transcript_text: str, llm: BaseLLM):
        """
        Args:
            transcript_text (str): Texto completo de la transcripción del audio.
            llm (BaseLLM): Un cliente compatible con la interfaz BaseLLM.
        """
        self.transcript = transcript_text
        self.llm = llm

    def ask_question(self, question: str) -> str:
        """
        Pregunta sobre el contenido de la transcripción.
        """
        prompt = (
            f"Aquí tienes el texto de una reunión:\n\n"
            f"{self.transcript}\n\n"
            f"Pregunta: {question}\n"
            f"Respuesta:"
        )

        return self.llm.ask(prompt)