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
            cv2.waitKey(int(100000 / frame_rate / slow_down_factor))

        else:
            print(f"Skipping unreadable image file: {image_path}")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    images_folder = "highres"
    display_video(images_folder, slow_down_factor=2)


# import cv2
# import os
# import imageio

# def save_frames_as_gif(images_folder, output_gif_path, frame_rate=30, slow_down_factor=2):
#     image_files = [file for file in os.listdir(images_folder) if file.lower().endswith('.png')]
#     image_files.sort()

#     if not image_files:
#         print("No PNG files found in the specified folder.")
#         return

#     # Read the first image file to get dimensions
#     first_image_path = os.path.join(images_folder, image_files[0])
#     first_image = cv2.imread(first_image_path)

#     if first_image is None:
#         print(f"Unable to read the first image file: {first_image_path}")
#         return

#     height, width, _ = first_image.shape

#     images = []
#     for image_file in image_files:
#         image_path = os.path.join(images_folder, image_file)
#         image = cv2.imread(image_path)

#         if image is not None:
#             # Resize the image to match the dimensions of the first image
#             image = cv2.resize(image, (width, height))

#             # Append the image to the list of frames
#             images.append(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#         else:
#             print(f"Skipping unreadable image file: {image_path}")

#     # Save frames as GIF with adjusted duration
#     imageio.mimsave(output_gif_path, images, duration=1.0 / frame_rate * slow_down_factor)

# if __name__ == "__main__":
#     images_folder = "highres"
#     output_gif_path = "outputhigh.gif"
#     save_frames_as_gif(images_folder, output_gif_path, slow_down_factor=2)





# import cv2
# import os

# def save_frames_as_video(images_folder, output_video_path, frame_rate=30, slow_down_factor=2):
#     image_files = [file for file in os.listdir(images_folder) if file.lower().endswith('.png')]
#     image_files.sort()

#     if not image_files:
#         print("No PNG files found in the specified folder.")
#         return

#     # Read the first image file to get dimensions
#     first_image_path = os.path.join(images_folder, image_files[0])
#     first_image = cv2.imread(first_image_path)

#     if first_image is None:
#         print(f"Unable to read the first image file: {first_image_path}")
#         return

#     height, width, _ = first_image.shape

#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format
#     output_video = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

#     for image_file in image_files:
#         image_path = os.path.join(images_folder, image_file)
#         image = cv2.imread(image_path)

#         if image is not None:
#             # Resize the image to match the dimensions of the first image
#             image = cv2.resize(image, (width, height))

#             # Write the frame to the video
#             output_video.write(image)

#             # Adjust the delay to slow down the video
#             cv2.waitKey(int(100000 / frame_rate / slow_down_factor))

#         else:
#             print(f"Skipping unreadable image file: {image_path}")

#     # Release the VideoWriter object
#     output_video.release()

# if __name__ == "__main__":
#     images_folder = "highres"
#     output_video_path = "output_high.mp4"
#     save_frames_as_video(images_folder, output_video_path, slow_down_factor=2)
