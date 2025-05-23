from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def ask(self, prompt: str, context: str = "", history: list[str] = []) -> str:
        """
        Envía una petición al modelo de lenguaje.

        :param prompt: La pregunta o instrucción del usuario.
        :param context: Texto transcrito de la reunión (como contexto).
        :param history: Lista de preguntas anteriores (para mantener contexto conversacional).
        :return: Respuesta del modelo.
        """
        pass
