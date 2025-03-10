# Q&A Chatbot
#from langchain.llms import OpenAI

import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Configure Gemini API
genai.configure(api_key="AIzaSyD9BekTB0ncpJ8tq0qudsHDgYwjt4uFcuU")  # Replace with your actual API key

# Streamlit UI
st.title("ProVisionAI: Image Annotation with Gemini Vision")
st.write("Upload an image to get AI-generated annotations.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")  # Convert to PNG format
    img_bytes.seek(0)  # Reset stream position

    # Prepare image for Gemini API
    img_blob = {
        "mime_type": "image/png",
        "data": img_bytes.getvalue(),
    }

    # Call Gemini Vision API
    model = genai.GenerativeModel("gemini-1.5-flash")  # Ensure you're using the correct model
    response = model.generate_content([img_blob])

    # Display the response
    st.subheader("AI-generated Description:")
    st.write(response.text if response else "No description generated.")
