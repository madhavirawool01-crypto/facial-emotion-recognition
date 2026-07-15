import streamlit as st
from deepface import DeepFace
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Facial Emotion Recognition",
    page_icon="😊",
    layout="centered"
)

# Title
st.title("😊 Facial Emotion Recognition")
st.write("Upload an image to detect the dominant facial emotion.")

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Display uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing emotion..."):
        try:
            # Analyze emotion
            result = DeepFace.analyze(
                img_array,
                actions=["emotion"],
                enforce_detection=False
            )

            emotion = result[0]["dominant_emotion"]
            emotions = result[0]["emotion"]

            st.success(f"🎉 Detected Emotion: **{emotion.upper()}**")

            st.subheader("Emotion Confidence Scores")

            for emo, score in emotions.items():
                st.progress(int(score))
                st.write(f"**{emo.capitalize()}** : {score:.2f}%")

        except Exception as e:
            st.error("Unable to analyze the image.")
            st.error(str(e))

st.markdown("---")
st.caption("Developed using Python, Streamlit, OpenCV, DeepFace, and TensorFlow.")
