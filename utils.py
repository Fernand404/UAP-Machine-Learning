import streamlit as st
import tensorflow as tf

@st.cache_resource
def load_model_file(path):
    # Load murni tanpa embel-embel custom_objects
    return tf.keras.models.load_model(path, compile=False)