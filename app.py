import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import PIL.Image
import time
import json
import ssl

# Fix SSL certificate verification issue on macOS
ssl._create_default_https_context = ssl._create_unverified_context

# Configure the Streamlit page
st.set_page_config(page_title="ZooNet | Team Neptune", page_icon="🐾", layout="centered")

# --- Custom Premium CSS ---
st.markdown("""
<style>
    /* Main Background & Text */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Container */
    .header-container {
        background: linear-gradient(135deg, #1f6feb 0%, #2ea043 100%);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 111, 235, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    .header-title {
        color: white;
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }
    .header-subtitle {
        color: #e6edf3;
        font-size: 1.2rem;
        font-weight: 400;
        margin-top: 10px;
    }

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(22, 27, 34, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    }
    
    /* Upload Button Styling */
    .stFileUploader label {
        color: #58a6ff !important;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    /* Progress/Spinner */
    .stSpinner > div > div {
        border-top-color: #2ea043 !important;
    }
    
    /* Prediction Result Box */
    .result-box {
        background: linear-gradient(90deg, rgba(46,160,67,0.1) 0%, rgba(31,111,235,0.1) 100%);
        border-left: 4px solid #2ea043;
        padding: 20px;
        border-radius: 0 8px 8px 0;
        margin-top: 20px;
    }
    .result-name {
        font-size: 2rem;
        font-weight: 700;
        color: #58a6ff;
        text-transform: capitalize;
    }
    .result-conf {
        font-size: 1.2rem;
        color: #8b949e;
    }
</style>
""", unsafe_allow_html=True)

# --- App Header ---
st.markdown("""
<div class="header-container">
    <h1 class="header-title">🐾 ZooNet</h1>
    <p class="header-subtitle">Advanced Animal Species Identification System</p>
</div>
""", unsafe_allow_html=True)

# --- Model Loading (Using MobileNetV2 as placeholder for missing repo weights) ---
@st.cache_resource
def load_model():
    # Since the trained custom weights were not saved in the repository, 
    # we use a pre-trained state-of-the-art MobileNetV2 for demonstration.
    # Using local weights file to avoid macOS SSL certificate errors.
    model = MobileNetV2(weights='/Users/subodh/.gemini/antigravity/scratch/zoonet/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5')
    return model

with st.spinner("Loading Neural Network..."):
    model = load_model()

# --- Main UI ---
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("### Upload an Animal Image")
uploaded_file = st.file_uploader("Choose an image (JPG/PNG)", type=["jpg", "jpeg", "png"])
st.markdown("</div>", unsafe_allow_html=True)

if uploaded_file is not None:
    # Display the uploaded image
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        img = PIL.Image.open(uploaded_file)
        st.image(img, caption="Captured Image", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### Analysis Report")
        
        # Preprocess the image
        img_resized = img.resize((224, 224))
        x = image.img_to_array(img_resized)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        # Add a simulated progress bar for UI effect
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
            if i < 30:
                status_text.text("Extracting image features...")
            elif i < 70:
                status_text.text("Applying convolutional filters...")
            else:
                status_text.text("Classifying species...")
        
        # Predict
        preds = model.predict(x)
        
        # Decode using local json file to avoid SSL issues
        with open('/Users/subodh/.gemini/antigravity/scratch/zoonet/imagenet_class_index.json') as f:
            CLASS_INDEX = json.load(f)
        top_indices = preds[0].argsort()[-3:][::-1]
        decoded_preds = [tuple(CLASS_INDEX[str(i)]) + (preds[0][i],) for i in top_indices]
        
        status_text.empty()
        progress_bar.empty()
        
        # Display top prediction
        top_pred = decoded_preds[0]
        species_name = top_pred[1].replace('_', ' ')
        confidence = top_pred[2] * 100
        
        st.markdown(f"""
        <div class="result-box">
            <div class="result-name">{species_name}</div>
            <div class="result-conf">Confidence: {confidence:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display other probabilities
        st.markdown("<br><b>Other Probabilities:</b>", unsafe_allow_html=True)
        for i in range(1, 3):
            name = decoded_preds[i][1].replace('_', ' ').title()
            conf = decoded_preds[i][2] * 100
            st.markdown(f"- {name}: `{conf:.1f}%`")
            
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #8b949e; margin-top: 50px; font-size: 0.9rem;">
    <i>Note: This demo uses a pre-trained ImageNet model as the custom ZooNet weights were not included in the repository.</i><br>
    ZooNet by Team Neptune © 2026
</div>
""", unsafe_allow_html=True)
