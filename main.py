from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("yolo11n.yaml")

# Train the model using the 'config.yaml' dataset for x epochs
results = model.train(data="config.yaml", epochs=100)
