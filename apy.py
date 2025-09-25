import streamlit as st
import os
from openai import OpenAI

# Récupérer la clé API depuis les secrets Streamlit
api_key = os.getenv("GEMINI_API_KEY")

# Vérification rapide de la clé API
if not api_key:
    st.error("❌ Clé API non trouvée. Assure-toi que GEMINI_API_KEY est configuré dans Secrets.")
    st.stop()  # arrête l'exécution si la clé est absente

# Initialiser le client OpenAI
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Interface Streamlit
st.title("🎬 Mini-App VO3 avec Opal IA")
st.write("Génère tes vidéos VO3 sans limite 🚀")

# Zone de texte pour le prompt
prompt = st.text_area("👉 Entre ton idée de vidéo :", "Un tutoriel VO3 de plomberie avec humour...")

# Bouton pour générer la vidéo
if st.button("Générer la vidéo"):
    if not prompt.strip():
        st.warning("⚠️ Mets un texte avant de générer !")
    else:
        with st.spinner("Génération en cours..."):
            try:
                response = client.chat.completions.create(
                    model="gemini-1.5-flash",
                    messages=[{"role": "user", "content": prompt}]
                )
                texte_genere = response.choices[0].message.content
                if texte_genere:
                    st.success("✅ Vidéo générée avec succès !")
                    st.write("**Script généré :**")
                    st.write(texte_genere)
                else:
                    st.warning("⚠️ Aucun texte généré !")
            except Exception as e:
                st.error(f"❌ Erreur OpenAI : {e}")

