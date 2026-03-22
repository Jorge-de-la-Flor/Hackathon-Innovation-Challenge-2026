# 🚀 Project TODO: Accessibility Assistant API

## 🔴 PRIORIDAD ALTA (Bloqueantes / Core)

- [✅ ] **Configuración:** Eliminar definitivamente `python-dotenv` y usar `SettingsConfigDict` en `src/core/config.py`.
- [✅] **Validación:** Asegurar que las variables de Azure OpenAI sean obligatorias (sin strings vacíos `""`).
- [ ] **Kernel:** Implementar la lógica de conexión asíncrona en `src/core/kernel_client.py` con Azure SDK.
- [✅] **Schemas:** Definir los modelos de Pydantic para `ProcessRequest` y `ProcessResponse` en `src/models/schemas.py`.

## 🟡 PRIORIDAD MEDIA (Desarrollo / DevOps)

- [ ] **Infraestructura:** Configurar el despliegue inicial en AWS (Lambda o App Runner).
- [ ] **Seguridad:** Crear un archivo `.env.example` con las llaves de ejemplo para el repositorio.
- [ ] **Middleware:** Reemplazar el manejo de errores genérico `str(e)` por un sistema de Logging profesional.
- [ ] **CORS:** Restringir `allow_origins` de `["*"]` a los dominios específicos de producción.

## 🟢 PRIORIDAD BAJA (Mejoras / Futuro)

- [ ] **Pagos:** Investigar e implementar el flujo de suscripciones con Stripe (Webhooks).
- [ ] **Docs:** Personalizar la documentación de Swagger (`/docs`) con ejemplos de uso del Asistente.
- [ ] **Testing:** Crear una suite de pruebas unitarias con `pytest` para los endpoints principales.
- [ ] **License:** Revisar el tipo de licencia que vamos a utilizar en el proyecto del Hackathon.

## ✅ COMPLETADO

- [x] Estructura base del proyecto con FastAPI.
- [x] Endpoints de salud (`/health`) y procesamiento (`/process`) definidos.
- [x] Docstrings profesionales añadidos a los módulos principales.
- [x] Limpieza de redundancias en la carga de configuración.

---

_Última actualización: 22 de marzo de 2026_
