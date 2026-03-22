"""
Módulo de Definición de Endpoints de la API.

Este módulo contiene las rutas de FastAPI para la interacción con el núcleo 
de procesamiento de texto. Define los puntos de entrada para la salud del 
servicio y el procesamiento principal de solicitudes.
"""

from fastapi import APIRouter, HTTPException
from src.models.schemas import ProcessRequest, ProcessResponse
from src.core.kernel_client import process_text

router = APIRouter()

@router.get("/health")
async def health():
    """
    Verifica el estado de salud de la API.

    Returns:
        dict: Un diccionario con el estado operativo del servicio.
    """
    return {"status": "ok"}


@router.post("/process", response_model=ProcessResponse)
async def process(request: ProcessRequest):
    """
    Procesa una solicitud de texto utilizando un perfil específico.

    Este endpoint recibe un texto y un perfil, delega el procesamiento al
    kernel_client y devuelve la respuesta estructurada.

    Args:
        request (ProcessRequest): El objeto de solicitud con el texto y el perfil.

    Returns:
        ProcessResponse: El resultado procesado y estructurado.

    Raises:
        HTTPException: Error 500 si ocurre una falla en la lógica de procesamiento.
    """
    try:
        # Procesamiento asíncrono del texto
        result = await process_text(request.text, request.profile)
        return ProcessResponse(**result)
    except Exception as e:
        # Captura de errores inesperados para evitar caídas del servicio
        raise HTTPException(status_code=500, detail=str(e))
