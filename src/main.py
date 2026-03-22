"""
Punto de Entrada Principal de la API - Accessibility Assistant.

Este módulo inicializa la aplicación FastAPI, configura el middleware de CORS
para permitir la comunicación entre diferentes dominios y orquesta la 
inclusión de los routers de la API bajo el prefijo '/api/v1'.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router

# Inicialización de la aplicación con metadatos para la documentación automática (Swagger)
app = FastAPI(
    title="Accessibility Assistant API",
    version="1.0.0",
    description="API para el procesamiento de texto y asistencia en accesibilidad cognitiva."
)

# Configuración de CORS (Cross-Origin Resource Sharing)
# Esto permite que aplicaciones frontend (como React o Vue) se comuniquen con este backend.


# NOTA: Durante desarrollo se usa ["*"], pero en producción debe restringirse a dominios específicos.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusión de rutas modulares bajo el prefijo de versión v1
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)