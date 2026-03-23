"""
Interfaz de Usuario - AccesAI.
Construida con Streamlit para ofrecer una experiencia accesible y fluida.
Comunica el frontend con el backend de FastAPI.
"""

import streamlit as st
import requests
import json

# Configuración de la página
st.set_page_config(
    page_title="AccesAI",
    page_icon="♿",
    layout="wide"
)

# Estilos personalizados para mejorar la legibilidad
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Título y descripción
st.title("🧠 AccesAI")
st.markdown("### Haz que cualquier texto sea más accesible para tu perfil cognitivo.")

# Sidebar para configuración de perfil
with st.sidebar:
    st.header("⚙️ Configuración")
    profile = st.selectbox(
        "Selecciona tu perfil de accesibilidad:",
        ["general", "adhd", "autism"],
        index=0
    )
    
    profile_info = {
        "general": ("Estándar", "Sin adaptaciones específicas."),
        "adhd": ("TDAH", "Texto simplificado, pasos cortos y énfasis en lo importante."),
        "autism": ("TEA", "Lenguaje literal, estructurado y libre de ambigüedades.")
    }
    
    name, desc = profile_info[profile]
    st.info(f"**Perfil {name}**: {desc}")
    st.divider()
    st.caption("Equipo 7 - Hackathon 2026")

# Layout de dos columnas para entrada y salida
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Texto Original")
    input_text = st.text_area(
        "Pega aquí el contenido que deseas adaptar:",
        height=350,
        placeholder="Ejemplo: Se recomienda encarecidamente la desconexión del suministro eléctrico..."
    )
    process_button = st.button("Adaptar Contenido", type="primary")

with col2:
    st.subheader("✨ Contenido Adaptado")
    if process_button:
        if not input_text.strip():
            st.warning("⚠️ Por favor, ingresa un texto para procesar.")
        else:
            with st.spinner("La IA está trabajando en la accesibilidad..."):
                try:
                    # Llamada al backend de FastAPI (Ruta corregida con v1)
                    response = requests.post(
                        "http://localhost:8000/api/v1/process",
                        json={"text": input_text, "profile": profile},
                        timeout=45
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        st.success("¡Procesamiento completado con éxito!")
                        
                        # Mostrar el texto simplificado
                        st.markdown("**Versión Simplificada:**")
                        st.write(data["simplified_text"])
                        
                        # Mostrar pasos si existen
                        if data.get("steps"):
                            st.markdown("---")
                            st.markdown("**📋 Pasos a seguir:**")
                            for i, step in enumerate(data["steps"], 1):
                                st.write(f"{i}. {step}")
                        
                        # Información del tono
                        st.markdown("---")
                        st.markdown(f"**🎯 Tono detectado:** `{data['tone']}`")
                        
                        # Explicación técnica oculta
                        with st.expander("🔍 Ver detalles técnicos de la adaptación"):
                            st.write(data.get("explanation", "Sin detalles adicionales."))
                    
                    else:
                        st.error(f"Error del servidor ({response.status_code}): {response.text}")
                
                except requests.exceptions.ConnectionError:
                    st.error("No se pudo conectar con el servidor. Asegúrate de que FastAPI esté corriendo en el puerto 8000.")
                except Exception as e:
                    st.error(f"Ocurrió un error inesperado: {str(e)}")
    else:
        st.info("Ingresa un texto a la izquierda y presiona 'Adaptar Contenido' para ver el resultado.")

# Footer
st.divider()
st.markdown("<center>AccesAI | Desarrollado para el Hackathon Innovation Challenge 2026</center>", unsafe_allow_html=True)
