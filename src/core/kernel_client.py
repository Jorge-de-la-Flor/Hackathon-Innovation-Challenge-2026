"""
Módulo del Cliente del Kernel de Procesamiento.
Implementa una arquitectura de robustez con fallback automático a Mock
en caso de fallos en el servicio de IA (Azure OpenAI / Semantic Kernel).
"""

import asyncio
import json
import logging
from typing import Dict
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from src.core.config import settings

# Configuración de logger para auditoría de errores
logger = logging.getLogger(__name__)

async def process_text(text: str, profile: str) -> Dict:
    """
    Procesa un texto adaptándolo al perfil de accesibilidad.
    Intenta usar la IA real y cae a un Mock determinista si hay errores.
    """
    try:
        # --- 1. INTENTO DE PROCESAMIENTO REAL (KERNEL DE IA) ---
        kernel = Kernel()

        # Configuración del servicio de Azure OpenAI usando los settings del proyecto
        kernel.add_service(
            AzureChatCompletion(
                deployment_name=settings.azure_openai_deployment,
                endpoint=settings.azure_openai_endpoint,
                api_key=settings.azure_openai_api_key,
                api_version="2024-06-01" 
            )
        )

        prompt_template = """
        Eres un experto en accesibilidad cognitiva. 
        Adapta el siguiente texto para un perfil de: {{ $profile }}.
        
        REGLAS:
        - adhd: Frases cortas, negritas en palabras clave, máximo 3 pasos.
        - autism: Lenguaje literal, sin metáforas, estructura clara.
        - general: Palabras sencillas y tono amable.

        Responde ÚNICAMENTE en formato JSON:
        {
            "simplified_text": "texto adaptado",
            "steps": ["paso 1", "paso 2"],
            "tone": "descripción del tono",
            "explanation": "por qué se adaptó así"
        }

        Texto a adaptar: {{ $input }}
        """

        func = kernel.add_function(
            function_name="adapt_text",
            plugin_name="AccessibilityPlugin",
            prompt=prompt_template
        )

        # Invocación al modelo de lenguaje
        result = await kernel.invoke(func, input=text, profile=profile)
        
        # Limpieza de Markdown (posibles bloques ```json ... ```)
        raw_result = str(result).strip()
        if raw_result.startswith("```json"):
            raw_result = raw_result.replace("```json", "").replace("```", "").strip()
        
        return json.loads(raw_result)

    except Exception as e:
        # --- 2. LÓGICA DE ROBUSTEZ (FALLBACK A MOCK) ---
        # Si Lidya no configuró bien las keys o el servicio cae, el sistema NO se detiene.
        logger.error(f"⚠️ Error crítico en IA: {e}. Activando motor de respaldo.")
        
        # Pequeña latencia para simular procesamiento
        await asyncio.sleep(0.2)
        
        # Respuestas deterministas para asegurar que el Frontend no se rompa
        mock_responses = {
            "adhd": {
                "simplified_text": f"[ADHD Mode] {text[:120]}...",
                "steps": [
                    "1. Identifica el punto central",
                    "2. Elimina las distracciones externas",
                    "3. Ejecuta la acción inmediata"
                ],
                "tone": "Directo y segmentado para reducir carga ejecutiva.",
                "explanation": "Activado modo de respaldo por latencia en el servicio de IA."
            },
            "autism": {
                "simplified_text": f"[Autism Mode] {text[:120]}...",
                "steps": [
                    "1. Punto de partida A",
                    "2. Punto de control B",
                    "3. Resultado final C"
                ],
                "tone": "Literal, estructurado y libre de ambigüedades.",
                "explanation": "Activado modo de respaldo por error en la conexión con el motor de IA."
            }
        }
        
        # Retornamos el mock correspondiente o el texto original si es perfil general
        return mock_responses.get(profile, {
            "simplified_text": text,
            "steps": [],
            "tone": "Estándar / General",
            "explanation": "Procesamiento básico sin adaptaciones específicas por error de servicio."
        })

# TODO: Considerar el uso de caché (Redis) para perfiles y textos repetidos.
