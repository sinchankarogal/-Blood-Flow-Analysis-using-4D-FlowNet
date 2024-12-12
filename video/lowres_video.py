import cv2
import os

def display_video(images_folder, frame_rate=30, slow_down_factor=2):
    image_files = [file for file in os.listdir(images_folder) if file.lower().endswith('.png')]
    image_files.sort()

    if not image_files:
        print("No PNG files found in the specified folder.")
        return

    # Read the first image file to get dimensions
    first_image_path = os.path.join(images_folder, image_files[0])
    first_image = cv2.imread(first_image_path)

    if first_image is None:
        print(f"Unable to read the first image file: {first_image_path}")
        return

    height, width, _ = first_image.shape

    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        image = cv2.imread(image_path)

        if image is not None:
            # Display the image
            cv2.imshow('PNG Video', image)
            
            # Adjust the delay to slow down the video
            cv2.waitKey(int(10000 / frame_rate / slow_down_factor))

        else:
            print(f"Skipping unreadable image file: {image_path}")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    images_folder = "lowres"
    display_video(images_folder, slow_down_factor=2)
