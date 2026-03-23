"""
Definición de rutas de la API.
Conecta los endpoints con la lógica de procesamiento del Kernel.
"""

from fastapi import APIRouter, HTTPException
from src.models.schemas import ProcessRequest, ProcessResponse
from src.core.kernel_client import process_text

router = APIRouter()

@router.post("/process", response_model=ProcessResponse, tags=["AI Processing"])
async def process(request: ProcessRequest):
    """
    Endpoint para procesar y adaptar texto según el perfil cognitivo.
    """
    try:
        # Llamada al motor de procesamiento (Kernel)
        result = await process_text(request.text, request.profile)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el procesamiento: {str(e)}")
