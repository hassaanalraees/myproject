# myapp/stitch_images.py
import cv2
import numpy as np

def stitch_images(images):
    # Calculate the dimensions of the stitched panorama
    max_height = max(image.shape[0] for image in images)
    total_width = sum(image.shape[1] for image in images)

    # Create an empty canvas for the panorama
    panorama = np.zeros((max_height, total_width, 3), dtype=np.uint8)

    # Calculate the starting column for each image
    current_width = 0
    for image in images:
        h, w = image.shape[:2]
        panorama[:h, current_width:current_width + w] = image
        current_width += w

    return panorama