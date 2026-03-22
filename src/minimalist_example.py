from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

class ProcessRequest(BaseModel):
    text: str
    profile: str

class ProcessResponse(BaseModel):
    simplified_text: str
    steps: List[str]
    tone: str
    explanation: Optional[str] = None

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/process", response_model=ProcessResponse)
async def process(request: ProcessRequest):
    # Acá va tu lógica (mock por ahora)
    return ProcessResponse(
        simplified_text=f"[{request.profile}] {request.text[:100]}...",
        steps=["1. Leer", "2. Resumir"],
        tone="Calmado",
        explanation="Ejemplo mock"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    