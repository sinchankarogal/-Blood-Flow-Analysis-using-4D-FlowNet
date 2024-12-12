# import os
# from PIL import Image, ImageTk
# import tkinter as tk
# import pydicom
# import numpy as np


# def load_dicom_series(directory):
#     slices = [pydicom.dcmread(os.path.join(directory, file)) for file in os.listdir(directory)]
#     slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
#     volume = [s.pixel_array for s in slices]
#     return volume

# def display_dicom_images(dicom_folder):
#     dicom_images = load_dicom_series(dicom_folder)

#     root = tk.Tk()
#     root.title("DICOM Image Viewer")

#     for image in dicom_images:
#         # Normalize to 8-bit for display
#         normalized_image = ((image - np.min(image)) / (np.max(image) - np.min(image)) * 255).astype(np.uint8)
#         img = Image.fromarray(normalized_image)

#         # Display the image using Tkinter
#         tk_image = ImageTk.PhotoImage(img)
#         label = tk.Label(root, image=tk_image)
#         label.pack()

#         # Close the window after 1000 milliseconds (1 second)
#         root.after(1000, label.destroy)

#         root.update_idletasks()
#         root.update()

#     root.mainloop()

# # Replace 'path/to/your/dicom/folder' with your actual path
# dicom_folder_path = 'images'
# display_dicom_images(dicom_folder_path)


# import os
# import numpy as np
# import cv2
# import pydicom

# def load_dicom_series(directory):
#     slices = [pydicom.dcmread(os.path.join(directory, file)) for file in os.listdir(directory)]
#     slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
#     volume = [s.pixel_array for s in slices]
#     return volume

# def display_dicom_images(dicom_folder):
#     dicom_images = load_dicom_series(dicom_folder)

#     for image in dicom_images:
#         # Normalize to 8-bit for display
#         normalized_image = ((image - np.min(image)) / (np.max(image) - np.min(image)) * 255).astype(np.uint8)
        
#         # Display the image using OpenCV
#         cv2.imshow('DICOM Image Viewer', normalized_image)
#         cv2.waitKey(1000)  # Show image for 1 second
#         cv2.destroyAllWindows()

# # Replace 'path/to/your/dicom/folder' with your actual path
# dicom_folder_path = 'images'
# display_dicom_images(dicom_folder_path)


import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Function to read video frames and labels from a folder
def load_video_frames(video_folder):
    frames = []
    labels = []
    
    for filename in os.listdir(video_folder):
        if filename.lower().endswith('.png'):
            frame_path = os.path.join(video_folder, filename)
            frame = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE)
            frames.append(frame)
            
            # Assuming the label is encoded in the filename (0 or 1)
            label = int(filename.split('_')[0])  
            labels.append(label)
    
    return np.array(frames), np.array(labels)

# Load video frames and labels
video_folder = 'images'
X, y = load_video_frames(video_folder)

# Split the dataset into training and testing sets
if len(X) == 0:
    print("Error: Your dataset is empty. Make sure you have video frames in the specified folder.")
else:
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple convolutional neural network (CNN) model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(X_train.shape[1], X_train.shape[2], 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Expand dimensions to match CNN input shape
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model on the test set
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
