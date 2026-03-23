import json
import logging
from typing import Dict
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from src.core.config import settings

logger = logging.getLogger(__name__)

async def process_text(text: str, profile: str) -> Dict:
    """
    Motor de IA de Lidya: Conexión real con Azure OpenAI.
    """
    try:
        kernel = Kernel()

        # Usamos los nombres exactos de tu config.py (en minúsculas)
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

        result = await kernel.invoke(func, input=text, profile=profile)

        # Limpieza del resultado por si el modelo envía etiquetas de markdown
        raw_result = str(result).strip()
        if raw_result.startswith("```json"):
            raw_result = raw_result.replace("```json", "").replace("```", "").strip()
        
        return json.loads(raw_result)

    except Exception as e:
        logger.error(f"Error en el Kernel de Lidya: {e}")
        return {
            "simplified_text": "Hubo un error al procesar el texto.",
            "steps": [],
            "tone": "Error",
            "explanation": str(e)
        }