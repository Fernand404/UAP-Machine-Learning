import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from utils import load_model_file
import json

def show_page():
    st.header("Analisis MobileNetV2")
    
    with open('class_names.json', 'r') as f:
        class_names = json.load(f)

    # Gunakan file .keras hasil training Functional API
    model = load_model_file("potato_mobilenet_model.keras")
    uploaded_file = st.file_uploader("Upload Foto Kentang", type=["jpg", "png"], key="mobilenet")

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, width=300)
        
        if st.button("Prediksi dengan MobileNet"):
            img = image.resize((224, 224))
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            
            # JANGAN GUNAKAN preprocess_input bawaan mobilenet di sini
            # Biarkan img_array berisi nilai 0-255 sesuai data training Anda
            
            preds = model.predict(img_array)
            result_index = np.argmax(preds[0])
            label = class_names[result_index]
            conf = np.max(preds[0]) * 100
            
            st.success(f"Hasil: {label} ({conf:.2f}%)")