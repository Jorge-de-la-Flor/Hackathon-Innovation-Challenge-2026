"""
Módulo de Configuración Centralizada.

Este módulo gestiona las variables de entorno de la aplicación utilizando 
Pydantic Settings. Carga automáticamente el archivo .env y valida que las 
credenciales necesarias para Azure OpenAI estén presentes antes de iniciar.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configuración global de la aplicación.
    
    Los atributos definidos aquí deben coincidir con las llaves en el archivo .env.
    Al no asignar un valor por defecto (como ""), Pydantic marcará estas 
    variables como requeridas.

    Attributes:
        azure_openai_endpoint (str): URL del endpoint de Azure OpenAI.
        azure_openai_api_key (str): Clave de API para autenticación.
        azure_openai_deployment (str): Nombre del modelo desplegado.
    """
    
    # Configuración de Azure OpenAI
    azure_openai_endpoint: str
    azure_openai_api_key: str
    azure_openai_deployment: str

    # Configuración de Pydantic V2 para la carga del entorno
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# Instancia de configuración lista para ser importada en el resto del proyecto
settings = Settings()
