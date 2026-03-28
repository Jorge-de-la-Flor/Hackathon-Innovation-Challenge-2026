"""
Punto de Entrada Principal de la API - Accessibility Assistant.
Inicializa FastAPI y orquesta los routers y middlewares.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router
# IMPORTANTE: Importamos el traductor que creaste arriba
from src.api.compatibility import router as compatibility_router
import uvicorn

app = FastAPI(
    title="AccesAI - Motor de Inclusión Cognitiva",
    description="Arquitectura de Resiliencia para TDAH y Autismo",
    version="1.0.0"
)

# CORS TOTAL: Para que el Angular conecte sin errores
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Registro de tus rutas originales (v1)
app.include_router(router, prefix="/api/v1")

# 2. Registro del puente de compatibilidad (Intercepta /api/breakdown)
app.include_router(compatibility_router)

@app.get("/")
async def health():
    return {
        "status": "ready",
        "mode": "hybrid_ai_resilient",
        "message": "Sistema de Accesibilidad Cognitiva Activo",
        "bridge": "Lidia's Frontend Compatible"
    }

if __name__ == "__main__":
    # Puerto 3000: Es el que busca el frontend por defecto
    uvicorn.run(app, host="0.0.0.0", port=3000)
    