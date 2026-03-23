import asyncio
from src.core.kernel_client import process_text

async def main():
    print("🚀 Iniciando prueba del motor de IA del Equipo 7...")
    
    # Texto de prueba difícil
    input_text = "Se recomienda encarecidamente la desconexión del suministro eléctrico antes de proceder con la manipulación de los componentes internos del hardware."
    
    # Probamos con perfil TDAH
    print("\n--- Probando perfil: ADHD ---")
    res_adhd = await process_text(input_text, "adhd")
    print(res_adhd)
    
    # Probamos con perfil Autismo
    print("\n--- Probando perfil: AUTISM ---")
    res_autism = await process_text(input_text, "autism")
    print(res_autism)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ Error en la prueba: {e}")