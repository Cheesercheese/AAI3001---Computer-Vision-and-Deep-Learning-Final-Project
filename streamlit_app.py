import streamlit as st
from PIL import Image

# Set title
st.title("Display results.png")

# Load and display the image
image_path = "/runs/detect/train/results.png"  # Ensure this path is correct
try:
    image = Image.open(image_path)
    st.image(image, caption="Results", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

# Example Inference: Add some dummy output
st.subheader("Inference Result")
if uploaded_file:
    st.write("This is a sample inference result!")
else:
    st.write("Upload a PNG file to see the result.")
