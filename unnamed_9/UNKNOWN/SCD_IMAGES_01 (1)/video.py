# import cv2
# import os
# import pydicom

# def create_video(images_folder, output_video_path, frame_rate=30):
#     dicom_files = [file for file in os.listdir(images_folder) if file.endswith(".dcm")]
#     dicom_files.sort()

#     first_dicom = pydicom.dcmread(os.path.join(images_folder, dicom_files[0]))
#     height, width = first_dicom.Rows, first_dicom.Columns

#     # video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))
#     video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), frame_rate, (width, height))


#     for dicom_file in dicom_files:
#         dicom_data = pydicom.dcmread(os.path.join(images_folder, dicom_file))
#         image = dicom_data.pixel_array
#         video.write(cv2.resize(image, (width, height)))

#     cv2.destroyAllWindows()
#     video.release()

# if __name__ == "__main__":
#     # Use double backslashes or a raw string for the path
#     images_folder = r"4DFlowNet\unnamed_9\UNKNOWN\SCD_IMAGES_01 (1)\18.9873409\CINELAX_Series0301"
#     output_video_path = "data/output.mp4"

#     create_video(images_folder, output_video_path)


from PIL import Image
import cv2
import os

def create_video(images_folder, output_video_path, frame_rate=30):
    images = [img for img in os.listdir(images_folder) if img.endswith(".png")]
    images.sort()

    if not images:
        print("No images found in the specified folder.")
        return

    first_image_path = os.path.join(images_folder, images[0])
    
    try:
        first_image = Image.open(first_image_path)
        width, height = first_image.size
    except Exception as e:
        print(f"Failed to load the first image: {first_image_path}")
        print(f"Error: {e}")
        return

    video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))

    for image in images:
        image_path = os.path.join(images_folder, image)
        
        try:
            img = Image.open(image_path)
            img_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            video.write(img_np)
        except Exception as e:
            print(f"Failed to load image: {image_path}")
            print(f"Error: {e}")

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    # Use relative paths based on the script location
    images_folder = "4DFlowNet\unnamed_9\UNKNOWN\SCD_IMAGES_01 (1)\18.9873409\CINELAX_Series0301"
    output_video_path = "data/output.mp4"

    create_video(images_folder, output_video_path)
