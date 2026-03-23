"""
Punto de Entrada Principal de la API - Accessibility Assistant.
Inicializa FastAPI y orquesta los routers y middlewares.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router

app = FastAPI(
    title="Accessibility Assistant API",
    version="1.0.0",
    description="API para el procesamiento de texto y asistencia en accesibilidad cognitiva."
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusión de rutas modulares
app.include_router(router, prefix="/api/v1")

@app.get("/health", tags=["System"])
async def health():
    """Verifica el estado de salud de la API."""
    return {"status": "ok", "service": "accessibility-assistant"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
    