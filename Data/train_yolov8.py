from ultralytics import YOLO

# Create a YOLOv8s object and load the pre-trained model
model = YOLO('models/yolov8/yolov8s.pt')  # Use yolov8s instead of yolov8m

# Training parameters
data_yaml = 'data/data.yaml'  # Path to your data.yaml configuration file
img_size = 1280  # Image size for training
epochs = 50
batch_size = 8

# Start training
results = model.train(
    data=data_yaml,
    imgsz=img_size,
    epochs=epochs,
    batch=batch_size,  # Use 'batch' argument, not 'batch_size'
    name='yolov8s_50e'  # Update the name accordingly
)

# Debug: Print or log the results for debugging purposes
print(results)

# Save the trained model
model.save('yolov8s_trained')  # Update the saved model name

# Export the results
results.export()
