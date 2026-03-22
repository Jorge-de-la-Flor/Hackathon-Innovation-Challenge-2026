"""
Esquemas Pydantic para las solicitudes y respuestas de la API.

Este módulo define los modelos de datos que usa el servicio para recibir
peticiones de procesamiento de texto y devolver resultados simplificados
y adaptados al perfil del usuario.
"""

from pydantic import BaseModel
from typing import List, Optional


class ProcessRequest(BaseModel):
    """
    Esquema de entrada para la API de procesamiento de texto.

    Atributos:
        text: Texto original que se quiere simplificar o adaptar.
        profile: Perfil del usuario objetivo (por ejemplo: "adhd", "autism", "general").
    """

    text: str
    profile: str  # Los perfiles pueden ser: "adhd", "autism", "general", etc.


class ProcessResponse(BaseModel):
    """
    Esquema de salida para la API de procesamiento de texto.

    Atributos:
        simplified_text: Versión simplificada o adaptada del texto original.
        steps: Lista de pasos o puntos clave extraídos del texto.
        tone: Tono utilizado en la respuesta (por ejemplo: "neutral", "friendly").
        explanation: Explicación opcional de cómo o por qué se transformó el texto.
    """

    simplified_text: str
    steps: List[str]
    tone: str
    explanation: Optional[str] = None
