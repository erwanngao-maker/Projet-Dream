import streamlit as st
import json
import os
from image_generator import generate_image

DATA_PATH = "data/dreams.json"
IMAGE_FOLDER = "Images"

st.set_page_config(page_title="Dream Interpreter", layout="centered")

st.title("🌙 Dream Interpreter")
st.write("Application de visualisation et génération d'images à partir d’un rêve.")

def load_dreams():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_dreams(dreams):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(dreams, f, indent=4, ensure_ascii=False)

dreams = load_dreams()

if not dreams:
    st.warning("Aucun rêve trouvé dans data/dreams.json")
else:
    selected_index = st.selectbox(
        "Choisir un rêve",
        range(len(dreams)),
        format_func=lambda i: dreams[i].get("summary", f"Rêve {i+1}")
    )

    dream = dreams[selected_index]

    st.subheader("📝 Rêve")
    st.write(dream.get("dream", ""))

    st.subheader("📄 Résumé")
    st.write(dream.get("summary", ""))

    st.subheader("🔮 Interprétation")
    st.write(dream.get("interpretation", ""))

    if dream.get("image_path") and os.path.exists(dream["image_path"]):
        st.subheader("🖼️ Image existante")
        st.image(dream["image_path"])

    if st.button("🎨 Générer une nouvelle image"):
        prompt = dream.get("interpretation") or dream.get("dream")

        with st.spinner("Génération de l'image en cours..."):
            image_path = generate_image(prompt)

        if image_path:
            dream["image_path"] = image_path
            save_dreams(dreams)
            st.success("Image générée et sauvegardée avec succès.")
            st.image(image_path)
        else:
            st.error("Erreur lors de la génération.")