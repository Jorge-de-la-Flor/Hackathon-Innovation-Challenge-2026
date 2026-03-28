# AccesAI - Makefile de Automatización (Equipo 7)
.PHONY: setup test api ui help start sync

# Colores
BLUE=\033[0;34m
NC=\033[m

# Rutas espejo (Ajusta 'jafde' si cambia tu usuario)
WSL_PATH = ./AccesAI_extension/
WIN_PATH = /mnt/c/Users/jafde/Documents/AccesAI_extension/

help:
	@echo "$(BLUE)Comandos disponibles:$(NC)"
	@echo "  make setup   - Instala dependencias (Python y Node)"
	@echo "  make api     - Lanza el backend Python (Puerto 3000)"
	@echo "  make ui      - Lanza el servidor Angular (Puerto 4200)"
	@echo "  make sync    - Sincroniza la extensión con Windows"
	@echo "  make start   - LANZA TODO (API + UI)"

# USAMOS '&' para que se ejecuten en paralelo y no se bloqueen
start: setup
	@echo "$(BLUE)Levantando el ecosistema completo...$(NC)"
	$(MAKE) api & $(MAKE) ui

setup:
	@echo "$(BLUE)Sincronizando entorno Python...$(NC)"
	uv sync
	@echo "$(BLUE)Instalando dependencias de Node...$(NC)"
	cd web_ui && npm install

api:
	@echo "$(BLUE)Iniciando API en puerto 3000...$(NC)"
	PYTHONPATH=. uv run python src/main.py

ui:
	@echo "$(BLUE)Iniciando Angular Dev Server...$(NC)"
	cd web_ui && npm start

sync:
	@echo "$(BLUE)Sincronizando extensión hacia Windows...$(NC)"
	rsync -avz --delete $(WSL_PATH) $(WIN_PATH)
	@echo "$(BLUE)✅ Espejo completado. Refresca en chrome://extensions$(NC)"

test:
	python -m test.test_kernel
