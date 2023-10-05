import cv2
import numpy as np

def process_image(image_path, output_path):
    # Read the image
    image = cv2.imread(r"C:/Users/liys2/Desktop/Numocr/212.jpg")

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define the kernel for dilation and erosion
    kernel = np.ones((5, 5), np.uint8)

    # Perform dilation and erosion
    dilated_image = cv2.dilate(gray_image, kernel, iterations=1)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=1)

    # Write the eroded image to a file
    cv2.imwrite(output_path, eroded_image)

    # Apply thresholding to get a binary image
    _, binary_image = cv2.threshold(eroded_image, 128, 255, cv2.THRESH_BINARY)

    # Write the binary image to a file
    cv2.imwrite("binary_image.jpg", binary_image)

# Replace 'input_image.jpg' with the path to your input image file
input_image_path = 'input_image.jpg'

# Replace 'output_image.jpg' with the desired output file path for the processed image
output_image_path = 'output_image.jpg'

# Call the function to process the image
process_image(input_image_path, output_image_path)
