import os
from typing import List
from openai import OpenAI
from .base_llm import BaseLLM

class FireworksModel(BaseLLM):
    def __init__(self, model_name: str, api_key: str = None):
        """
        :param model_name: Nombre del modelo en Fireworks (ej: 'accounts/fireworks/models/firefunction-v1')
        :param api_key: Clave API de Fireworks.ai
        """
        self.api_key = api_key or os.getenv("FIREWORKS_API_KEY")
        if not self.api_key:
            raise ValueError("FIREWORKS_API_KEY no está definida")
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.fireworks.ai/inference/v1"
        )
        self.model = model_name

    def ask(self, prompt: str, context: str = "", history: List[str] = []) -> str:
        """
        Llama al modelo de Fireworks con un contexto de reunión y el historial conversacional.
        """
        messages = []

        # Si hay contexto previo de la reunión, lo añadimos como sistema
        if context:
            messages.append({"role": "system", "content": f"Este es el texto de una reunión: {context}"})

        # Agregar historial previo de preguntas/respuestas si existe
        for past in history:
            messages.append({"role": "user", "content": past})

        # Mensaje actual
        messages.append({"role": "user", "content": prompt})

        # Llamada al modelo
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()
