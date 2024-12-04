import streamlit as st
from PIL import Image

# Title
st.title("PNG Inference Web Application")

# Upload PNG
uploaded_file = st.file_uploader("Upload a PNG image", type=["png"])

if uploaded_file:
    # Open image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded PNG", use_column_width=True)

# Example Inference: Add some dummy output
st.subheader("Inference Result")
if uploaded_file:
    st.write("This is a sample inference result!")
else:
    st.write("Upload a PNG file to see the result.")
