# myapp/views.py
import os
import cv2
import numpy as np
from django.shortcuts import render
from myapp.stitch_images import stitch_images
from myproject.settings import BASE_DIR
from PIL import Image
from django.views.generic import TemplateView

def panorama_view(request):
    image_paths = [
        os.path.join(BASE_DIR, 'myapp', 'media', f'image{i}.jpg') for i in range(1, 6)
    ]

    # Load images and convert them to 8-bit unsigned integer (CV_8U) and BGR color format
    images = [cv2.imread(path, cv2.IMREAD_COLOR) for path in image_paths]
    images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB) for image in images]

    # Check if all images were loaded successfully
    if all(image is not None for image in images):
        panorama = stitch_images(images)

        # Check if stitching was successful
        if isinstance(panorama, np.ndarray) and panorama.size > 0:
            panorama_path = os.path.join('media', 'panorama.jpg')  # Update the path here

            # Convert the image to 8-bit unsigned integer and save using Pillow
            panorama = cv2.convertScaleAbs(panorama)
            panorama_pil = Image.fromarray(panorama)
            panorama_pil.save(os.path.join(BASE_DIR, 'myapp', panorama_path))
            

            return render(request, 'panorama.html', {'panorama_path': panorama_path})
        else:
            error_message = "Error: Image stitching failed."
    else:
        error_message = "Error: Failed to load all images."

    return render(request, 'error.html', {'error_message': error_message})



# Create your views here.
class HomeView(TemplateView):
    template_name = 'panorama.html'