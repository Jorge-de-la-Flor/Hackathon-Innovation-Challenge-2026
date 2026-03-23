"""
Script de Pruebas de Integración - Equipo 7.
Valida que el motor de IA (Kernel) responda correctamente para todos los perfiles,
o que el sistema de robustez (Mock) se active en caso de fallo.
"""

import asyncio
import json
import logging
from src.core.kernel_client import process_text

# Desactivar logs innecesarios para una salida de prueba limpia
logging.getLogger("semantic_kernel").setLevel(logging.WARNING)

async def run_test_suite():
    """
    Ejecuta una serie de pruebas sobre el motor de procesamiento.
    """
    print("\n" + "="*60)
    print("🚀 ACCESAI - RUNNER DE PRUEBAS TÉCNICAS")
    print("="*60)
    
    test_case = (
        "Para proceder con el restablecimiento de la contraseña, el usuario debe "
        "acceder al portal de seguridad, validar su identidad mediante un código "
        "de un solo uso (OTP) y posteriormente definir una nueva cadena alfanumérica."
    )
    
    profiles = ["adhd", "autism", "general"]
    
    for profile in profiles:
        print(f"\n[TEST] Perfil: {profile.upper()}")
        print("-" * 30)
        
        try:
            # Ejecución del proceso (con lógica de robustez interna)
            result = await process_text(test_case, profile)
            
            # Validación de campos mínimos requeridos
            required_keys = ["simplified_text", "steps", "tone"]
            if all(key in result for key in required_keys):
                print("✅ Estructura JSON válida.")
                print(f"📄 Resumen: {result['simplified_text'][:80]}...")
                print(f"🎯 Tono: {result['tone']}")
                if "explanation" in result:
                    print(f"💡 Info: {result['explanation'][:50]}...")
            else:
                print("⚠️ Advertencia: Faltan campos en la respuesta JSON.")
                
        except Exception as e:
            print(f"❌ Fallo crítico en el test para {profile}: {e}")

    print("\n" + "="*60)
    print("✅ CICLO DE PRUEBAS COMPLETADO")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        asyncio.run(run_test_suite())
    except KeyboardInterrupt:
        print("\nTest interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError fatal en el runner de pruebas: {e}")
        