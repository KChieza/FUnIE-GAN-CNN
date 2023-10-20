import cv2
import os
import numpy as np


# Define the input and output folders
input_path = r"2013_aldabra_relabelled.v3i.tensorflow"
output_path = r"train_Sharpened"

folder = "train"

# Define the input and output folders
input_folder = os.path.join(input_path, folder)
output_folder = os.path.join(output_path, folder)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the sharpening kernel 
kernel = np.array([[0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]])

input_files = os.listdir(input_folder)
output_files = os.listdir(output_folder)

# Loop through each image file in the input folder
for file_name in input_files:

    # Construct the full path of the input image
    input_image_path = os.path.join(input_folder, file_name)
    
    # Load the input image
    input_image = cv2.imread(input_image_path)
    
    # Apply the sharpening kernel to the image using filter2D function
    sharpened_image = cv2.filter2D(input_image, -1, kernel)
    
    # Construct the full path of the output image
    output_image_path = os.path.join(output_folder, file_name)
    
    # Save the sharpened image to the output folder
    cv2.imwrite(output_image_path, sharpened_image)

print("Sharpening completed. Sharpened images are saved in:", output_folder)
