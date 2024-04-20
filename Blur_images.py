import cv2
import os

# Function to apply blur effect to an image
def apply_blur(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    blurred_image = cv2.GaussianBlur(image, (37, 37), 0)  # You can adjust the kernel size for different blur intensity
    cv2.imwrite(output_image_path, blurred_image)

# Folder containing input images
input_folder = ".\\dataset_fifth\\train\\images"

# Folder to save blurred images
output_folder = ".\\dataset_fifth\\train\\New folder"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Apply blur effect to each image in the input folder
for image_name in os.listdir(input_folder):
    input_image_path = os.path.join(input_folder, image_name)
    output_image_path = os.path.join(output_folder, image_name)
    apply_blur(input_image_path, output_image_path)
