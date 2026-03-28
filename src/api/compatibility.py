from fastapi import APIRouter, Body
from src.core.kernel_client import process_text 
from typing import Any, Dict

router = APIRouter()

@router.post("/api/breakdown")
async def breakdown_compatibility(
    payload: Dict[str, Any] = Body(...)
):
    """
    Interceptor para el Frontend de Angular.
    Mapea 'task' -> 'text' y devuelve el formato que la UI de Lidia espera.
    """
    # Extraemos lo que envía el Angular de Lidia
    task_content = payload.get("task", "")
    profile = payload.get("profile", "adhd")
    
    print(f"--- [BRIDGE] Interceptando para UI: {task_content[:30]}... ---")

    # Llamada a tu lógica de Semantic Kernel
    result = await process_text(task_content, profile)
    
    # Formateamos para su interfaz (pasos con tiempo y tipo)
    formatted_steps = []
    steps_data = result.get("steps", [])
    
    for step in steps_data:
        # En tu loop de formatted_steps:
        formatted_steps.append({
            "description": step, # Cambia 'text' por 'description' si Lidia lo llamó así
            "estimatedTime": "5 min", # Ajusta los nombres de las llaves
            "type": "action"
        })
        
    return {
        "difficulty": "Adaptada",
        "totalTime": f"{len(formatted_steps) * 5} min",
        "steps": formatted_steps,
        "explanation": result.get("explanation", "Generado por AccesAI Core.")
    }
    