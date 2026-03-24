# AccesAI - Makefile de Automatización (Equipo 7)
# Facilita la instalación, pruebas y ejecución del proyecto.

.PHONY: setup test api ui help

# Colores para la terminal
BLUE=\033[0;34m
NC=\033[m

help:
	@echo "$(BLUE)Comandos disponibles:$(NC)"
	@echo "  make setup   - Instala dependencias y prepara el entorno con uv"
	@echo "  make test    - Ejecuta las pruebas de integración del Kernel"
	@echo "  make api     - Lanza el backend de FastAPI (Puerto 8000)"
	@echo "  make ui      - Lanza la interfaz de Streamlit (Puerto 8501)"
	@echo "  make all     - Ejecuta la instalación y luego las pruebas"

setup:
	@echo "$(BLUE)Sincronizando entorno con uv...$(NC)"
	uv sync

test:
	@echo "$(BLUE)Ejecutando suite de pruebas técnicas...$(NC)"
	python -m test.test_kernel

api:
	@echo "$(BLUE)Iniciando API de AccesAI...$(NC)"
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

ui:
	@echo "$(BLUE)Iniciando Interfaz de Usuario...$(NC)"
	streamlit run src/ui/app.py

all: setup test
