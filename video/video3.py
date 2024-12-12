import pydicom
import cv2
import os
import imageio

def display_video(images_folder, output_gif_path, frame_rate=30):
    dicom_files = [file for file in os.listdir(images_folder) if file.lower().endswith('.dcm')]
    dicom_files.sort()

    if not dicom_files:
        print("No DICOM files found in the specified folder.")
        return

    # Read the first DICOM file to get dimensions
    first_dicom_path = os.path.join(images_folder, dicom_files[0])
    first_dicom = pydicom.dcmread(first_dicom_path)

    if first_dicom is None:
        print(f"Unable to read the first DICOM file: {first_dicom_path}")
        return

    height, width = first_dicom.Rows, first_dicom.Columns

    images = []
    for dicom_file in dicom_files:
        dicom_path = os.path.join(images_folder, dicom_file)
        dicom = pydicom.dcmread(dicom_path)

        if dicom is not None:
            # Convert DICOM pixel data to numpy array
            image_array = dicom.pixel_array

            # Convert 16-bit to 8-bit for displaying with OpenCV
            image_array = cv2.normalize(image_array, None, 0, 255, cv2.NORM_MINMAX)
            image_array = image_array.astype('uint8')

            # Convert grayscale to RGB
            image_rgb = cv2.cvtColor(image_array, cv2.COLOR_GRAY2RGB)

            # Save the frame as an image
            images.append(image_rgb)

            # Display the image (optional)
            cv2.imshow('DICOM Video', image_rgb)
            cv2.waitKey(int(10000 / frame_rate))

        else:
            print(f"Skipping unreadable DICOM file: {dicom_path}")

    # Save frames as GIF
    imageio.mimsave(output_gif_path, images, duration=1.0 / frame_rate)

    # Close OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    images_folder = "aorta"
    output_gif_path = "output_video.gif"
    display_video(images_folder, output_gif_path)
