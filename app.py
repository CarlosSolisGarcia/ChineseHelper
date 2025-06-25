import numpy as np
import streamlit as st
from PIL import Image
from streamlit import session_state

from utils.text_processing import convert_to_simplified, convert_to_traditional, read_text_from_image

st.title("CSolis的中文助手")

st.header("我怎么帮你?")

available_tasks = [
    "Text Recognition (OCR)",
    "Traditional ⇌ Simplified",
    "Coming soon"]

chosen_task = st.segmented_control(label="Tasks:",
                     options=available_tasks,
                     selection_mode="single")

if chosen_task == available_tasks[0]:
    ### OCR Branch
    st.write("Great, let me help you with your chosen image.")
    uploaded_image = st.file_uploader(
        label="Upload an image of a text you would like to process",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_image is not None:
        # Abrir imagen con PIL
        image = Image.open(uploaded_image)
        image = image.convert("RGB")
        image_np = np.array(image)

        # Mostrar la imagen en la app
        st.image(image, caption="Uploaded image", use_container_width=True)

        # Mostrar el texto convertido
        img_text = read_text_from_image(image_np)

        st.write(img_text)


elif chosen_task == available_tasks[1]:
    st.write("Please, tell me what you would like to convert.")

    if 'last_changed' not in st.session_state:
        st.session_state.last_changed = None
    if 'traditional_text' not in st.session_state:
        st.session_state.traditional_text = ""
    if 'simplified_text' not in st.session_state:
        st.session_state.simplified_text = ""

    def on_trad_change():
        st.session_state.last_changed = "trad"
        st.session_state.simplified_text = convert_to_simplified(st.session_state.traditional_text)

    def on_simp_change():
        st.session_state.last_changed = "simp"
        st.session_state.traditional_text = convert_to_traditional(st.session_state.simplified_text)

    st.text_area(
        "Traditional Chinese| 繁体中文",
        value=st.session_state.traditional_text,
        key="Traditional text",
        on_change=on_simp_change(),
        height=75,
    )

    st.text_area(
        "Simplified Chinese | 简体中文",
        value=session_state.simplified_text,
        on_change=on_simp_change(),
        key="simplified_text",
        height=75,
    )

else:
    st.write("New features coming soon!")

# Sidebar block
with st.sidebar:
    st.header("介绍一下!: About me.")
    st.write("欢迎你！这是中文助手。")
    st.write("My name is Carlos, "
             "I built this small app in order to help me study chinese.")