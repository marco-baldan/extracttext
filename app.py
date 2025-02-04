import streamlit as st
import cv2
import pytesseract
import numpy as np
from PIL import Image

st.title("Live Ski Pass OCR Scanner")
st.write("Scan the ski pass text in real-time. Once detected, it will freeze and populate the text box.")

# Open camera feed
camera_input = st.camera_input("Take a picture of the ski pass")

if camera_input is not None:
    image = Image.open(camera_input)
    img_cv = np.array(image)
    
    # Perform OCR
    text = pytesseract.image_to_string(img_cv)
    
    if text.strip():
        st.text_input("Extracted Ski Pass Number:", text, key="ocr_output", disabled=True)
    else:
        st.error("No text detected. Try again with better lighting.")