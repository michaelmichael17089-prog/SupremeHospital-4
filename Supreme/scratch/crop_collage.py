import os
from PIL import Image

image_path = r"c:\Program Files\Ampps\www\Supreme-1\Supreme\images\dental_concerns_collage.png"
if os.path.exists(image_path):
    img = Image.open(image_path)
    width, height = img.size
    print(f"Original dimensions: {width}x{height}")
    
    # The right collage part starts around 47-48% of the width.
    # Let's crop from 47% to 100% of the width.
    crop_x = int(width * 0.47)
    cropped_img = img.crop((crop_x, 0, width, height))
    
    cropped_img.save(image_path)
    print(f"Cropped image saved successfully with dimensions: {cropped_img.size}")
else:
    print("Image not found!")
