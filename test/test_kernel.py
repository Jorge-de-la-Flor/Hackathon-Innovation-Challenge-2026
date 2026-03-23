import asyncio
import json
from src.core.kernel_client import process_text

async def main():
    """
    Script de prueba para validar la integración con el Kernel de IA.
    Prueba los diferentes perfiles de accesibilidad cognitiva.
    """
    print("Iniciando prueba del motor de IA - Equipo 7")
    print("=" * 50)
    
    # Texto de prueba con alta carga cognitiva
    input_text = (
        "Se recomienda encarecidamente la desconexión del suministro eléctrico "
        "antes de proceder con la manipulación de los componentes internos del hardware."
    )
    
    profiles = ["adhd", "autism", "general"]
    
    for profile in profiles:
        print(f"\n--- Probando perfil: {profile.upper()} ---")
        try:
            # Llamada al cliente del kernel (real con fallback a mock)
            result = await process_text(input_text, profile)
            
            # Formateo de salida para mejor lectura
            print(json.dumps(result, indent=4, ensure_ascii=False))
            
        except Exception as e:
            # Captura errores específicos de la llamada sin detener el proceso
            print(f"Error procesando el perfil {profile}: {e}")

    print("\n" + "=" * 50)
    print("Pruebas finalizadas.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nPrueba cancelada por el usuario.")
    except Exception as e:
        print(f"\nError fatal en el runner de pruebas: {e}")
        