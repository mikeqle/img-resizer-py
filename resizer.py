import os
from PIL import Image

# Ensure 'output' directory exists, if not, create it
output_dir = './output'
input_dir = "./assets"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get list of all image files in the current directory
image_files = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Iterate over all image files
for image_file in image_files:
    # Open image file
    with Image.open(os.path.join(input_dir, image_file)) as img:
        # Get image size
        width, height = img.size

        # Check if the image is square
        if width == height:
            print(f'Processing file {image_file}...')
            # Resize image
            resized_img = img.resize((100, 100))

            # Save resized image in 'output' directory in webp format
            output_file = f'{output_dir}/resized_{os.path.splitext(image_file)[0]}.webp'
            resized_img.save(output_file, 'webp')
            print(f'Successfully resized and saved {image_file} as {output_file}')
        else:
            print(f'Skipping {image_file} as it is not a square image.')

print("Finished resizing images.")
