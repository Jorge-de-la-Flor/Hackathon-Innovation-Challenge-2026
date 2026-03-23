"""
Modelos de datos para la API utilizando Pydantic.
"""

from pydantic import BaseModel, Field
from typing import List, Optional

class ProcessRequest(BaseModel):
    text: str = Field(..., description="Texto original a simplificar")
    profile: str = Field(..., description="Perfil de destino: adhd, autism, o general")

class ProcessResponse(BaseModel):
    simplified_text: str
    steps: List[str]
    tone: str
    explanation: Optional[str] = None
    