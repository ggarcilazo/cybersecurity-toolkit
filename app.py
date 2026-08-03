import streamlit as st
from src.crypto_utils import check_password_strength, encrypt_message

st.set_page_config(page_title="CyberSec Toolkit", page_icon="🛡️", layout="wide")
st.title("🛡️ Cybersecurity Toolkit Profesional")

menu = st.sidebar.selectbox("Selecciona una herramienta", ["Auditor de Contraseñas", "Cifrado AES"])

if menu == "Auditor de Contraseñas":
    st.header("🔑 Auditor de Fortaleza de Contraseñas")
    pwd = st.text_input("Introduce la contraseña a evaluar:", type="password")
    if pwd:
        score, feedback = check_password_strength(pwd)
        if score == 4: st.success("🔒 ¡Contraseña altamente segura!")
        elif score >= 2: st.warning("⚠️ Contraseña aceptable pero mejorable.")
        else: st.error("❌ Contraseña muy vulnerable.")
        for item in feedback: st.write(f"- {item}")

elif menu == "Cifrado AES":
    st.header("🔐 Cifrado de Mensajes Simétrico")
    msg = st.text_area("Texto a cifrar:")
    if st.button("Generar Cifrado"):
        if msg:
            encrypted, key = encrypt_message(msg)
            st.code(f"Mensaje Cifrado:\n{encrypted}", language="text")
            st.code(f"Clave secreta (¡Guárdala bien!):\n{key}", language="text")
        else: st.warning("Escribe un mensaje primero.")

