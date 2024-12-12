import pydicom
import cv2
import os

def save_video_frames(images_folder, output_folder, frame_rate=30):
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

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for idx, dicom_file in enumerate(dicom_files):
        dicom_path = os.path.join(images_folder, dicom_file)
        dicom = pydicom.dcmread(dicom_path)

        if dicom is not None:
            # Convert DICOM pixel data to numpy array
            image_array = dicom.pixel_array

            # Convert 16-bit to 8-bit for saving with OpenCV
            image_array = cv2.normalize(image_array, None, 0, 255, cv2.NORM_MINMAX)
            image_array = image_array.astype('uint8')

            # Convert grayscale to RGB
            image_rgb = cv2.cvtColor(image_array, cv2.COLOR_GRAY2RGB)

            # Save the image
            output_path = os.path.join(output_folder, f"frame_{idx + 1}.png")
            cv2.imwrite(output_path, image_rgb)

            print(f"Frame {idx + 1} saved: {output_path}")

        else:
            print(f"Skipping unreadable DICOM file: {dicom_path}")

if __name__ == "__main__":
    images_folder = "aorta"
    output_folder = "output_frames"
    save_video_frames(images_folder, output_folder)
