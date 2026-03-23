import streamlit as st
import requests
import json

# Configuración de la página
st.set_page_config(
    page_title="AccesAI",
    page_icon="♿",
    layout="wide"
)

# Título
st.title("♿ AccesAI")
st.markdown("Haz que cualquier texto sea más accesible para tu perfil cognitivo.")

# Sidebar para perfil
with st.sidebar:
    st.header("Configuración")
    profile = st.selectbox(
        "Selecciona tu perfil de accesibilidad:",
        ["general", "adhd", "autism"]
    )
    profile_desc = {
        "general": "Sin adaptaciones específicas.",
        "adhd": "Texto simplificado, pasos cortos y tono calmado.",
        "autism": "Lenguaje estructurado, sin ambigüedades."
    }
    st.caption(profile_desc[profile])

# Área principal
col1, col2 = st.columns(2)

with col1:
    st.subheader("Texto original")
    input_text = st.text_area(
        "Pega o escribe el texto que quieres adaptar:",
        height=300,
        placeholder="Ejemplo: La Declaración Universal de los Derechos Humanos establece que todos los seres humanos nacen libres e iguales en dignidad y derechos..."
    )
    process_button = st.button("Procesar", type="primary")

with col2:
    st.subheader("Texto adaptado")
    if process_button and input_text:
        with st.spinner("Procesando con IA..."):
            try:
                response = requests.post(
                    "http://localhost:8000/process",  # Ajustar si el backend corre en otro puerto/host
                    json={"text": input_text, "profile": profile},
                    timeout=30
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("¡Texto adaptado!")
                    st.markdown("**📝 Versión simplificada:**")
                    st.write(data["simplified_text"])
                    if data["steps"]:
                        st.markdown("**📋 Pasos recomendados:**")
                        for step in data["steps"]:
                            st.write(f"- {step}")
                    st.markdown("**🎯 Tono aplicado:**")
                    st.info(data["tone"])
                    with st.expander("Ver explicación de la adaptación"):
                        st.write(data["explanation"])
                else:
                    st.error(f"Error en el servidor: {response.status_code}")
            except Exception as e:
                st.error(f"Error de conexión: {e}")
    elif process_button and not input_text:
        st.warning("Por favor, escribe o pega algún texto.")

# Footer
st.divider()
st.caption("AccesAI - Hackathon Innovation Challenge 2026")
