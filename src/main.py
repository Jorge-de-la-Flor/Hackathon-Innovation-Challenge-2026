"""
Punto de Entrada Principal de la API - Accessibility Assistant.
Inicializa FastAPI y orquesta los routers y middlewares.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router
import uvicorn

app = FastAPI(
    title="AccesAI - Motor de Inclusión Cognitiva",
    description="Arquitectura de Resiliencia para TDAH y Autismo",
    version="1.0.0"
)

# CORS TOTAL: Para que cualquier frontend conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de rutas
app.include_router(router, prefix="/api/v1")

@app.get("/")
async def health():
    return {
        "status": "ready",
        "mode": "hybrid_ai_resilient",
        "message": "Sistema de Accesibilidad Cognitiva Activo"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)