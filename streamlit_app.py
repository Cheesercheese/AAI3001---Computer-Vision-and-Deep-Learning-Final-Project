import streamlit as st
from PIL import Image

st.title("Computer Vision and Deep Learning Final Project")
st.header("Test data information")
st.write("There are 6 total subclasses in the dataset. The image bellow shows the classes and their classification number.")

# Load and display the image
image_path = "images/classes.png"
try:
    image = Image.open(image_path)
    st.image(image, caption="Defined classes in config.yaml", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

st.write("The datasets are split into images and labels where the labels each correspond to the same number image number. This is a requirement for YOLO. The labels are in .txt")

st.header("Training the model")
st.write("The model ran for 100 epochs. After the training, it outputs the file  \"runs\" which contains images that shows what the training batch looks like and what the output of the prediction looks like. Examples of what this looks like are attached below.")

# Load and display the image
image_path = "runs/detect/train/train_batch2520.jpg"
try:
    image = Image.open(image_path)
    st.image(image, caption="Example of training data", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

# Load and display the image
image_path = "runs/detect/train/val_batch1_pred.jpg"
try:
    image = Image.open(image_path)
    st.image(image, caption="Example of predicted fishes", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

st.header("Results of model accuracy and training data")
st.subheader("Confusion Matrix")

# Load and display the image
image_path = "runs/detect/train/confusion_matrix_normalized.png"  # Ensure this path is correct
try:
    image = Image.open(image_path)
    st.image(image, caption="Normalized confusion matrix", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

st.subheader("F1 Confidence Curve")

# Load and display the image
image_path = "runs/detect/train/F1_curve.png"  # Ensure this path is correct
try:
    image = Image.open(image_path)
    st.image(image, caption="F1 Confidence Curve", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

st.subheader("Precision Confidence Curve")

# Load and display the image
image_path = "runs/detect/train/P_curve.png"  # Ensure this path is correct
try:
    image = Image.open(image_path)
    st.image(image, caption="Precision confidence curve", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

st.subheader("Precision Recall Curve")

# Load and display the image
image_path = "runs/detect/train/PR_curve.png"  # Ensure this path is correct
try:
    image = Image.open(image_path)
    st.image(image, caption="Precision recall curve", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

st.subheader("Recall Confidence Curve")

# Load and display the image
image_path = "runs/detect/train/R_curve.png"  # Ensure this path is correct
try:
    image = Image.open(image_path)
    st.image(image, caption="Recall confidence curve", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")

st.subheader("Training results")

# Load and display the image
image_path = "runs/detect/train/results.png"  # Ensure this path is correct
try:
    image = Image.open(image_path)
    st.image(image, caption="Overall training statistics", use_column_width=True)
except FileNotFoundError:
    st.error(f"File {image_path} not found. Please ensure the path is correct.")
