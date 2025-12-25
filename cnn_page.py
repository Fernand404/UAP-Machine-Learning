import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from utils import load_model_file
import json

def show_page():
    st.header("Analisis CNN Custom") # Judul diperbaiki
    
    with open('class_names.json', 'r') as f:
        class_names = json.load(f)

    # Pastikan memanggil file .h5 atau .keras milik CNN Custom
    model = load_model_file("potato_disease_model.h5") 
    uploaded_file = st.file_uploader("Upload Foto Kentang", type=["jpg", "png"], key="cnn_unique")

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, width=300)
        
        if st.button("Prediksi dengan CNN Custom"):
            # 1. Resize harus 256x256 sesuai training di Colab
            img = image.resize((256, 256)) 
            
            # 2. Konversi ke array
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            
            # PENTING: JANGAN dibagi 255 lagi di sini karena 
            # model Anda sudah punya layer Rescaling(1./255) di dalamnya.
            # JANGAN gunakan preprocess_input milik VGG/MobileNet di sini.

            # 3. Prediksi
            preds = model.predict(img_array)
            
            # 4. Ambil hasil
            result_index = np.argmax(preds[0])
            label = class_names[result_index]
            conf = np.max(preds[0]) * 100
            
            st.success(f"Hasil: {label} ({conf:.2f}%)")