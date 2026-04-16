import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# ✅ CORRECT MODEL PATH
model = tf.keras.models.load_model("/content/drive/MyDrive/best_bird_drone_model.h5")

st.title("🦅 Bird vs Drone Classifier")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

def preprocess(image):
    image = image.resize((224,224))
    image = np.array(image)/255.0
    image = np.expand_dims(image, axis=0)
    return image

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img)

    img = preprocess(img)
    pred = model.predict(img)[0][0]

    if pred > 0.5:
        label = "🚁 Drone"
        confidence = pred
    else:
        label = "🦅 Bird"
        confidence = 1 - pred

    st.write(f"Prediction: {label}")
    st.write(f"Confidence: {confidence:.2f}")
