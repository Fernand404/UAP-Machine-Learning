import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from utils import load_model_file
import json

def show_page():
    st.header("Analisis ResNet50")
    st.info("ResNet50 menggunakan Residual Connections untuk akurasi yang lebih dalam dan stabil.")
    
    # 1. Load Class Names
    with open('class_names.json', 'r') as f:
        class_names = json.load(f)

    # 2. Load Model (.keras format)
    # Pastikan di utils.py load_model_file menggunakan compile=False
    model = load_model_file("potato_resnet_model.keras")
    
    uploaded_file = st.file_uploader("Upload Foto Kentang (ResNet)", type=["jpg", "png"], key="resnet_upload")

    if uploaded_file:
        image = Image.open(uploaded_file).convert('RGB') # Pastikan format RGB
        st.image(image, width=300, caption="Gambar Terunggah")
        
        if st.button("Prediksi dengan ResNet50"):
            with st.spinner('Sedang menganalisis...'):
                # --- PROSES PREPROCESSING RESNET ---
                # A. Resize sesuai input training (224x224)
                img = image.resize((224, 224))
                
                # B. Konversi ke Array
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                
                # C. Tambah Dimensi Batch
                img_array = np.expand_dims(img_array, axis=0)
                
                # D. WAJIB: Gunakan Preprocessing ResNet50
                # Ini akan mengubah RGB ke BGR dan Zero-Centering
                img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
                
                # 3. Eksekusi Prediksi
                preds = model.predict(img_array)
                
                # 4. Ambil Hasil
                result_index = np.argmax(preds[0])
                label = class_names[result_index]
                conf = np.max(preds[0]) * 100
                
                # Tampilkan Hasil
                st.subheader(f"Hasil: {label}")
                st.write(f"Tingkat Kepercayaan: **{conf:.2f}%**")
                
                if conf < 60:
                    st.warning("⚠️ Keyakinan model rendah. Pastikan foto jelas dan fokus pada bagian kentang.")