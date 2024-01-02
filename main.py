import os
import argparse
from enhance import enhance_image
from boundingbox import drawbox
from cv2 import imwrite,imread

def save_result(image,image_path):
    result = drawbox(image)
    output_path = os.path.join("outputs", os.path.basename(image_path))
    print(output_path)
    imwrite(output_path, result)
    print("image saved")

def process_images(images_directory):
    # Ensure the output directory exists
    output_directory = "outputs"
    os.makedirs(output_directory, exist_ok=True)

    # Iterate over images in the specified directory
    for filename in os.listdir(images_directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(images_directory, filename)
            image = imread(image_path)
            image = enhance_image(image) #enhances the image, saves it and then returns the enhanced image
            save_result(image,image_path)

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Process images and save results")
    parser.add_argument("images_directory", type=str, help="Path to the directory containing images")

    # Parse command-line arguments
    args = parser.parse_args()

    # Process images in the specified directory
    process_images(args.images_directory)
