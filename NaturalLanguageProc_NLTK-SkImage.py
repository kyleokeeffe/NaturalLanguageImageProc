#COMP-318 Group Assignment

import numpy as np
from skimage.transform import rotate
from skimage.filters import threshold_otsu
from skimage import io, filters, color, util, img_as_ubyte
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# Request input from user
user_input = input("Please provide your request: ")

# Tokenize and convert to lowercase
tokens = word_tokenize(user_input.lower())

# Define keywords
blur_keywords = ['blur', 'blurring', 'blurry', 'apply blur', 'add blur', 'image blur']
edge_keywords = ['edge', 'edges', 'edge detection', 'detect edges', 'highlight edges']
invert_keywords = ['invert', 'inverse', 'invert colors', 'invert image', 'inversion']
rotate_keywords = ['rotate', 'rotation', 'turn', 'twist']
threshold_keywords = ['threshold', 'binary', 'thresholding', 'convert to binary']

# Check for blurring request
if any(keyword in tokens for keyword in blur_keywords):
    print("The input contains a request to blur an image.")
    image_path = input("Please provide the path to the image you want to blur: ")
    # Ask the user for the blurring intensity
    try:
        sigma_value = float(input("Please specify the blurring intensity (e.g., 1 for light blur, 5 for more blur): "))
    except ValueError:
        print("Invalid blurring intensity provided. Using default value of 1.")
        sigma_value = 1
    try:
        # Load the image using skimage
        image = io.imread(image_path)
        # Apply Gaussian blur operation with the user-specified sigma
        blurred_image = filters.gaussian(image, sigma=sigma_value)
        # Convert the blurred image to uint8 before saving
        blurred_image_uint8 = img_as_ubyte(blurred_image)
        # Save the blurred image
        blurred_image_path = f"blurred_image_sigma_{sigma_value}.png"
        io.imsave(blurred_image_path, blurred_image_uint8)
        print(f"Image has been blurred with intensity {sigma_value} and saved as:", blurred_image_path)
    except Exception as e:
        print("Error:", str(e))

# Check for edge detection request
elif any(keyword in tokens for keyword in edge_keywords):
    print("The input contains a request to detect edges in an image.")
    image_path = input("Please provide the path to the image you want to process for edge detection: ")
    try:
        # Load the image using skimage
        image = io.imread(image_path)
        # Convert image to grayscale as edge detection typically works on grayscale images
        gray_image = color.rgb2gray(image)
        # Apply Sobel edge detection
        edges = filters.sobel(gray_image)
        #Convert array to RGB
        edges_RGB = (edges * 255).round().astype(np.uint8)
        # Save the edge-detected image
        edge_image_path = "edges_image.png"
        io.imsave(edge_image_path, edges_RGB, cmap="gray")
        #print("edge detection complete")
        print("Edge detection has been applied and saved as:", edge_image_path)
    except Exception as e:
        print("Error:", str(e))

# Check for inversion request
elif any(keyword in tokens for keyword in invert_keywords):
    print("The input contains a request to invert the image colors.")
    image_path = input("Please provide the path to the image you want to invert: ")
    try:
        # Load the image using skimage
        image = io.imread(image_path)
        # Invert the image
        inverted_image = util.invert(image)
        # Save the inverted image
        inverted_image_path = "inverted_image.png"
        io.imsave(inverted_image_path, inverted_image)
        print("Image colors have been inverted and saved as:", inverted_image_path)
    except Exception as e:
        print("Error:", str(e))

# Check for rotation request
elif any(keyword in tokens for keyword in rotate_keywords):
    print("The input contains a request to rotate the image.")
    image_path = input("Please provide the path to the image you want to rotate: ")
    try:
        angle = float(input("Please specify the rotation angle (in degrees): "))
    except ValueError:
        print("Invalid angle provided. Using default value of 90 degrees.")
        angle = 90
    try:
        # Load the image using skimage
        image = io.imread(image_path)
        # Rotate the image by the specified angle
        rotated_image = rotate(image, angle, resize=True)
        #Convert array to RGB
        rotated_image_RGB = (rotated_image * 255).round().astype(np.uint8)
        
        # Save the rotated image
        rotated_image_path = f"rotated_image_{angle}_degrees.png"
        io.imsave(rotated_image_path, rotated_image_RGB)
        print(f"Image has been rotated by {angle} degrees and saved as:", rotated_image_path)
    except Exception as e:
        print("Error:", str(e))

# Check for thresholding request
elif any(keyword in tokens for keyword in threshold_keywords):
    print("The input contains a request to threshold the image.")
    image_path = input("Please provide the path to the image you want to threshold: ")
    try:
        # Load the image using skimage
        image = io.imread(image_path)
        # Convert the image to grayscale
        gray_image = color.rgb2gray(image)
        # Get threshold value using Otsu's method
        thresh = threshold_otsu(gray_image)
        binary = gray_image > thresh
        # Save the thresholded image
        threshold_image_path = "thresholded_image.png"
        io.imsave(threshold_image_path, img_as_ubyte(binary))
        print("Image has been thresholded and saved as:", threshold_image_path)
    except Exception as e:
        print("Error:", str(e))

else:
    print("The input does not contain a recognizable request.")