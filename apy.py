import streamlit as st
import os
from openai import OpenAI

# Charger la clé API depuis les secrets
api_key = os.getenv("GEMINI_API_KEY")  # <-- nom du secret

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
st.title("🎬 Mini-App VO3 avec Opal IA")
st.write("Génère tes vidéos VO3 sans limite 🚀")

# Zone de texte pour ton prompt
prompt = st.text_area("👉 Entre ton idée de vidéo :", "Un tutoriel VO3 de plomberie avec humour...")

# Bouton pour générer
if st.button("Générer la vidéo"):
    if not prompt.strip():
        st.warning("⚠️ Mets un texte avant de générer !")
    else:
        with st.spinner("Génération en cours..."):
            response = client.chat.completions.create(
                model="gemini-1.5-flash",
                messages=[{"role": "user", "content": prompt}]
            )
            texte_genere = response.choices[0].message.content
            st.success("✅ Vidéo générée avec succès !")
            st.write("**Script généré :**")
            st.write(texte_genere)
